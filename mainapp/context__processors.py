from django.template import RequestContext
from django.conf import settings
from basketapp.models import Basket
from mainapp.models import ProductCategory


def get_categories(request):
    return {'all_categories': ProductCategory.objects.all()}


def get_basket(request):
    basket = []
    user = request.user
    quantity = None
    total_price = None

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=user)
        quantity = sum(list(map(lambda item: item.quantity, basket)))
        total_price = sum(list(map(lambda item: item.cost, basket)))

    return {
        'basket': basket,
        'basket_quantity': quantity,
        'basket_total_price': total_price
    }