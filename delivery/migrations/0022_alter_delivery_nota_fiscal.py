# Generated by Django 4.0.6 on 2023-02-22 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0021_alter_delivery_modulo_alter_delivery_morador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='nota_fiscal',
            field=models.CharField(default=None, max_length=15, verbose_name='Nota Fiscal'),
        ),
    ]
