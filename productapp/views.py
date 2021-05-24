from django.shortcuts import render
from django.http import HttpResponse
from .models import products
# Create your views here.

def index(request):
    product = products.objects.all()
    return render(request, 'productapp/products_list.html', {'products': product})

def desc(request,id):
    product = products.objects.get(pk=id)
    return render(request, 'productapp/products_desc.html', {'product_desc': product})