from django.db import models

# Переменная для строк, которые можем не использовать
NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """Отдельный класс для продуктов"""
    factory = models.ForeignKey(
        'suppliers.Link',
        on_delete=models.CASCADE,
        verbose_name='завод',
        **NULLABLE
    )
    name = models.CharField(
        max_length=100,
        verbose_name='название',
        **NULLABLE
    )
    model = models.CharField(max_length=100, verbose_name='модель', **NULLABLE)
    release_date = models.DateField(verbose_name='дата выхода', **NULLABLE)

    def __str__(self):
        return f'{self.name}, {self.model}, {self.release_date}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
