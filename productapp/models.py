from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey('Category', related_name='product', on_delete=models.CASCADE,null=True)
    # category = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name
