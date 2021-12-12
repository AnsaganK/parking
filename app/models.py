import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse
from django.template.defaultfilters import safe


class ParkingSpace(models.Model):
    name = models.CharField(max_length=500, verbose_name='Название')
    slug = models.SlugField(max_length=500, unique=True, verbose_name='Слаг')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:parking_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Парковочное место'
        verbose_name_plural = 'Парковочные места'
        ordering = ['-pk']


class ReservingUser(models.Model):
    first_name = models.CharField(max_length=500, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=500, verbose_name='Фамилия пользователя')
    email = models.EmailField(null=True, blank=True, verbose_name='Почта пользователя')
    phone = models.CharField(max_length=500, null=True, blank=True, verbose_name='Телефон пользователя')

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Бронирующий пользователь'
        verbose_name_plural = 'Бронирующие пользователи'


class Reserve(models.Model):
    reserving_user = models.ForeignKey(ReservingUser, on_delete=models.CASCADE, verbose_name='Бронирующий пользователь',
                                       related_name='reserves')
    reserving_emlpoyee = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Бронирующий сотрудник',
                                           related_name='reserves')
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE, verbose_name='Парковочное место',
                                      related_name='reserves')
    time_start = models.DateTimeField(null=True, blank=True)
    time_end = models.DateTimeField(null=True, blank=True)
    unique_id = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return str(self.unique_id)

    @property
    def get_date(self):
        return safe(f'{self.time_start.strftime("%d-%m-%Y %H:%M")}<br>'
                    f'{self.time_end.strftime("%d-%m-%Y %H:%M")}'
                    )

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'
        ordering = ['pk']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    img = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['-pk']


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
