# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('order', models.FloatField(default=0)),
                ('publicated', models.BooleanField(default=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('keywords', models.CharField(max_length=255, null=True, blank=True)),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='blog.Category', null=True)),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('publicated', models.BooleanField(default=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('viewed', models.IntegerField(default=0)),
                ('content', ckeditor.fields.RichTextField()),
                ('preview_image', models.ImageField(upload_to=b'images/%Y/%m', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430 \u043f\u0440\u0435\u0432\u044c\u044e')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('keywords', models.CharField(max_length=255, null=True, blank=True)),
                ('category', models.ForeignKey(blank=True, to='blog.Category', null=True)),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': '\u0417\u0430\u043f\u0438\u0441\u044c',
                'verbose_name_plural': '\u0417\u0430\u043f\u0438\u0441\u0438',
            },
        ),
    ]
