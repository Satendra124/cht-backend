# Generated by Django 3.2.4 on 2021-06-17 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_index_locations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Locations',
            new_name='Location',
        ),
    ]
