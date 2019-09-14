from django.shortcuts import render
from django.views.generic import ListView, TemplateView
import os

from .models import Product, ProductCategory


# Class-Based Views

class HomePageView(TemplateView):
    template_name = 'mainapp/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView , self).get_context_data(*args, **kwargs)
        user_login = os.getlogin()
        context['user'] = user_login
        return context


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
        context['category'] = ProductCategory.objects.filter(id=category_id)[0]
        context['products'] = Product.objects.filter(category_id=category_id)
        return context


# class BookListView(generic.ListView):
#     model = Book
#     context_object_name = 'my_book_list'  # your own name for the list as a template variable
#     queryset = Book.objects.filter(title__icontains='war')[:5]  # Get 5 books containing the title war
#     template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

# Function-Based Views

# def main(request):
#     user_login = os.getlogin()
#     context = {'user': user_login}
#     return render(request, 'mainapp/index.html', context)


# def products(request):
#     product_items = os.listdir('./templates/mainapp/catalog/')
#     product_items = [(os.path.splitext(item)[0], count+1) for count, item in enumerate(product_items)]
#     context = {'products': product_items}
#     return render(request, 'mainapp/catalog.html', context)


# def contacts(request):
#     return render(request, 'mainapp/contacts.html')
