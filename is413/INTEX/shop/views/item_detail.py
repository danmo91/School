from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
import homepage.models as hmod
from django.contrib.auth import authenticate, login, logout

templater = get_renderer('shop')

'''
    item_detail:

        - returns product to detail template
        - returns item to detail template
'''

@view_function
def process_request(request):
    '''
        process_request: returns selected product to detail template
    '''
    params = {}

    form = SearchForm()

    params['form'] = form

    # get the id of the item

    item_id = request.urlparams[0]

    # get the item out of the db

    item = hmod.Product.objects.get(id = item_id)

    # send item to template

    params['item'] = item

    # get number of items in cart
    num_items = 0
    if 'shopping_cart' in request.session:
        num_items = len(request.session['shopping_cart'])

    params['num_items'] = num_items

    return templater.render_to_response(request, 'item_detail.html', params)

@view_function
def rental(request):
    '''
        rental: returns selected item to detail template
    '''

    params = {}

    # get the id of the item
    item_id = request.urlparams[0]

    # get the item out of the db
    item = hmod.Item.objects.get(id = item_id)

    # send item to template

    params['item'] = item

    # get number of items in cart
    num_items = 0
    if 'shopping_cart' in request.session:
        num_items = len(request.session['shopping_cart'])

    params['num_items'] = num_items


    return templater.render_to_response(request, 'rental_item_detail.html', params)


class SearchForm(forms.Form):
    '''
        SearchForm: collects input for searching products
    '''

    input_field = forms.CharField(required=True, widget=forms.TextInput(attrs ={'placeholder':'Search', 'class':'form-control'}))
