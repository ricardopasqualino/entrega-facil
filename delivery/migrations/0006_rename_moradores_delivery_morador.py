# Generated by Django 4.0.6 on 2023-01-03 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_delivery_moradores'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery',
            old_name='moradores',
            new_name='morador',
        ),
    ]
