# Generated by Django 4.1 on 2022-08-12 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_contactmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmodel',
            old_name='title_lastname',
            new_name='name_lastname',
        ),
    ]
