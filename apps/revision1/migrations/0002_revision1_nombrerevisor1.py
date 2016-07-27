# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revision1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='revision1',
            name='nombreRevisor1',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
