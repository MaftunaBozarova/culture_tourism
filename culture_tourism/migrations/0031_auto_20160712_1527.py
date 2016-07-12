# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 10:27
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('culture_tourism', '0030_auto_20160712_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='comment',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description_en',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description_ru',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description_uz',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='library',
            name='lib_description',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='library',
            name='lib_description_en',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='library',
            name='lib_description_ru',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='library',
            name='lib_description_uz',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='otherinfo',
            name='description',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='otherinfo',
            name='description_en',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='otherinfo',
            name='description_ru',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='otherinfo',
            name='description_uz',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_text',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_text_en',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_text_ru',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_text_uz',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='regions',
            name='region_description',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='regions',
            name='region_description_en',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='regions',
            name='region_description_ru',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='regions',
            name='region_description_uz',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='subarticle',
            name='body',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='subarticle',
            name='body_en',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='subarticle',
            name='body_ru',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='subarticle',
            name='body_uz',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='description',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='description_en',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='description_ru',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='description_uz',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
    ]
