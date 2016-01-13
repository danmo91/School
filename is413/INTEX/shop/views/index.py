from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
import homepage.models as hmod
from django.contrib.auth import authenticate, login, logout

templater = get_renderer('shop')

'''
    index:

        - reminds user to login
        - displays list of all products
        - displays list of all rentals
        - allows user to search for specific products
        - allows user to logout
        - allows user to signup for new account
'''

@view_function
def process_request(request):
    '''
        process_request: Displays list of products for sale to user
    '''
    params = {}

    # check to see if login is required to checkout
    params['login_required'] = False

    if 'login_required' in request.session:
        params['login_required'] = True
        del request.session['login_required']

    #Get list of all items
    items = hmod.Product.objects.all()

    #Pass list of items to template
    params['items'] = items

    # get items in cart
    num_items = 0

    if 'shopping_cart' in request.session:
        num_items = len(request.session['shopping_cart'])

    params['num_items'] = num_items

    return templater.render_to_response(request, 'index.html', params)

@view_function
def rentals(request):
    '''
        rentals: Displays list of items available for rent to user
    '''

    params = {}

    #Get list of all rental items
    items = hmod.Item.objects.filter(available = True)

    #Pass list of items to template
    params['items'] = items

    # get items in cart
    num_items = 0

    if 'shopping_cart' in request.session:
        num_items = len(request.session['shopping_cart'])

    params['num_items'] = num_items

    return templater.render_to_response(request, 'rental_index.html', params)


@view_function
def search(request):
    '''
        search: Returns a list of filtered products by input field
    '''
    params = {}

    search_data = request.REQUEST.get('input')

    items = []

    if search_data != '':
        if request.method == 'POST':
            items = hmod.Product.objects.filter(name=search_data)
    else:
        items = hmod.Item.objects.all()

    params['items'] = items

    return templater.render_to_response(request, 'index.search.html', params)


@view_function
def logout_view(request):
    '''
        logout_view: Logout user and send to shop page
    '''
    logout(request)

    return HttpResponseRedirect('/shop/index/')

@view_function
def signup(request):
    '''
        signup: Loads modal and validates signup form
    '''
    params = {}

    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():

            # update user object
            user = hmod.User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.phone = form.cleaned_data['phone']

            user.save()

            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'] )

            login(request, user)

            return HttpResponse('''
                    <script>
                        window.location.href = window.location.href
                    </script>

                '''
                )


    params['form'] = form

    return templater.render_to_response(request, 'index.signup.html', params)


class SignupForm(forms.Form):
    '''
        SignupForm: collects information for new users, trying to sign up and makes sure they have unique username
    '''
    username = forms.CharField(label="Username", required=True, max_length=100)
    password = forms.CharField(label="Password", required=True,max_length=100, widget = forms.PasswordInput)
    first_name = forms.CharField(label="First Name",required=True, max_length=100)
    last_name = forms.CharField(label="Last Name", required=True, max_length=100)
    email = forms.EmailField(label="Email", required=True, max_length=100)
    phone = forms.CharField(label="Phone", required=True, max_length=100)

    def clean(self):
        user = hmod.User.objects.filter(username=self.cleaned_data['username'])
        if user.count() > 0:
            raise forms.ValidationError('%s already exists' % self.cleaned_data['username'])
        return self.cleaned_data
