from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse
from basketapp.models import Basket
from mainapp.models import Product

@login_required
def basket(request):
    return render(request, 'basketapp/basket.html')


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('product', args=[pk]))

    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    basket_slot = get_object_or_404(Basket, pk=pk)

    if basket_slot:
        if basket_slot.quantity == 1:
            basket_slot.delete()
        else:
            basket_slot.quantity -= 1
            basket_slot.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def edit(request, pk):
    print(pk)
    print(request.GET.get('quantity'))

# @login_required
# def basket_edit(request, pk, quantity):
#     if request.is_ajax():
#         quantity = int(quantity)
#         new_basket_item = Basket.objects.get(pk=int(pk))
#
#         if quantity > 0:
#             new_basket_item.quantity = quantity
#             new_basket_item.save()
#         else:
#             new_basket_item.delete()
#
#         basket_items = Basket.objects.filter(user=request.user). \
#             order_by('product__category')
#
#         content = {
#             'basket_items': basket_items,
#         }
#
#         result = render_to_string('basketapp/includes/inc_basket_list.html', \
#                                   content)
#
#         return JsonResponse({'result': result})
