from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
import homepage.models as hmod

templater = get_renderer('shop')

'''
    shopping_cart:

        - fills shopping cart modal with items and products
        - add items and products to cart
        - delete items and products from cart

'''


@view_function
def process_request(request):
    '''
        process_request: returns list of items and products to cart template
    '''

    params = {}

    # get shopping cart objects
    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}

    item_ids = request.session['shopping_cart']

    items = {}

    for key,value in item_ids.items():

        item = hmod.Product.objects.get(id = key)

        item_container = []
        item_container.append(item)
        item_container.append(value)


        items[item.id] = item_container

    params['items'] = items


    # get rental cart objects
    if 'rental_cart' not in request.session:
        request.session['rental_cart'] = []

    rental_ids = request.session['rental_cart']

    rentals = []

    for rental in rental_ids:
        # get object
        rental = hmod.Item.objects.get(id=rental)

        # add to list
        rentals.append(rental)

    print('rentals:', rentals)

    # pass to view
    params['rentals'] = rentals

    return templater.render_to_response(request, 'shopping_cart.html', params)


@view_function
def add(request):
    '''
        add: add's item or product to rental or shopping cart
        returns user to view cart
    '''

    object_id = request.urlparams[0]
    qty = int(request.urlparams[1])
    product = request.urlparams[2]

    # product or item
    if product == 'true':

        # add to the shopping_cart

        if 'shopping_cart' not in request.session:
            request.session['shopping_cart'] = {}

        if object_id in request.session['shopping_cart']:
            request.session['shopping_cart'][object_id] += qty

        else:
            request.session['shopping_cart'][object_id] = qty

    else:

        # add to the rental_cart
        if 'rental_cart' not in request.session:
            request.session['rental_cart'] = [] # list of item_id's

        if object_id not in request.session['rental_cart']:
            request.session['rental_cart'].append(object_id)

    request.session.modified = True

    return HttpResponseRedirect('/shop/shopping_cart/')

@view_function
def delete(request):
    '''
        delete: deletes selected item or product form cart
        returns user to cart view
    '''

    # product_id and quantity
    object_id = request.urlparams[0]
    product = request.urlparams[1]

    # product or item?

    if product == 'True':
        del request.session['shopping_cart'][object_id]
    else:
        request.session['rental_cart'].remove(object_id)


    request.session.modified = True

    return HttpResponseRedirect('/shop/shopping_cart/')
