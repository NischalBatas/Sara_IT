# Generated by Django 4.1.6 on 2023-02-14 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesite', '0045_rename_demo_confirm_password_demo_demo_pnumber_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=150)),
                ('f_email', models.EmailField(max_length=254)),
                ('f_messages', models.TextField()),
            ],
        ),
    ]
