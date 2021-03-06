# Generated by Django 4.0 on 2021-12-13 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_reserve_time_reserve_time_end_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reserve',
            options={'ordering': ['pk'], 'verbose_name': 'Бронирование', 'verbose_name_plural': 'Бронирование'},
        ),
        migrations.AlterField(
            model_name='reservinguser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта пользователя'),
        ),
        migrations.AlterField(
            model_name='reservinguser',
            name='phone',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Телефон пользователя'),
        ),
    ]
