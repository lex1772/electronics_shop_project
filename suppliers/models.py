from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Link(models.Model):
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='поставщик', **NULLABLE)
    name = models.CharField(max_length=100, verbose_name='название')
    debt = models.DecimalField(max_digits=21, decimal_places=2)
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return f'{self.name}, {self.creation_time}'

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'
