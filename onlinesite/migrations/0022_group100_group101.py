# Generated by Django 4.0.4 on 2023-01-24 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesite', '0021_alter_group9_quote'),
    ]

    operations = [
        migrations.CreateModel(
            name='group100',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='group101',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_name', models.CharField(max_length=200)),
            ],
        ),
    ]