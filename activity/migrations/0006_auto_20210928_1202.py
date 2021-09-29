# Generated by Django 3.2.4 on 2021-09-28 06:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0005_alter_survey_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='moods',
            field=models.CharField(default='00000', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sleepevent',
            name='time_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='survey',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 28, 12, 1, 56, 433431)),
        ),
    ]
