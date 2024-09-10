from django.contrib import admin

from catalog.models import Product, Category


# Зарегистрируйте свои модели здесь.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "Purchase_price", "Category")
    list_filter = ("Category",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
