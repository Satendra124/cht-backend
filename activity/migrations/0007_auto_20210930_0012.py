# Generated by Django 3.2.4 on 2021-09-29 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0006_auto_20210928_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usagedata',
            old_name='timestamp',
            new_name='date_posted',
        ),
        migrations.AlterField(
            model_name='survey',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 30, 0, 12, 33, 300557)),
        ),
    ]