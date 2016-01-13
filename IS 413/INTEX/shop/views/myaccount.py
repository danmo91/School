from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
import homepage.models as hmod
from django.contrib.auth import authenticate, login, logout

templater = get_renderer('shop')

'''
    myaccount:

        - returns logged in user's account information
        - allows user to edit account information
        - allows user to change password

'''

@view_function
def process_request(request):
    '''
        process_request: returns user object to account template
    '''

    params = {}

    user_id = request.user.id

    try:
        user = hmod.User.objects.get(id=user_id)

    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/shop/index/')

    params['user'] = user


    # get items in cart
    num_items = 0

    if 'shopping_cart' in request.session:
        num_items = len(request.session['shopping_cart'])

    params['num_items'] = num_items

    return templater.render_to_response(request, 'myaccount.html', params)

@view_function
def edit(request):
    '''
        edit: returns and validates edit form which updates user object
    '''

    params = {}

    user = hmod.User.objects.get(id=request.user.id)

    print("user_id:", user.id)

    form = UserEditForm(initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email,
        'phone': user.phone,
        'user_id' : user.id,
    })

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        form.user_id = user.id
        if form.is_valid():
            print('form is valid')
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.phone = form.cleaned_data['phone']
            # update user object

            user.save()

            return HttpResponse('''
                    <script>
                        window.location.href = window.location.href
                    </script>

                '''
                )


    params['form'] = form


    return templater.render_to_response(request, 'myaccount.edit.html', params)


@view_function
def change_password(request):
    '''
        change_password: returns and validates change_password form, allows user to change password
    '''

    params = {}

    user = hmod.User.objects.get(id=request.user.id)
    saved_username = user.username

    form = ChangePasswordForm()

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        form.username = user.username
        if form.is_valid():
            print('form is valid')

            # update user object
            user.set_password(form.cleaned_data['new_password'])
            user.save()


            user = authenticate(username = saved_username, password = form.cleaned_data['new_password'] )
            login(request, user)

            return HttpResponse('''
                    <script>
                        window.location.href = window.location.href
                    </script>

                '''
                )


    params['form'] = form


    return templater.render_to_response(request, 'myaccount.change_password.html', params)


class UserEditForm(forms.Form):
    '''
        UserEditForm: collects information used to edit user object
    '''

    username = forms.CharField(label="Username", required=True, max_length=100)
    first_name = forms.CharField(label="First Name",required=True, max_length=100)
    last_name = forms.CharField(label="Last Name", required=True, max_length=100)
    email = forms.EmailField(label="Email", required=True, max_length=100)
    phone = forms.CharField(label="Phone", required=True, max_length=100)

    def clean(self):
        print(self.cleaned_data)
        user = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.user_id)

        if user.count() > 0:
            raise forms.ValidationError('%s already exists' % self.cleaned_data['username'])

        return self.cleaned_data

class ChangePasswordForm(forms.Form):
    '''
        ChangePasswordForm: collects old password and double confirms new password, raises error when incorrect password is passed
    '''

    old_password = forms.CharField(label="Old Password", required=True, widget = forms.PasswordInput)
    new_password = forms.CharField(label="New Password", required=True, widget = forms.PasswordInput)
    reenter_password = forms.CharField(label="Re-enter Password", required=True, widget = forms.PasswordInput)

    def clean(self):

        # try and authenticate
        if self.is_valid():

            user = authenticate(username=self.username, password = self.cleaned_data['old_password'])

            if user is None:
                raise forms.ValidationError('Old Password incorrect')

            if self.cleaned_data['new_password'] != self.cleaned_data['reenter_password']:
                raise forms.ValidationError('Passwords do not match')

        return self.cleaned_data
