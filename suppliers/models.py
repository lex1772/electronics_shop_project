from django.db import models

from contacts.models import Contact
from products.models import Product

# Переменная для строк, которые можем не использовать
NULLABLE = {'blank': True, 'null': True}


class Link(models.Model):
    """Класс для звена сети"""
    supplier = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        verbose_name='поставщик', **NULLABLE
    )
    name = models.CharField(
        max_length=100, verbose_name='название звена'
    )
    debt = models.DecimalField(
        max_digits=21, decimal_places=2,
        verbose_name='Задолженность перед поставщиком',
        **NULLABLE
    )
    creation_time = models.DateTimeField(
        auto_now_add=True, verbose_name='время создания'
    )

    @property
    def products(self):
        """Функция для получения списка продуктов текущего звена сети"""
        if len(Product.objects.filter(factory_id=self.pk)) > 0:
            length = len(Product.objects.filter(factory_id=self.pk))
            return Product.objects.filter(factory_id=self.pk)[length - 1]
        else:
            return None

    @property
    def contacts(self):
        """Функция для получения списка контактов текущего звена сети"""
        if len(Contact.objects.filter(link=self.pk)) > 0:
            length = len(Contact.objects.filter(link=self.pk))
            return Contact.objects.filter(link=self.pk)[length - 1]
        else:
            return None

    @contacts.setter
    def contacts(self, value):
        """Функция для добавления или
        изменения контактов текущего звена сети"""
        if value['email'] is None:
            pass
        else:
            length = len(Contact.objects.filter(link=self))
            if length > 0:
                contact_id = (
                    Contact.objects.filter(link=self)
                    .values())[length - 1]['id']
                Contact.objects.filter(pk=contact_id).update(**value)
            else:
                Contact.objects.create(link=self, **value)

    @products.setter
    def products(self, value):
        """Функция для добавления или
        изменения продуктов текущего звена сети"""
        if value['name'] is None:
            pass
        else:
            length = len(Product.objects.filter(factory=self))
            if length > 0:
                product_id = (
                    Contact.objects.filter(factory=self)
                    .values())[length - 1]['id']
                Product.objects.filter(pk=product_id).update(**value)
            else:
                Product.objects.create(factory=self, **value)

    def __str__(self):
        return f'{self.name}, {self.creation_time}'

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'
