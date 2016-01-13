from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
import homepage.models as hmod
from django.contrib.auth import authenticate, login, logout

templater = get_renderer('events')

'''
    index: Main event list page
'''

@view_function
def process_request(request):
    '''
        process_request: Get events pass to template

    '''
    params = {}

    # get list of events
    events = hmod.Event.objects.all()

    # pass to template
    params['events'] = events

    return templater.render_to_response(request, 'index.html', params)
