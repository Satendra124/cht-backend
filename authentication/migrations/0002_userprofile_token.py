# Generated by Django 3.2.4 on 2021-06-22 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='token',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]
