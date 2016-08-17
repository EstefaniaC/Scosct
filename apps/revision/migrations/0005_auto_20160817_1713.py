# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revision', '0004_auto_20160817_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revision',
            name='oficioConcluido',
            field=models.FileField(null=True, upload_to=b'oficiosConcluidos', blank=True),
        ),
    ]
