# Generated by Django 4.1 on 2022-08-25 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='qualification',
            field=models.CharField(choices=[('Specialist_jr', 'Молодой специалист'), ('Occupation_confirmed', 'Cоответствие занимаемой должности'), ('First_category', 'Первая квалификационная категория'), ('High_category', 'Высшая квалификационная категория')], default=None, max_length=20, verbose_name='Квалификация'),
        ),
    ]
