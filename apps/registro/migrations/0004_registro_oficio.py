# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_remove_registro_numerofolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='oficio',
            field=models.ImageField(default=b'path/to/my/default/image.jpg', upload_to=b'oficios'),
        ),
    ]
