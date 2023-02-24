# Generated by Django 4.0.6 on 2023-02-19 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resident', '0008_morador_aceite_alertas_morador_condominio_and_more'),
        ('delivery', '0016_morador_alter_delivery_morador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='morador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='resident.morador'),
        ),
        migrations.DeleteModel(
            name='Morador',
        ),
    ]
