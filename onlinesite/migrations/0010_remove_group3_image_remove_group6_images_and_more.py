# Generated by Django 4.1.3 on 2023-01-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesite', '0009_group3_group4_group5_group6'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group3',
            name='image',
        ),
        migrations.RemoveField(
            model_name='group6',
            name='images',
        ),
        migrations.AddField(
            model_name='group3',
            name='svg_file',
            field=models.FileField(default=1, upload_to='svgs/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group6',
            name='svg_file',
            field=models.FileField(default=11, upload_to='svgs/'),
            preserve_default=False,
        ),
    ]
