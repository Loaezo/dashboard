# Generated by Django 3.1.7 on 2021-04-16 06:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('company_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.CharField(max_length=100, verbose_name='Descripción')),
                ('stock_volume', models.CharField(max_length=50, verbose_name='Acciones en circulación')),
                ('stock_price', models.CharField(max_length=50, verbose_name='Precio por acción')),
            ],
        ),
        migrations.CreateModel(
            name='market_cap',
            fields=[
                ('market_cap_id', models.IntegerField(primary_key=True, serialize=False)),
                ('year', models.DateField()),
                ('mkt_value', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
