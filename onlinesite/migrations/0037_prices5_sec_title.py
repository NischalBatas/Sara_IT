# Generated by Django 4.0.4 on 2023-01-25 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesite', '0036_prices2_buttons_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='prices5',
            name='sec_title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]