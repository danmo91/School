from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.mail import send_mail, EmailMessage
import datetime
from django import forms
import homepage.models as hmod
from decimal import Decimal

templater = get_renderer('manager')

'''
    return: CRUD functions for returns

'''

@view_function
def process_request(request):
    '''
        process_request: Return list of rentals that have not been returned
    '''

    params = {}

    rentals = hmod.Rental.objects.filter(returned = False)

    params['rentals'] = rentals

    return templater.render_to_response(request, 'return.html', params)

@view_function
def dash(request):
    '''
        process_request: Return list of rentals that have not been returned
    '''

    params = {}


    return templater.render_to_response(request, 'dash.html', params)


@view_function
def return_form(request):
    '''
        return_form: Sends return form to agent to collect information about return
    '''

    params = {}

    # get rental information
    object_id = request.urlparams[0]
    rental = hmod.Rental.objects.get(id=object_id)

    # get late fee
    late_fee = 0.00
    if rental.due_date < datetime.date.today():
        late_fee = 3.99

    form = ReturnForm()

    if request.method == 'POST':

        form = ReturnForm(request.POST)
        if form.is_valid():

            # set return date
            rental.return_date = datetime.date.today()
            rental.returned = True
            rental.save()


            # update item
            if rental.item:
                item = rental.item
                item.available = True
                if form.cleaned_data['damage']:
                    item.condition = form.cleaned_data['damage']
                item.save()

            # update user
            if rental.user:
                user = rental.user

                if form.cleaned_data['late_fee'] != '' and form.cleaned_data['late_fee_waived'] == False:
                    user.account_balance += int(form.cleaned_data['late_fee'])

                if form.cleaned_data['damage_fee'] != '' and form.cleaned_data['damage_fee_waived'] == False:
                    user.account_balance += int(form.cleaned_data['damage_fee'])

                user.save()


            return HttpResponse('''
                <script>
                    window.location.href = window.location.href
                </script>

            '''
            )

    params['late_fee'] = late_fee
    params['form'] = form
    params['rental'] = rental

    return templater.render_to_response(request, 'return_form.html', params)

@view_function
def send_email(request):
    '''
        send_email:

            - Get's list of overdue rentals at input interval (batch)
            - Get's list of user emails
            - sends email to users with overdue items
    '''
    params = {}

    batch = request.urlparams[0]

    overdue_rentals = []

    today = datetime.date.today()
    start = (datetime.date.today() - datetime.timedelta(days=60))

    if batch == 'thirty':
        # get list of overdue rentals
        end = (datetime.date.today() - datetime.timedelta(days=30))
        overdue_rentals = hmod.Rental.objects.filter(due_date__range = (start, end), returned=False)

    if batch == 'sixty':
        # get list of overdue rentals
        start = (datetime.date.today() - datetime.timedelta(days=90))
        end = (datetime.date.today() - datetime.timedelta(days=60))
        overdue_rentals = hmod.Rental.objects.filter(due_date__range = (start, end), returned=False)

    if batch == 'ninety':
        # get list of overdue rentals
        start = (datetime.date.today() - datetime.timedelta(days=365))
        end = (datetime.date.today() - datetime.timedelta(days=90))
        overdue_rentals = hmod.Rental.objects.filter(due_date__range = (start, end), returned=False)

    # get users emails
    user_emails = []
    for rental in overdue_rentals:
        if rental.user:
            if rental.user.email != '':
                if rental.user.email not in user_emails:
                    user_emails.append(rental.user.email)

    print('user_emails:', user_emails)

    # send email to each user
    if user_emails:
        for email in user_emails:

            # get list of over_due rentals
            user = hmod.User.objects.get(email=email)
            rentals = hmod.Rental.objects.filter(due_date__range = (start, end), returned=False, user = user)
            params['rentals'] = rentals
            params['date'] = datetime.date.today()
            params['user'] = user.full_name


            #Send Email
            if  email != '':
                subject = "Your Rental is Overdue"
                to = [email]
                from_email = 'dan.morain91@gmail.com'

                message = templater.render(request, 'overdue_email.html', params)

                msg = EmailMessage(subject, message, to=to, from_email=from_email)
                msg.content_subtype = 'html'
                msg.send()

        return HttpResponse('1')


    return HttpResponse('0')


class ReturnForm(forms.Form):
    '''
        ReturnForm: Fields to collect return info- damage, late_fee, damage_fee
    '''
    DAMAGE_CHOICES = (
        ('', ''),
        (1, '1.00'),
        (2, '2.00'),
        (3, '3.00'),
        (4, '4.00'),
    )

    LATE_CHOICES = (
        ('', ''),
        (2, '2.00'),
    )

    damage = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control field', 'placeholder': 'Enter damage description'}))
    late_fee = forms.CharField(required=False, widget=forms.Select(choices=LATE_CHOICES, attrs={'class': 'selectpicker', 'data-width':'100%', 'title':'Late Fee'}))
    damage_fee = forms.CharField(required=False, widget=forms.Select(choices=DAMAGE_CHOICES, attrs={'class': 'selectpicker', 'data-width':'100%', 'title':'Damage Fee'}))
    late_fee_waived = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'type':"checkbox",'class':"my-checkbox"}))
    damage_fee_waived = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'type':"checkbox",'class':"my-checkbox right"}))
