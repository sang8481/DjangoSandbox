# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161006_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailForm',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255, default='sang8481')),
                ('password', models.CharField(max_length=32, default='tkdtnfl8481')),
                ('email_to', models.CharField(max_length=255, default='sang8481@naver.com')),
                ('subject', models.CharField(max_length=255, default='Testing mail')),
                ('message', models.TextField(default='FUCK')),
            ],
        ),
    ]
