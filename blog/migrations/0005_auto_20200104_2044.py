# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-04 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151128_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='preview_image',
            field=models.ImageField(upload_to='images/%Y/%m', verbose_name='Картинка превью'),
        ),
    ]