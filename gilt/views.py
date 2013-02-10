# Create your views here.
from gilt.models import Store, Product

def get_gilt_item(request):
    random_product = Product.objects.order_by('?')[0]


