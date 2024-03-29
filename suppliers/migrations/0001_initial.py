# Generated by Django 4.2.6 on 2023-10-07 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('debt', models.DecimalField(decimal_places=2, max_digits=21)),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suppliers.link', verbose_name='поставщик')),
            ],
            options={
                'verbose_name': 'звено сети',
                'verbose_name_plural': 'звенья сети',
            },
        ),
    ]
