from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
import datetime
from django import forms
import homepage.models as hmod

templater = get_renderer('manager')

'''
    events: CRUD functions for events

'''

@view_function
def process_request(request):
    '''
        process_request: Return list of events, sorted by start date
    '''

    params = {}

    # get list of events, sorted by start date
    events = hmod.Event.objects.all().order_by('start')

    # pass list to template
    params['events'] = events

    return templater.render_to_response(request, 'events.html', params)


@view_function
def create(request):
    '''
        create: Creates empty event, sends user to edit page
    '''
    params = {}

    # create event object
    event = hmod.Event()

    # save new event
    event.save()

    # send user to edit page
    return HttpResponseRedirect('/manager/events.edit/{}/'.format(event.id))

@view_function
def edit(request):
    '''
        edit: Sends form for editing event details
    '''
    params = {}

    # try to get event
    try:
        event = hmod.Event.objects.get(id = request.urlparams[0])
    except hmod.Event.DoesNotExist:
        # redirect to event list page
        return HttpResponseRedirect('/manager/events/')

    # initialize event edit form
    form = EventEditForm(initial={
        'name' : event.name,
        'description': event.description,
        'start': event.start,
        'end': event.end,
    })

    # if POST
    if request.method == 'POST':
        # get form from request
        form = EventEditForm(request.POST)

        # if form is valid
        if form.is_valid():

            print('Form is valid')

            # edit event object
            event.name = form.cleaned_data['name']
            event.description = form.cleaned_data['description']
            event.start = form.cleaned_data['start']
            event.end = form.cleaned_data['end']

            # implement after form is done
            # event.venue = form.cleaned_data['name']

            event.save()

            # send to event list page
            return HttpResponseRedirect('/manager/events/')


    params['form'] = form

    return templater.render_to_response(request, 'events.edit.html', params)

@view_function
def delete(request):
    '''
        delete: Deletes selected Event
    '''
    params = {}

    # try and get event
    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])

    # if event does not exist
    except hmod.Event.DoesNotExist:
        # go back to event list page
        return HttpResponseRedirect('/manager/events/')

    # else, delete event
    event.delete()

    # return to event list page
    return HttpResponseRedirect('/manager/events/')


class EventEditForm(forms.Form):
    '''
        EventEditForm: Fields to edit event name, description, start date, end date
    '''
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ward BBQ'}))
    description = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "7pm @ Dan's house.  Be there or be [ ]"}))
    start = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2015-3-12'}))
    end = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2015-3-13'}))
