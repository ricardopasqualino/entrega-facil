# Generated by Django 4.0.6 on 2023-02-23 03:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resident', '0015_alter_morador_morador'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0023_alter_delivery_modulo_alter_delivery_morador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='modulo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='delivery.box'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='delivery',
            name='morador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='resident.moradia'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='recebido_por',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
