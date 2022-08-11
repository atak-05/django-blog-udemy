# Generated by Django 4.1 on 2022-08-11 11:44

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0002_alter_categorymodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='text_image')),
                ('context', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_author', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(related_name='text', to='blog_app.categorymodel')),
            ],
            options={
                'verbose_name': 'Text',
                'verbose_name_plural': 'Texts',
                'db_table': 'Text',
            },
        ),
    ]
