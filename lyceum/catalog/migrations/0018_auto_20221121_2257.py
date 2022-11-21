# Generated by Django 3.2.16 on 2022-11-21 22:57

import catalog.validators
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20221121_2253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainimage',
            options={'verbose_name': 'главное изображение', 'verbose_name_plural': 'главные изображения'},
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='previews/%Y/%m/%d', verbose_name='главное изображение товара'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=ckeditor.fields.RichTextField(help_text='Описание должно содержать слова "роскошно" и "превосходно"', validators=[catalog.validators.validate_amazing], verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='mainimage',
            name='image',
            field=models.ImageField(upload_to='previews/%Y/%m/%d', verbose_name='главное изображение товара'),
        ),
    ]