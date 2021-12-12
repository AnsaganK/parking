# Generated by Django 4.0 on 2021-12-11 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0002_alter_parkingspace_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parkingspace',
            options={'ordering': ['-pk'], 'verbose_name': 'Парковочное место', 'verbose_name_plural': 'Парковочные места'},
        ),
        migrations.AlterField(
            model_name='reserve',
            name='parking_space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserves', to='app.parkingspace', verbose_name='Парковочное место'),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='reserving_emlpoyee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserves', to='auth.user', verbose_name='Бронирующий сотрудник'),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='reserving_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserves', to='app.reservinguser', verbose_name='Бронирующий пользователь'),
        ),
    ]