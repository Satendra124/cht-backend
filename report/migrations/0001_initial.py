# Generated by Django 3.2.4 on 2021-09-30 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityIndexDiscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greaterThan', models.FloatField()),
                ('lessThan', models.FloatField()),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('minHours', models.FloatField()),
                ('maxHours', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.index')),
            ],
        ),
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greaterThan', models.FloatField()),
                ('lessThan', models.FloatField()),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('description', models.CharField(max_length=200)),
                ('imageUrl', models.CharField(max_length=200)),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.index')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.location')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDay', models.DateTimeField()),
                ('score', models.FloatField()),
                ('steps', models.IntegerField()),
                ('screenTime', models.IntegerField()),
                ('sleepTime', models.IntegerField()),
                ('indexHours', models.TextField()),
                ('activityIndexDiscriptions', models.ManyToManyField(blank=True, to='report.ActivityIndexDiscriptions')),
                ('suggestions', models.ManyToManyField(blank=True, to='report.Suggestions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='activityindexdiscriptions',
            name='index',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.index'),
        ),
    ]
