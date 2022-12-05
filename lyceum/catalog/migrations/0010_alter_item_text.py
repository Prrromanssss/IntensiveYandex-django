# Generated by Django 3.2.16 on 2022-12-05 19:54

import catalog.validators
import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20221205_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=ckeditor.fields.RichTextField(help_text='Описание должно содержать слова "роскошно" и "превосходно"', validators=[catalog.validators.validate_amazing], verbose_name='описание'),
        ),
    ]
