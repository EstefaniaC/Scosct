# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revision', '0003_revision_oficioconcluido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revision',
            name='oficioConcluido',
            field=models.FileField(default=b'path/to/my/default/image.jpg', upload_to=b'oficiosConcluidos'),
        ),
    ]
