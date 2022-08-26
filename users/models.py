from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    QUALIFICATION_CHOICES = [
        ('Specialist_jr', 'Молодой специалист'),
        ('Occupation_confirmed', 'Cоответствие занимаемой должности'),
        ('First_category', 'Первая квалификационная категория'),
        ('High_category', 'Высшая квалификационная категория')]
    email = models.EmailField(max_length=50, unique=True)
    qualification = models.CharField(
        max_length=20,
        verbose_name='Квалификация',
        choices=QUALIFICATION_CHOICES,
        default=None,
        blank=True
    )
    fullname = models.CharField(max_length=20, verbose_name='Фамилия, Имя', blank=False)
    is_teacher = models.BooleanField(default=False, verbose_name='Преподаватель')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'fullname']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)
        constraints = (
            models.UniqueConstraint(
                fields=(
                    'email',
                ),
                name='unique_user_email',
            ),
        )

    def __str__(self):
        return self.fullname