from django.core.management import BaseCommand
from gilt.models import Store, Product

from webapp.gilt_apis import *

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        men_store, created = Store.objects.get_or_create(name='men')
        women_store, created = Store.objects.get_or_create(name='women')
        men_store.save()
        women_store.save()

        stores = ( ('men', men_store), ('women', women_store))
        for store in stores:
            sales = json.loads(GiltActiveSales(store[0]))["sales"]
            for sale in sales:
                try:
                    product_urls = sale['products']
                    for product_url in product_urls:
                        product = json.loads(GiltLookup(product_url))
                        print(json.dumps(product, indent=4))
                        image_urls = product['image_urls']
                        brand = product['brand']
                        material = product['content']['material']
                        image_url = image_urls['300x400'][0]['url']
                        item_url = product['url']
                        description = product['content']['description']
                        name = product['name']
                        sale_price = product['skus'][0]['sale_price']
                        msrp_price = product['skus'][0]['msrp_price']

                        Product.objects.create(material=material, brand=brand, image_url=image_url, store=store[1], item_url=item_url,
                        description=description, name=name,msrp_price=msrp_price, sale_price=sale_price)
                except KeyError as e:
                    print "exception was " + str(e)
                    continue



#description = product['content']['description']



