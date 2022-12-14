# Generated by Django 3.2.16 on 2022-11-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221130_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='день рождения'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='почта'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='фамилия'),
        ),
    ]
