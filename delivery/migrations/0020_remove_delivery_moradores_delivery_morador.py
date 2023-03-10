# Generated by Django 4.0.6 on 2023-02-19 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resident', '0010_alter_morador_condominio'),
        ('delivery', '0019_alter_delivery_moradores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='moradores',
        ),
        migrations.AddField(
            model_name='delivery',
            name='morador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='resident.morador'),
            preserve_default=False,
        ),
    ]
