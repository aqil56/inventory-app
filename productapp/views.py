from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from productapp.forms import ProductForm
from productapp.models import Product, Category
# def ProductList(request):
#     product = Product.objects.all()
#     return render(request, 'productapp/product_list.html', {'products': product})


class ProductList(ListView):
    template_name = 'productapp/product_list.html'
    model = Product
    context_object_name = 'products'
    extra_context = {'categories': Category.objects.all()}


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

class ProductNew(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    exclude = ['user']
    template_name = 'productapp/product_new.html'
    success_url = reverse_lazy('product:product_list')
    login_url = 'login'

    def form_valid(self, form):  # MRO
        form.instance.user = self.request.user  # logged in user
        return super(ProductNew, self).form_valid(form)


class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    exclude = ['user']
    template_name = 'productapp/product_update.html'
    success_url = reverse_lazy('product:product_list')

    def form_valid(self, form):  # MRO
        form.instance.user = self.request.user  # logged in user
        return super(ProductUpdate, self).form_valid(form)


class ProductDelete(DeleteView):
    model = Product
    template_name = 'productapp/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product:product_list')
