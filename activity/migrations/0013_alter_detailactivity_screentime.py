# Generated by Django 3.2.4 on 2021-06-29 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0012_alter_rawactivity_screentime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailactivity',
            name='screenTime',
            field=models.IntegerField(),
        ),
    ]
