from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    material = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    store = models.ForeignKey(Store)
    item_url = models.CharField(max_length=200)
    sale_price = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    name = models.CharField(max_length=200)
    sale_price = models.CharField(max_length=200)
    msrp_price = models.CharField(max_length=200)

def __unicode(self):
        return "material %s brand %s store %s" % (self.material, self.brand, self.store)
