from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from productapp.forms import ProductForm
from productapp.models import Product
# def ProductList(request):
#     product = Product.objects.all()
#     return render(request, 'productapp/product_list.html', {'products': product})


class ProductList(ListView):
    template_name = 'productapp/product_list.html'
    model = Product
    context_object_name = 'products'


# def ProductDetail(request, id):
#     product = Product.objects.get(id=id)
#     return render(request, 'productapp/product_detail.html', {'product': product})

class ProductDetail(DetailView):
    model = Product
    template_name = 'productapp/product_detail.html'
    context_object_name = 'product'


# def ProductNew(request):
#     if request.method == 'get':
#         form = ProductForm()
#         return render(request, 'productapp/product_new.html', {'form': form})
#     else:
#     form = self.form_class(request.POST)
#         if form.is_valid():
#             post=form.save()
#             post.save()
#             return redirect('product_detail', pk=post.pk)
#         return render(request, 'productapp/product_new.html', {'form': form})

class ProductNew(CreateView):
    model = Product
    fields = ['name', 'category', 'description', 'price']
    template_name = 'productapp/product_new.html'
    success_url = reverse_lazy('product:product_list')


class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'category', 'description', 'price']
    template_name = 'productapp/product_update.html'
    success_url = reverse_lazy('product:product_list')


class ProductDelete(DeleteView):
    model = Product
    template_name = 'productapp/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product:product_list')
