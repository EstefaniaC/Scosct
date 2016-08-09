# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revision', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='revision',
            name='concluido',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
