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
        x = json.dumps(sales[1]['products'][0])
        #x = str(json.dumps(json.loads(GiltActiveSales('men')), indent=4))
        x = x.replace('"', '')
        print 'url is ' + x
        content = GiltLookup(x)
        product = json.loads(content)
        image_urls = product['image_urls']
        brand = product['brand']
        description = product['content']['description']
        material = product['content']['material']
        image_url = image_urls['300x400'][0]['url']
        item_url = product['url']

        print product
        product = Product.objects.create(material=material, brand=brand, image_url=image_url, store=men_store, item_url=item_url)


        """
            material = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    store = models.ForeignKey(Store)

        """


        #return render_to_response('gilt.html', {'name' : product['name'], 'img_url': image_url} )
