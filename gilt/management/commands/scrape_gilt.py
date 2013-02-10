from django.core.management import BaseCommand
from gilt.models import Store, Product

from webapp.gilt_apis import *

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        men_store, created = Store.objects.get_or_create(name='men')
        women_store, created = Store.objects.get_or_create(name='women')
        men_store.save()
        women_store.save()

        sales = json.loads(GiltActiveSales('men'))["sales"]
        for sale in sales:
            try:
                product_urls = sale['products']
                for product_url in product_urls:
                    product = json.loads(GiltLookup(product_url))
                    image_urls = product['image_urls']
                    brand = product['brand']
                    material = product['content']['material']
                    image_url = image_urls['300x400'][0]['url']
                    item_url = product['url']

                    product = Product.objects.create(material=material, brand=brand, image_url=image_url, store=men_store, item_url=item_url)

            except KeyError:
                continue

#description = product['content']['description']



