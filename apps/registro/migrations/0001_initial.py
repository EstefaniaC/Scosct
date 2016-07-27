# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreEntrega', models.CharField(max_length=50, null=True, blank=True)),
                ('numeroFolio', models.IntegerField(null=True, blank=True)),
                ('asunto', models.CharField(max_length=50, null=True, blank=True)),
                ('numeroOficio', models.CharField(max_length=50, null=True, blank=True)),
                ('coordinador', models.CharField(max_length=50, null=True, blank=True)),
                ('empresa', models.CharField(max_length=50, null=True, blank=True)),
                ('fechaRecibido', models.DateField()),
                ('modalidad', models.CharField(max_length=50, null=True, blank=True)),
                ('fechaEntrega', models.DateField()),
                ('municipio', models.CharField(max_length=25, null=True, blank=True)),
                ('observacion', models.TextField(default=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
