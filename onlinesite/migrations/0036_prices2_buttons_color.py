# Generated by Django 4.0.4 on 2023-01-25 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesite', '0035_alter_prices2_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='prices2',
            name='buttons_color',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]