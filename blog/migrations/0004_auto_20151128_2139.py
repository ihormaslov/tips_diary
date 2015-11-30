# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151128_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='post',
            name='keywords',
        ),
    ]
