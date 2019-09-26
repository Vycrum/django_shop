from django.urls import path, include
# from .views import main, catalog, contacts
from .views import CategoriesView, HomePageView, ContactsPageView, CategoryDetailView, ProductDetailView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('catalog/', CategoriesView.as_view(), name='catalog'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('', HomePageView.as_view(), name='main'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)