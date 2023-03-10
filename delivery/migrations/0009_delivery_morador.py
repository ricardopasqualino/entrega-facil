# Generated by Django 4.0.6 on 2023-01-03 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resident', '0004_casa_condominio'),
        ('delivery', '0008_alter_delivery_numero_casa'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='morador',
            field=models.ForeignKey(default=None, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, to='resident.morador'),
        ),
    ]
