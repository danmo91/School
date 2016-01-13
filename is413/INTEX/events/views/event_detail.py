from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
import homepage.models as hmod
from django.contrib.auth import authenticate, login, logout

templater = get_renderer('events')

'''
    event_detail:

        When user clicks to view 'more info' on Event
        this view get's the event object, associated areas
        and passes them to the template

'''

@view_function
def process_request(request):
    '''
        process_request: Get event and associated areas and pass to template

    '''

    params = {}

    # get event
    event = hmod.Event.objects.get(id = request.urlparams[0])

    # get list of areas
    areas = hmod.Area.objects.filter(event = event)


    # pass to template
    params['event'] = event
    params['areas'] = areas

    return templater.render_to_response(request, 'event_detail.html', params)
