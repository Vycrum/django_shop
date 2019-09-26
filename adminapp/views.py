from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView,  DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect


class AdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def get_test_func(self):
        return self.test_func

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result:
            return redirect('adminapp:forbidden')
        return super().dispatch(request, *args, **kwargs)


class ForbiddenView(TemplateView):
    template_name = 'adminapp/forbidden.html'


class AdminHomeView(LoginRequiredMixin, AdminMixin, TemplateView):
    template_name = 'adminapp/base.html'


# Users Views

class UsersListView(LoginRequiredMixin, AdminMixin, ListView):
    model = ShopUser
    context_object_name = 'users'
    template_name = 'adminapp/users/users_list.html'
    login_url = 'authapp:login'


class UsersDetailView(LoginRequiredMixin, AdminMixin, DetailView):
    model = ShopUser
    context_object_name = 'user'
    template_name = 'adminapp/users/users_detail.html'
    login_url = 'authapp:login'


class UsersCreateView(LoginRequiredMixin, AdminMixin, CreateView):
    model = ShopUser
    fields = '__all__'
    template_name = 'adminapp/users/users_create.html'
    login_url = 'authapp:login'


class UsersUpdateView(LoginRequiredMixin, AdminMixin, UpdateView):
    model = ShopUser
    fields = '__all__'
    context_object_name = 'user'
    template_name = 'adminapp/users/users_edit.html'
    login_url = 'authapp:login'


class UsersDeleteView(LoginRequiredMixin, AdminMixin, DeleteView):
    model = ShopUser
    context_object_name = 'user'
    template_name = 'adminapp/users/users_delete.html'
    success_url = reverse_lazy('superadmin:users_list')
    login_url = 'authapp:login'


# Categories Views

class CategoryListView(LoginRequiredMixin, AdminMixin, ListView):
    model = ProductCategory
    context_object_name = 'categories'
    template_name = 'adminapp/categories/category_list.html'
    login_url = 'authapp:login'


class CategoryDetailView(LoginRequiredMixin, AdminMixin, DetailView):
    model = ProductCategory
    context_object_name = 'category'
    template_name = 'adminapp/categories/category_detail.html'
    login_url = 'authapp:login'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        category_pk = self.kwargs.get('pk')
        context['products'] = Product.objects.filter(category=category_pk)
        return context


class CategoryCreateView(LoginRequiredMixin, AdminMixin, CreateView):
    model = ProductCategory
    fields = '__all__'
    template_name = 'adminapp/categories/category_create.html'
    login_url = 'authapp:login'


class CategoryUpdateView(LoginRequiredMixin, AdminMixin, UpdateView):
    model = ProductCategory
    fields = '__all__'
    context_object_name = 'category'
    template_name = 'adminapp/categories/category_edit.html'
    login_url = 'authapp:login'


class CategoryDeleteView(LoginRequiredMixin, AdminMixin, DeleteView):
    model = ProductCategory
    context_object_name = 'category'
    template_name = 'adminapp/categories/category_delete.html'
    success_url = reverse_lazy('superadmin:category_list')
    login_url = 'authapp:login'


# Products Views

class ProductsListView(LoginRequiredMixin, AdminMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'adminapp/products/products_list.html'
    login_url = 'authapp:login'


class ProductsDetailView(LoginRequiredMixin, AdminMixin, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'adminapp/products/products_detail.html'
    login_url = 'authapp:login'


class ProductsCreateView(LoginRequiredMixin, AdminMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = 'adminapp/products/products_create.html'
    login_url = 'authapp:login'


class ProductsUpdateView(LoginRequiredMixin, AdminMixin, UpdateView):
    model = Product
    fields = '__all__'
    context_object_name = 'product'
    template_name = 'adminapp/products/products_edit.html'
    login_url = 'authapp:login'


class ProductsDeleteView(LoginRequiredMixin, AdminMixin, DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'adminapp/products/products_delete.html'
    login_url = 'authapp:login'

    def get_success_url(self):
        product = Product.objects.filter(id=self.kwargs['pk'])[0]
        category_pk = product.category.pk

        return reverse_lazy('superadmin:category_detail', kwargs={'pk': category_pk})
