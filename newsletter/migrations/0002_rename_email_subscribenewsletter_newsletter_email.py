# Generated by Django 3.2 on 2022-11-27 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribenewsletter',
            old_name='email',
            new_name='newsletter_email',
        ),
    ]
