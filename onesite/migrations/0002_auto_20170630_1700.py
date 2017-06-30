# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onesite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onesitedemo',
            name='onesitedemo_date',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'),
            preserve_default=True,
        ),
    ]
