from django.db import models

from contacts.models import Contact
from products.models import Product

NULLABLE = {'blank': True, 'null': True}


class Link(models.Model):
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='поставщик', **NULLABLE)
    name = models.CharField(max_length=100, verbose_name='название')
    debt = models.DecimalField(max_digits=21, decimal_places=2, verbose_name='Задолженность перед поставщиком')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    @property
    def products(self):
        return Product.objects.get(pk=self.pk)

    @property
    def contacts(self):
        return Contact.objects.get(pk=self.pk)

    def __str__(self):
        return f'{self.name}, {self.creation_time}'

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'
