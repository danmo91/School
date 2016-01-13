from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
from django.contrib.auth import authenticate, login, logout
import homepage.models as hmod
import datetime

templater = get_renderer('manager')

'''
    rentals: CRUD functions for rentals

'''

@view_function
def process_request(request):
    '''
        process_request: Return list of rentals, sorted by due_date
    '''
    params = {}

    # get list of rentals, sorted by due date
    rentals = hmod.Rental.objects.all().order_by('due_date')

    # pass list to template
    params['rentals'] = rentals

    return templater.render_to_response(request, 'rentals.html', params)

@view_function
def create(request):
    '''
        create: Creates empty rental, sends user to edit page
    '''
    params = {}

    # create rental object
    rental = hmod.Rental()

    # save new rental
    rental.save()

    # send user to rental page
    return HttpResponseRedirect('/manager/rentals.edit/{}/'.format(rental.id))

@view_function
def edit(request):
    '''
        edit: Sends form for editing rental details
    '''

    params = {}

    # try to get rental
    try:
        rental = hmod.Rental.objects.get(id = request.urlparams[0])
    except hmod.Rental.DoesNotExist:
        # redirect to rental list page
        return HttpResponseRedirect('/manager/rentals/')

    # initialize rental edit form
    form = RentalEditForm(initial={
        'description': rental.description,
        'rental_date': rental.rental_date,
        'due_date': rental.due_date,

    })

    # if POST
    if request.method == 'POST':
        # get form from request
        form = RentalEditForm(request.POST)

        # if form is valid
        if form.is_valid():

            # item event object
            rental.description = form.cleaned_data['description']
            rental.rental_date = form.cleaned_data['rental_date']
            rental.due_date = form.cleaned_data['due_date']

            rental.save()

            # send to rental list page
            return HttpResponseRedirect('/manager/rentals/')

    params['form'] = form

    return templater.render_to_response(request, 'rentals.edit.html', params)

@view_function
def delete(request):
    '''
        delete: Deletes selected rentals
    '''
    params = {}

    # try and get rental
    try:
        rental = hmod.Rental.objects.get(id=request.urlparams[0])

    # if rental does not exist
    except hmod.Rental.DoesNotExist:

        # go back to rental list page
        return HttpResponseRedirect('/manager/rentals/')


    # else, delete rental
    rental.delete()

    # return to rental list page
    return HttpResponseRedirect('/manager/rentals/')


@view_function
def overdue(request):
    '''
        overdue: gets list of overdue rentals in intervals of 30 days, 60 days, 90 days
    '''

    params = {}

    # set range intervals
    today = datetime.date.today()
    start_date = (datetime.date.today() - datetime.timedelta(days=60))

    # get rentals over 30
    end_date = (datetime.date.today() - datetime.timedelta(days=30))
    over_30 = hmod.Rental.objects.filter(due_date__range = (start_date, end_date), returned=False)

    # get rentals over 60
    start_date = (datetime.date.today() - datetime.timedelta(days=90))
    end_date = (datetime.date.today() - datetime.timedelta(days=60))
    over_60 = hmod.Rental.objects.filter(due_date__range = (start_date, end_date), returned=False)

    # get rentals over 90
    start_date = (datetime.date.today() - datetime.timedelta(days=365))
    end_date = (datetime.date.today() - datetime.timedelta(days=90))
    over_90 = hmod.Rental.objects.filter(due_date__range = (start_date, end_date), returned=False)

    end_date = (datetime.date.today() - datetime.timedelta(days=90))
    overdue_items = hmod.Rental.objects.filter(due_date__range = (start_date, end_date))

    params['over_30'] = over_30
    params['over_60'] = over_60
    params['over_90'] = over_90

    return templater.render_to_response(request, 'rentals.overdue.html', params)


class RentalEditForm(forms.Form):
    '''
        RentalEditForm: Fields to edit rental description, rental_date, due_date
    '''

    description = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Not another pony ride'}))
    rental_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2015-04-05'}))
    due_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2015-04-05'}))
