# Generated by Django 4.2.6 on 2023-10-09 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='debt',
            field=models.DecimalField(decimal_places=2, max_digits=21, verbose_name='Задолженность перед поставщиком'),
        ),
    ]
