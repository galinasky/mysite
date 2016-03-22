# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20160320_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Article_like',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbd\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb8\xd0\xbb\xd0\xbe\xd1\x81\xd1\x8c'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='Comments_text',
            field=models.CharField(max_length=300, verbose_name=b'\xd0\xba\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9'),
        ),
    ]
