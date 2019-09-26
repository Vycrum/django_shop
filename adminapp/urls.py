import adminapp.views as adminapp
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('forbidden/', adminapp.ForbiddenView.as_view(), name='forbidden'),

    path('users/create/', adminapp.UsersCreateView.as_view(), name='user_create'),
    path('users/', adminapp.UsersListView.as_view(), name='users_list'),
    path('users/<int:pk>/', adminapp.UsersDetailView.as_view(), name='users_detail'),
    path('users/update/<int:pk>/', adminapp.UsersUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', adminapp.UsersDeleteView.as_view(), name='user_delete'),

    path('categories/create/', adminapp.CategoryCreateView.as_view(), name='category_create'),
    path('categories/', adminapp.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', adminapp.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/update/<int:pk>/', adminapp.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.CategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/', adminapp.ProductsCreateView.as_view(), name='product_create'),
    path('products/category/<int:pk>/', adminapp.ProductsListView.as_view(), name='products_list'),
    path('products/<int:pk>/', adminapp.ProductsDetailView.as_view(), name='product_detail'),
    path('products/update/<int:pk>/', adminapp.ProductsUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', adminapp.ProductsDeleteView.as_view(), name='product_delete'),

    path('', adminapp.AdminHomeView.as_view(), name='admin_home'),
]