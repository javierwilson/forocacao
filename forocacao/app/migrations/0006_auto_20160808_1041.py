# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_question_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('weight', models.IntegerField()),
            ],
            options={
                'ordering': ['weight'],
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Temas',
            },
        ),
        migrations.AlterField(
            model_name='organization',
            name='type',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[('O', 'Organizador'), ('E', 'Exhibidor'), ('S', 'Speaker')]),
        ),
        migrations.AddField(
            model_name='organization',
            name='topic',
            field=models.ForeignKey(verbose_name='Topic', blank=True, to='app.Topic', null=True),
        ),
    ]
