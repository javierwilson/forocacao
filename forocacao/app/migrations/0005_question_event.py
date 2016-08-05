# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160804_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='event',
            field=models.ForeignKey(default=4, verbose_name='Evento', to='app.Event'),
            preserve_default=False,
        ),
    ]
