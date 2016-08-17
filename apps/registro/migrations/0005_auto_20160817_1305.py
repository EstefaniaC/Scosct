# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_registro_oficio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='oficio',
            field=models.FileField(null=True, upload_to=b'oficios', blank=True),
        ),
    ]
