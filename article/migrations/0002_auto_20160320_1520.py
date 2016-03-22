# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='Comments_name',
        ),
        migrations.AlterField(
            model_name='article',
            name='Article_like',
            field=models.IntegerField(default=0, verbose_name=b'like'),
        ),
        migrations.AlterField(
            model_name='article',
            name='Article_text',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='article',
            name='Article_title',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='Comments_text',
            field=models.CharField(max_length=300),
        ),
    ]
