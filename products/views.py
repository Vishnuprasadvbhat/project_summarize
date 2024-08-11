from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import products
# Create your views here


def hello(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())


def productsname(request):
    allproducts = products.objects.all().values()
    template = loader.get_template('products_page.html')
    context = {
        'allproducts': allproducts
    }

    return HttpResponse(template.render(context, request))

def solo_products(request):
    template = loader.get_template('solo.html')
    return HttpResponse(template.render())


