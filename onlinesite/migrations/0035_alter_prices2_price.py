# Generated by Django 4.0.4 on 2023-01-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesite', '0034_prices1_prices2_prices3_prices4_prices5_prices6'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices2',
            name='price',
            field=models.FloatField(max_length=200),
        ),
    ]
