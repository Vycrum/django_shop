from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,  DeleteView
from django.urls import reverse_lazy


class UsersView(ListView):
    model = ShopUser
    context_object_name = 'users'
    template_name = 'adminapp/users.html'


class UsersDetailView(DetailView):
    model = ShopUser
    context_object_name = 'user'
    template_name = 'adminapp/users_detail.html'


class UsersCreateView(CreateView):
    model = ShopUser
    fields = '__all__'
    template_name = 'adminapp/users_create.html'


class UsersUpdateView(UpdateView):
    model = ShopUser
    fields = '__all__'
    context_object_name = 'user'
    template_name = 'adminapp/users_edit.html'


class UsersDeleteView(DeleteView):
    model = ShopUser
    context_object_name = 'user'
    template_name = 'adminapp/users_delete.html'
    success_url = reverse_lazy('superadmin:users')


def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.all()

    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)


def category_create(request):
    pass


def category_update(request, pk):
    pass


def category_delete(request, pk):
    pass


def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', content)


def product_create(request, pk):
    pass


def product_read(request, pk):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass