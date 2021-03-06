# Generated by Django 3.2.4 on 2021-09-30 13:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emojiString', models.CharField(max_length=10)),
                ('useruid', models.CharField(max_length=100)),
                ('date_posted', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_string', models.CharField(max_length=100)),
                ('useruid', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2021, 9, 30, 19, 21, 30, 864411))),
            ],
        ),
        migrations.CreateModel(
            name='UsageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useruid', models.CharField(max_length=100)),
                ('usageString', models.TextField()),
                ('date_posted', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='SleepEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_end', models.DateTimeField()),
                ('time_start', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('place', models.CharField(max_length=100)),
                ('amplitude', models.IntegerField()),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('steps', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.userprofile')),
            ],
        ),
    ]
