# Generated by Django 4.0 on 2021-12-11 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_parkingspace_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserve',
            name='time',
        ),
        migrations.AddField(
            model_name='reserve',
            name='time_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reserve',
            name='time_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
