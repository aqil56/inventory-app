from django.db import models

# Create your models here.


class products(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name