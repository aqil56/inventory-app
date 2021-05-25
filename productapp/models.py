from django.db import models

# Create your models here.


# class Category(models.Model):
#     name = models.CharField(max_length=30)

#     class Meta:
#         verbose_name_plural = 'categories'

#     def __str__(self):
#         return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
