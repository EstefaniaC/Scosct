# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_remove_registro_numerofolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreRevisor1', models.CharField(max_length=100, null=True, blank=True)),
                ('estado1', models.CharField(max_length=30, null=True, blank=True)),
                ('observacion1', models.TextField(max_length=500, null=True, blank=True)),
                ('nombreRevisor2', models.CharField(max_length=100, null=True, blank=True)),
                ('estado2', models.CharField(max_length=30, null=True, blank=True)),
                ('observacion2', models.TextField(max_length=500, null=True, blank=True)),
                ('nombreRevisor3', models.CharField(max_length=100, null=True, blank=True)),
                ('estado3', models.CharField(max_length=30, null=True, blank=True)),
                ('observacion3', models.TextField(max_length=500, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('registro', models.ForeignKey(to='registro.Registro')),
            ],
        ),
    ]
