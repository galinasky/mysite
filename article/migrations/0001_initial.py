# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Article_title', models.CharField(max_length=100, verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('Article_text', models.TextField()),
                ('Article_date', models.DateTimeField()),
                ('Article_like', models.IntegerField(default=0, verbose_name=b'\xd0\xbd\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb8\xd1\x82\xd1\x81\xd1\x8f')),
            ],
            options={
                'ordering': ['Article_title', 'Article_date'],
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Comments_text', models.CharField(max_length=200)),
                ('Comments_name', models.CharField(max_length=30)),
                ('Comments_id', models.ForeignKey(to='article.Article')),
            ],
        ),
    ]
