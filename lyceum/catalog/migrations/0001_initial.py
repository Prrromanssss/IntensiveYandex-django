# Generated by Django 3.2.16 on 2022-11-08 20:19

import catalog.validators
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
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('slug', models.SlugField(help_text='Только slug-значения, максимум 200 символов', max_length=200, unique=True, verbose_name='slug')),
                ('name', models.CharField(help_text='Максимум 150 символов', max_length=150, unique=True, verbose_name='название')),
                ('weight', models.PositiveSmallIntegerField(default=100, help_text='Максимум 32767', verbose_name='вес')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Preview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='previews/%Y/%m/%d', verbose_name='превью товара')),
                ('name', models.CharField(help_text='Максимум 150 символов', max_length=150, unique=True, verbose_name='название')),
            ],
            options={
                'verbose_name': 'превьюха',
                'verbose_name_plural': 'превьюхи',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('slug', models.SlugField(help_text='Только slug-значения, максимум 200 символов', max_length=200, unique=True, verbose_name='slug')),
                ('name', models.CharField(help_text='Максимум 150 символов', max_length=150, unique=True, verbose_name='название')),
            ],
            options={
                'verbose_name': 'тег',
                'verbose_name_plural': 'теги',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('name', models.CharField(help_text='Максимум 150 символов', max_length=150, verbose_name='название')),
                ('text', models.TextField(help_text='Описание должно содержать слова "роскошно" и "превосходно"', validators=[catalog.validators.validate_amazing], verbose_name='описание')),
                ('category', models.ForeignKey(help_text='Выберите категорию', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='catalog.category', verbose_name='категория')),
                ('preview', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='catalog.preview', verbose_name='категория')),
                ('tags', models.ManyToManyField(related_name='items', to='catalog.Tag', verbose_name='тег')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'default_related_name': 'items',
            },
        ),
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='previews/%Y/%m/%d', verbose_name='превью товара')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.item', verbose_name='товар')),
            ],
            options={
                'verbose_name': 'Фото товара',
                'verbose_name_plural': 'Фотогалерея товара',
            },
        ),
    ]
