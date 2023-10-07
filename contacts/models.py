from django.db import models

from suppliers.models import Link


class Contact(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, verbose_name='цепь звена')
    email = models.EmailField()
    country = models.TextField(verbose_name='страна')
    city = models.TextField(verbose_name='город')
    street = models.TextField(verbose_name='улица')
    house = models.TextField(verbose_name='дом')

    def __str__(self):
        return f'{self.email}, {self.country}, город {self.city}, улица {self.street}, дом {self.house}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
