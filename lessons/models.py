from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Class(models.Model):
    name = models.CharField(max_length=15, verbose_name='Номер помещения')
    teacher = models.ManyToManyField(
        User, through='LearningActivity', related_name='rooms'
    )

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'
        ordering = ('id',)
        constraints = (
            models.UniqueConstraint(
                fields=(
                    'name',
                ),
                name='unique_classroom_name',
            ),
        )

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=20, verbose_name='Предмет')
    teacher = models.ManyToManyField(
        User, through='LearningActivity',
        related_name='subjects'
    )

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ('id',)
        constraints = (
            models.UniqueConstraint(
                fields=(
                    'name',
                ),
                name='unique_subject_name',
            ),
        )

    def __str__(self):
        return self.name


class LearningActivity(models.Model):
    teachers = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Преподаватель'
    )
    rooms = models.ForeignKey(
        Class, on_delete=models.CASCADE,
        verbose_name='Помещение'
    )
    subjects = models.ForeignKey(
        Subject, on_delete=models.CASCADE,
        verbose_name='Предмет'
    )

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
        ordering = ('subjects',)
        constraints = (
            models.UniqueConstraint(
                fields=(
                    'subjects',
                    'rooms',
                    'teachers'
                ),
                name='unique_lesson',
            ),
        )

    def __str__(self):
        return (
            f'{self.teachers} '
            f'ведет {self.subjects} '
            f'в кабинетах номер {self.rooms}'
        )
