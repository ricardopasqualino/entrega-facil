# Generated by Django 4.0.6 on 2023-02-19 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resident', '0008_morador_aceite_alertas_morador_condominio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morador',
            name='condominio',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='resident.condominio', verbose_name='Nome do condomínio'),
        ),
    ]
