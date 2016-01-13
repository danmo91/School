from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
import homepage.models as hmod
from django.contrib.auth import authenticate, login, logout

templater = get_renderer('events')

'''
    area_detail:

        When user clicks to view 'more info' on Area
        this view get's the area object, associated area_items
        and passes them to the template

'''

@view_function
def process_request(request):
    '''
        process_request: Get area and associated area_items and pass to template

    '''

    params = {}

    # get area
    area = hmod.Area.objects.get(id = request.urlparams[0])

    # get list of products for sale
    products = hmod.Area_Item.objects.filter(area=area)

    # pass to template
    params['area'] = area
    params['products'] = products

    return templater.render_to_response(request, 'area_detail.html', params)
