from django.template import RequestContext
from django.conf import settings
from basketapp.models import Basket


def test(request):
    return {'test_var': 'vycrum_666'}


def get_basket(request):
    basket = []
    user = request.user

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=user)
        quantity = 0
        total_price = 0

        for item in basket:
            quantity += item.quantity
            total_price += item.cost

        basket = {
            'quantity': quantity,
            'total_price': total_price
        }

    return {'basket': basket}