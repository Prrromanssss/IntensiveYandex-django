# Generated by Django 3.2.16 on 2022-10-31 19:41

import catalog.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('name', models.CharField(help_text='максимум 150 символов', max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Только slug-значения,\n                             максимум 200 символов', max_length=200, unique=True, verbose_name='Адрес')),
                ('weight', models.PositiveSmallIntegerField(default=100, help_text='Максимум 32767', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Вес')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('name', models.CharField(help_text='максимум 150 символов', max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Только slug-значения,\n                             максимум 200 символов', max_length=200, unique=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('name', models.CharField(help_text='максимум 150 символов', max_length=150, verbose_name='Название')),
                ('text', models.TextField(help_text='Описание должно содержать слова "роскошно" и "превосходно"', validators=[catalog.validators.validate_amazing], verbose_name='Описание')),
                ('category', models.ForeignKey(help_text='Выберите категорию', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='catalog.category', verbose_name='Категория')),
                ('tags', models.ManyToManyField(help_text='Выберите теги', related_name='items', to='catalog.Tag', verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
