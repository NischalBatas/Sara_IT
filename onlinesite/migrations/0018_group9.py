# Generated by Django 4.1.3 on 2023-01-23 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesite', '0017_alter_group80_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='group9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('quote', models.TextField(max_length=200)),
            ],
        ),
    ]
