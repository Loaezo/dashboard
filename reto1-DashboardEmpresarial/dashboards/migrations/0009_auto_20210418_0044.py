# Generated by Django 3.1.7 on 2021-04-18 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0008_company_market_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='market_value',
        ),
        migrations.AddField(
            model_name='company',
            name='[2772, 7163, 1902, 9733, 6489, 2912, 2559, 6331, 115, 3648, 9937, 9442, 4444, 700, 208, 1680, 6633, 3451, 5127, 4320, 1072, 6325, 3259, 6368, 1398, 6635, 6581, 2924, 7457, 6870, 7061, 592, 107, 1909, 5380, 5297, 4969, 9103, 8863, 5665, 2980, 6826, 7379, 8870, 4039, 2324, 6185, 3714, 5522, 1995]',
            field=models.CharField(default=1000, max_length=500000, verbose_name='Valores a mercado'),
        ),
    ]
