# Generated by Django 4.0 on 2021-12-13 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_reserve_options_alter_reservinguser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingspace',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True, verbose_name='Слаг'),
        ),
    ]
