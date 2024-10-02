from django.views.generic import ListView, DetailView, TemplateView

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
