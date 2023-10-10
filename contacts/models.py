from django.db import models

# Переменная для строк, которые можем не использовать
NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    """Отдельный класс для контактов"""
    link = models.ForeignKey(
        'suppliers.Link',
        on_delete=models.CASCADE,
        verbose_name='цепь звена',
        **NULLABLE
    )
    email = models.EmailField()
    country = models.TextField(verbose_name='страна')
    city = models.TextField(verbose_name='город')
    street = models.TextField(verbose_name='улица')
    house = models.TextField(verbose_name='дом')

    def __str__(self):
        return (f'{self.email}, '
                f'{self.country}, '
                f'город {self.city}, '
                f'улица {self.street}, '
                f'дом {self.house}')

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
