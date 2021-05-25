from django import forms

from productapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'price')
