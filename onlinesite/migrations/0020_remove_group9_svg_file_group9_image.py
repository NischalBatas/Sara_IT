# Generated by Django 4.1.3 on 2023-01-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesite', '0019_group9_svg_file_alter_group80_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group9',
            name='svg_file',
        ),
        migrations.AddField(
            model_name='group9',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
