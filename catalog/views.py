from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from catalog.models import Product


# Создавайте свои мнения здесь.


class HomePageView(TemplateView):
    template_name = "catalog/home.html"


class ContactsPageView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "image", "category", "purchase_price")
    success_url = reverse_lazy("catalog:catalog_list")

