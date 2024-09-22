from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home
from catalog.views import contacts
from catalog.views import products_list

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product_list/", products_list, name="product_list"),
]
