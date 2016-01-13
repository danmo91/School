from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
import homepage.models as hmod
from django.contrib.auth import authenticate, login, logout
import requests
import datetime
from django.core.mail import send_mail, EmailMessage

templater = get_renderer('shop')

'''
    checkout:

        - ensures user is logged in
        - sends user to order sumary page
        - collects payment and shipping information
        - emails receipt to user
        - sends user to receipt page

'''

@view_function
def process_request(request):
    '''
        process_request: Generates order summary page with list of products and items
    '''
    params = {}

    # check to see if user needs to login to checkout
    user = request.user
    if request.user.username == '':
        request.session['login_required'] = True
        return HttpResponseRedirect('/shop/index/')

    # get shopping_cart items
    items = {}

    if 'shopping_cart' in request.session:

        item_ids = request.session['shopping_cart']

        for key,value in item_ids.items():

            item = hmod.Product.objects.get(id = key)

            item_container = []
            item_container.append(item)
            item_container.append(value)


            items[item.id] = item_container

    params['items'] = items

    # get rental_cart items
    rentals = []
    if 'rental_cart' in request.session:

        rental_ids = request.session['rental_cart']

        for rental_id in rental_ids:
            rental = hmod.Item.objects.get(id=rental_id)
            rentals.append(rental)

    params['rentals'] = rentals

    return templater.render_to_response(request, 'confirm_order.html', params)

@view_function
def enter_payment(request):
    '''
        enter_payment: Collects and verifies shipping and payment info
    '''
    params = {}

    form = CheckoutForm(initial = {
        'creditcard' : '4732817300654',
        'exp_month' : '10',
        'exp_year' : '15',
        'cvc' : '411',
    })

    if request.method == 'POST':
        # get form
        form = CheckoutForm(request.POST)
        if form.is_valid():
            request.session['credit_card'] = {
                'creditcard' : '4732817300654',
                'exp_month' : '10',
                'exp_year' : '15',
                'cvc' : '411',
            }

            # check if user has an address
            user = hmod.User.objects.get(id=request.user.id)
            has_address = hmod.Address.objects.filter(user = user)

            if has_address.count() == 0:

                # save address information
                address = hmod.Address()

                address.street = form.cleaned_data['street']
                address.city = form.cleaned_data['city']
                address.state = form.cleaned_data['state']
                address.zip_code = form.cleaned_data['zip_code']
                address.save()

                # associate user with address
                address.user = user
                address.save()

            return HttpResponseRedirect('/shop/checkout.charge_card')


    params['form'] = form

    return templater.render_to_response(request, 'enter_payment.html', params)

def get_total(request):
    '''
        get_total: Returns the total cost of all items and products in cart
    '''

    total = 0

    # get list of items in shopping_cart
    if 'shopping_cart' in request.session:

        for ID,qty in request.session['shopping_cart'].items():
            product = hmod.Product.objects.get(id=ID)
            total += product.current_price * qty

    # don't forget rental_cart
    if 'rental_cart' in request.session:
        rental_ids = request.session['rental_cart']

        for rental_id in rental_ids:
            rental = hmod.Item.objects.get(id=rental_id)
            total += rental.rental_price

    print('total:', total)

    return total

@view_function
def charge_card(request):
    '''
        charge_card: charges card via REST API,
    '''

    params = {}

    params['form'] = CheckoutForm()


    # should i do this in the clean method?  When do i want to charge??

    # send the request with the data
    API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
    API_KEY = 'aa846fb6f04d54c4b952561399e40d84'

    creditcard = request.session['credit_card']['creditcard']
    exp_month = request.session['credit_card']['exp_month']
    exp_year = request.session['credit_card']['exp_year']
    cvc = request.session['credit_card']['cvc']

    del request.session['credit_card']

    r = requests.post(API_URL, data={
        'apiKey': API_KEY,
        'currency': 'usd',
        'amount': get_total(request), # my total
        'type': 'Visa',
        'number': creditcard,
        'exp_month': exp_month,
        'exp_year': exp_year,
        'cvc': cvc,
        'name': 'Cosmo Limesandal',
        'description': 'Charge for cosmo@is411@byu.edu',
    })

    # parse response dictionary
    resp = r.json()
    if 'error' in resp:
        print('ERROR: ', resp['error'])

    else:

        # if order, create order object
        if len(request.session['shopping_cart']) > 0:

            order = hmod.Order()

            order.order_date = datetime.date.today()
            order.total = get_total(request)
            user = hmod.User.objects.get(id = request.user.id)
            order.user = user
            order.charge_id = resp['ID']
            order.save()

        # if rental, create rental objects for each rental
        if len(request.session['rental_cart']) > 0:
            rental_ids = request.session['rental_cart']

            for rental_id in rental_ids:
                r = hmod.Item.objects.get(id=rental_id)

                rental = hmod.Rental()
                rental.description = r.name
                rental.rental_date = datetime.date.today()
                rental.due_date = (datetime.date.today() + datetime.timedelta(days=30))
                rental.available = False
                rental.charge_id = resp['ID']
                user = hmod.User.objects.get(id=request.user.id)
                rental.user = user
                rental.item = r
                rental.save()

        # redirect to receipt
        return HttpResponseRedirect('/shop/checkout.receipt')

    return templater.render_to_response(request, 'enter_payment.html', params)

@view_function
def receipt(request):
    '''
        receipt: sends receipt email to user, sends user to receipt page
    '''

    params = {}

    params['total'] = get_total(request)

    # get items in shopping_cart
    items = {}

    if 'shopping_cart' in request.session:
        item_ids = request.session['shopping_cart']

        for key,value in item_ids.items():

            item = hmod.Product.objects.get(id = key)

            item_container = []
            item_container.append(item)
            item_container.append(value)


            items[item.id] = item_container

        # clear out shopping cart
        del request.session['shopping_cart']

    # pass to template
    params['items'] = items

    # get items in rental_cart
    rentals = []

    if 'rental_cart' in request.session:
        rental_ids = request.session['rental_cart']

        for rental_id in rental_ids:
            rental = hmod.Item.objects.get(id=rental_id)
            rental.available = False
            rental.save()
            rentals.append(rental)

        # delete rental_cart
        del request.session['rental_cart']

    # pass to template
    params['rentals'] = rentals

    # get user's address
    user = hmod.User.objects.get(id=request.user.id)
    address = hmod.Address.objects.get(user=user)

    params['address'] = address
    params['user'] = user.full_name
    params['date'] = datetime.date.today()

    #Send Email
    if request.user.email != "":
        subject = "CHF Receipt"
        to = [request.user.email]
        from_email = 'dan.morain91@gmail.com'



        message = templater.render(request, 'receipt_email.html', params)

        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()

    return templater.render_to_response(request, 'receipt.html', params)


class CheckoutForm(forms.Form):
    '''
        CheckoutForm: Collects shipping and credit card information
    '''
    street = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'street'}))
    city = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}))
    state = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'state'}))
    zip_code = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zip'}))
    creditcard = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'credit card number'}))
    exp_month = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'exp. month "mm"'}))
    exp_year = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'exp. year "yy"'}))
    cvc = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cvc'}))
