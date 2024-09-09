from django.db import models


# Создавайте свои модели здесь.

class Product(models.Model):
    Name = models.CharField(max_length=50, verbose_name='Наименование продукта')
    Description = models.TextField(max_length=1000, verbose_name='Описание продукта')
    Image = models.ImageField(upload_to='products/')
    Category = models.CharField(max_length=100, verbose_name='Категория')
    Purchase_price = models.CharField(max_length=100, verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата последнего изменения')

    def __str__(self):
        return (f'{self.Name}{self.Description}{self.Category}{self.Purchase_price}'
                f'{self.created_at}{self.updated_at}')

    class Meta:
        pass


class Category(models.Model):
    Name = models.CharField(max_length=50, verbose_name='Наименование')
    Description = models.TextField(max_length=1000, verbose_name='Описание')

    def __str__(self):
        return f'{self.Name}{self.Description}'

    class Meta:
        pass
