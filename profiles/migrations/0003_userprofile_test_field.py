# Generated by Django 3.2 on 2022-11-26 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_subscribe_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='test_field',
            field=models.BooleanField(default=True),
        ),
    ]
