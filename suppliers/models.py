from django.db import models

from contacts.models import Contact
from products.models import Product

NULLABLE = {'blank': True, 'null': True}


class Link(models.Model):
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='поставщик', **NULLABLE)
    name = models.CharField(max_length=100, verbose_name='название звена')
    debt = models.DecimalField(max_digits=21, decimal_places=2, verbose_name='Задолженность перед поставщиком')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    @property
    def products(self):
        if len(Product.objects.filter(factory_id=self.pk)) > 0:
            length = len(Product.objects.filter(factory_id=self.pk))
            return Product.objects.filter(factory_id=self.pk)[length-1]
        else:
            return None

    @property
    def contacts(self):
        return Contact.objects.get(link=self.pk)

    @contacts.setter
    def contacts(self, value):
        if Contact.objects.filter(link=self.pk):
            Contact.objects.filter(link=self.pk).update(**value)
        else:
            Contact.objects.create(link=self.pk, **value)

    @products.setter
    def products(self, value):
        length = len(Product.objects.filter(factory_id=self.pk))
        if length > 0:
            Product.objects.filter(factory_id=self.pk)[length-1].update(**value)
        else:
            Product.objects.create(factory_id=self.pk, **value)

    def __str__(self):
        return f'{self.name}, {self.creation_time}'

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'
