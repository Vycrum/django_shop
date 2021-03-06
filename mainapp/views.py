from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.shortcuts import get_object_or_404
import os

from .models import Product, ProductCategory
from basketapp.models import Basket


# Class-Based Views

class HomePageView(TemplateView):
    template_name = 'mainapp/index.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CategoriesView(ListView):
    model = ProductCategory
    template_name = 'mainapp/catalog.html'
    context_object_name = 'all_categories'


# TODO refactor this class to get queryset using ListView or DetailView methods only.
class CategoryDetailView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'mainapp/category_products.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        category_id = self.kwargs.get('pk')
        user = self.request.user
    #
    #    Basket functions are moved to 'context__processors' to work in global context.
    #
        context['category'] = ProductCategory.objects.filter(id=category_id)[0]
        context['products'] = Product.objects.filter(category_id=category_id)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'mainapp/product.html'

# Function-Based Views

# def main(request):
#     user_login = os.getlogin()
#     context = {'user': user_login}
#     return render(request, 'mainapp/index.html', context)


# def products(request, pk=None):
#     print(pk)
#
#     title = 'Products'
#     links_menu = ProductCategory.objects.all()
#
#     basket = []
#     if request.user.is_authenticated:
#         basket = Basket.objects.filter(user=request.user)
#
#     if pk:
#         if pk == 0:
#             products = Product.objects.all().order_by('price')
#             category = {'name': 'All'}
#         else:
#             category = get_object_or_404(ProductCategory, pk=pk)
#             products = Product.objects.filter(category__pk=pk).order_by('price')
#
#         content = {
#             'title': title,
#             'links_menu': links_menu,
#             'category': category,
#             'products': products,
#         }
#
#         return render(request, 'mainapp/products_list.html', content)
#
#     same_products = Product.objects.all()[3:5]
#
#     content = {
#         'title': title,
#         'links_menu': links_menu,
#         'same_products': same_products
#     }
#
#     return render(request, 'mainapp/products.html', content)


# def contacts(request):
#     return render(request, 'mainapp/contacts.html')
