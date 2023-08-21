from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    product_image = models.ImageField(upload_to='catalog/', verbose_name='изображение товара', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    purchase_price = models.IntegerField(verbose_name='цена за покупку')
    date_creation = models.DateTimeField(**NULLABLE, verbose_name='дата создания')
    last_modified_date = models.DateTimeField(**NULLABLE, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('title',)
