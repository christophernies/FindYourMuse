from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    material = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    store = models.ForeignKey(Store)
    item_url = models.CharField(max_length=200)
