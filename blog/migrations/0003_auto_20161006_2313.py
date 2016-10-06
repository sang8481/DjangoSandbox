# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161005_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publicshed_date',
            new_name='published_date',
        ),
    ]
