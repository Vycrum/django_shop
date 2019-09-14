from django.urls import path
# from .views import main, catalog, contacts
from .views import CategoriesView, HomePageView, ContactsPageView, CategoryDetailView
from django.conf.urls.static import static
from django.conf import settings

# Class-Based URLs

urlpatterns = [
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_products'),
    path('catalog/', CategoriesView.as_view(), name='catalog'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('', HomePageView.as_view(), name='main'),
]


# Function-Based URLs

# urlpatterns = [
#     path('catalog/', products, name='catalog'),
#     path('contacts/', contacts, name='contacts'),
#     path('', main, name='main'),
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)