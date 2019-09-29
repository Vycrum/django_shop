from django.contrib import admin
from authapp.models import ShopUser
from basketapp.models import Basket


@admin.register(ShopUser)
class UserAdmin(admin.ModelAdmin):
    list_display = 'username', 'email', 'is_staff', 'is_superuser', 'is_active',
    list_filter = 'is_staff', 'is_active', 'is_superuser',
    search_fields = 'username', 'email',
    # readonly_fields = 'username',
    sortable_by = 'username',


class ShopUserWithBasket(ShopUser):
    class Meta:
        verbose_name = 'User with basket'
        verbose_name_plural = 'Users with basket'
        proxy = True


class BasketInline(admin.TabularInline):
    model = Basket
    extra = 0


@admin.register(ShopUserWithBasket)
class ShopUserWithBasketAdmin(admin.ModelAdmin):
    list_display = 'username', 'email', 'get_basket_quantity', 'get_basket_cost',
    fields = 'username',
    readonly_fields = 'username',
    inlines = BasketInline,
    # sortable_by = 'get_basket_quantity', 'get_basket_cost',

    def get_queryset(self, request):
        return ShopUser.objects.filter(basket__quantity__gt=0).distinct()

    def get_basket_quantity(self, instance):
        basket = instance.basket.all()
        total_quantity = sum(list(map(lambda basket: basket.quantity, basket)))
        return total_quantity

    get_basket_quantity.short_description = 'Items in basket'

    def get_basket_cost(self, instance):
        basket = Basket.objects.filter(user=instance)
        return sum(list(map(lambda basket: basket.cost, basket)))

    get_basket_cost.short_description = 'Total cost'
