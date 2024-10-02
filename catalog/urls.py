from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsPageView, HomePageView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="catalog_list"),
    path("home/", HomePageView.as_view(), name="home"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="catalog_detail"),
    path("catalog/create/", ProductCreateView.as_view(), name="product_create"),
]
