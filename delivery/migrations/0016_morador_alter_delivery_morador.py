# Generated by Django 4.0.6 on 2023-02-19 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0015_delivery_morador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Morador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default=None, max_length=200, null=True)),
                ('sobrenome', models.CharField(default=None, max_length=200, null=True)),
                ('telefone', models.CharField(default=None, max_length=40, null=True)),
                ('email', models.CharField(default=None, max_length=200, null=True, verbose_name='E-mail')),
                ('numero_casa', models.CharField(default=None, max_length=4, null=True, verbose_name='Número da casa')),
            ],
        ),
        migrations.AlterField(
            model_name='delivery',
            name='morador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='delivery.morador'),
        ),
    ]
