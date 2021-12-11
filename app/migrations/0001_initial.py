# Generated by Django 4.0 on 2021-12-11 19:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Название')),
                ('slug', models.SlugField(max_length=500, verbose_name='Слаг')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Парковочное место',
                'verbose_name_plural': 'Парковочные места',
            },
        ),
        migrations.CreateModel(
            name='ReservingUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(max_length=500, verbose_name='Фамилия пользователя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта пользователя')),
                ('phone', models.CharField(max_length=500, verbose_name='Почта пользователя')),
            ],
            options={
                'verbose_name': 'Бронирующий пользователь',
                'verbose_name_plural': 'Бронирующие пользователи',
            },
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('unique_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('parking_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.parkingspace', verbose_name='Парковочное место')),
                ('reserving_emlpoyee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Бронирующий сотрудник')),
                ('reserving_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.reservinguser', verbose_name='Бронирующий пользователь')),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирование',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='auth.user')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'ordering': ['-pk'],
            },
        ),
    ]
