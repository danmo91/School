from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
import datetime
from django import forms
import homepage.models as hmod

templater = get_renderer('manager')

'''
    users: CRUD functions for users

'''

@view_function
def process_request(request):
    '''
        process_request: Return list of users, sorted by last name
    '''
    params = {}

    # get list of users, sorted by last name
    users = hmod.User.objects.all().order_by('last_name')

    # pass list to template
    params['users'] = users

    return templater.render_to_response(request, 'users.html', params)

@view_function
def create(request):
    '''
        create: Creates empty user, sends user to edit page
    '''

    params = {}

    user = hmod.User()
    user.username = ''
    user.last_name = ''
    user.first_name = ''
    user.email = ''
    user.phone = ''

    user.save()

    # send user to edit page
    return HttpResponseRedirect('/manager/users.edit/{}'.format(user.id))

@view_function
def edit(request):
    '''
        edit: Sends form for editing user details
    '''

    params = {}

    # try to get user
    try:
        user = hmod.User.objects.get(id = request.urlparams[0])
    except hmod.User.DoesNotExist:
        # redirect to user list page
        return HttpResponseRedirect('/manager/users/')

    # initialize event user form
    form = UserEditForm(initial={
        'username' : user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'phone': user.phone,

    })

    # if POST
    if request.method == 'POST':
        # get form from request
        form = UserEditForm(request.POST)

        # for use in clean method
        form.user_id = user.id

        # if form is valid
        if form.is_valid():

            # edit user object
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.phone = form.cleaned_data['phone']

            user.save()

            if form.cleaned_data['password'] != '':

                user.set_password(form.cleaned_data['password'])


            user.save()

            # send to event list page
            return HttpResponseRedirect('/manager/users/')


    params['form'] = form

    return templater.render_to_response(request, 'events.edit.html', params)

@view_function
def delete(request):
    '''
        delete: Deletes selected user
    '''

    params = {}

    # try and get user
    try:
        user = hmod.User.objects.get(id=request.urlparams[0])

    # if user does not exist
    except hmod.User.DoesNotExist:

        # go back to user list page
        return HttpResponseRedirect('/manager/users/')


    # else, delete user
    user.delete()

    # return to user list page
    return HttpResponseRedirect('/manager/users/')


class UserEditForm(forms.Form):
    '''
        UserEditForm: Fields to edit user username, password, first_name, last_name, email, phone
    '''
    username = forms.CharField(label="Username", required=True, max_length=100)
    password = forms.CharField(label="Password", required=False, widget = forms.PasswordInput)
    first_name = forms.CharField(label="First Name",required=True, max_length=100)
    last_name = forms.CharField(label="Last Name", required=True, max_length=100)
    email = forms.EmailField(label="Email", required=True, max_length=100)
    phone = forms.CharField(label="Phone", required=True, max_length=100)

    def clean_username(self):
        # check if username is unique
        user = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.user_id)

        if user.count() > 0:
            raise forms.ValidationError('%s already exists' % self.cleaned_data['username'])

        return self.cleaned_data['username']
