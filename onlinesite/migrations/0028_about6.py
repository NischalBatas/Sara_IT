# Generated by Django 4.1.3 on 2023-01-24 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesite', '0027_about4_video_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='about6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('dates', models.DateField()),
                ('Editor', models.CharField(max_length=200)),
                ('Comments_count', models.IntegerField()),
                ('images', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
