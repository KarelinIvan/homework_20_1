from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import catalog_list
from catalog.views import home
from catalog.views import contacts
from catalog.views import catalog_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("catalog_list/", catalog_list, name="catalog_list"),
    path("contacts/", contacts, name="contacts"),
    path("catalog/<int:pk>/", catalog_detail, name="catalog_detail"),
]
