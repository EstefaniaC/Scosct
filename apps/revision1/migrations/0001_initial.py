# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_auto_20160726_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revision1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(max_length=30, null=True, blank=True)),
                ('observacion_1', models.TextField(max_length=500, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('registro', models.ForeignKey(to='registro.Registro')),
            ],
        ),
    ]
