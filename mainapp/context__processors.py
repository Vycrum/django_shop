from mainapp.models import ProductCategory


def get_categories(request):
    return {'all_categories': ProductCategory.objects.all()}


def get_basket(request):
    basket = []
    quantity = None
    total_price = None

    if request.user.is_authenticated:
        basket = request.user.basket.select_related('product__category').all()
        quantity = sum(list(map(lambda item: item.quantity, basket)))
        total_price = sum(list(map(lambda item: item.cost, basket)))

    return {
        'basket': basket,
        'basket_quantity': quantity,
        'basket_total_price': total_price
    }