# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-27 21:06
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('culture_tourism', '0002_auto_20160816_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='comment',
            field=ckeditor.fields.RichTextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='library',
            name='lib_description',
            field=ckeditor.fields.RichTextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='library',
            name='lib_description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='library',
            name='lib_description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='library',
            name='lib_description_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='maqollar',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='Maqol'),
        ),
        migrations.AlterField(
            model_name='maqollar',
            name='body_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Maqol'),
        ),
        migrations.AlterField(
            model_name='maqollar',
            name='body_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Maqol'),
        ),
        migrations.AlterField(
            model_name='maqollar',
            name='body_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Maqol'),
        ),
        migrations.AlterField(
            model_name='mostvisited',
            name='body',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='mostvisited',
            name='body_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='mostvisited',
            name='body_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='mostvisited',
            name='body_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='otherinfo',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='otherinfo',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='otherinfo',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='otherinfo',
            name='description_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='regions',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='regions',
            name='body_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='regions',
            name='body_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='regions',
            name='body_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='description_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
    ]
