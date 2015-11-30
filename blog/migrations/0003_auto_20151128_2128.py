# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151128_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 28, 21, 28, 6, 489341, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 28, 21, 28, 39, 742337, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
