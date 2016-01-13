from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
import datetime
from django import forms
import homepage.models as hmod

templater = get_renderer('manager')

'''
    products: CRUD functions for product

'''

@view_function
def process_request(request):
    '''
        process_request: Return list of products, sorted by name
    '''
    params = {}

    # get list of products, sorted by name
    products = hmod.Product.objects.all().order_by('name')

    # pass list to template
    params['products'] = products

    return templater.render_to_response(request, 'products.html', params)


@view_function
def create(request):
    '''
        create: Creates empty product, sends user to edit page
    '''
    params = {}

    # create product object
    product = hmod.Product()

    # save new product
    product.save()

    # send user to edit page
    return HttpResponseRedirect('/manager/products.edit/{}/'.format(product.id))

@view_function
def edit(request):
    '''
        edit: Sends form for editing proudct details
    '''
    params = {}

    # try to get product
    try:
        product = hmod.Product.objects.get(id = request.urlparams[0])
    except hmod.Product.DoesNotExist:
        # redirect to product list page
        return HttpResponseRedirect('/manager/products/')

    # initialize event product form
    form = ProductEditForm(initial={
        'name' : product.name,
        'description': product.description,
        'category': product.category,
        'current_price': product.current_price,

    })

    # if POST
    if request.method == 'POST':
        # get form from request
        form = ProductEditForm(request.POST)

        # if form is valid
        if form.is_valid():

            # item product object
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.current_price = form.cleaned_data['current_price']


            product.save()

            # send to product list page
            return HttpResponseRedirect('/manager/products/')


    params['form'] = form

    return templater.render_to_response(request, 'products.edit.html', params)

@view_function
def delete(request):
    '''
        delete: Deletes selected Product
    '''
    params = {}

    # try and get product
    try:
        product = hmod.Product.objects.get(id=request.urlparams[0])

    # if product does not exist
    except hmod.Product.DoesNotExist:

        # go back to product list page
        return HttpResponseRedirect('/manager/products/')


    # else, delete product
    product.delete()

    # return to product list page
    return HttpResponseRedirect('/manager/products/')


class ProductEditForm(forms.Form):
    '''
        ProductEditForm: Fields to edit product name, description, category, current_price
    '''
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Master Sword'}))
    description = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Temple of Light'}))
    category = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Weapon'}))
    current_price = forms.DecimalField(max_digits=7,decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '69.00'}))
