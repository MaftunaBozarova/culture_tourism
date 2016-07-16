# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 11:16
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('culture_tourism', '0033_maqollar'),
    ]

    operations = [
        migrations.AddField(
            model_name='maqollar',
            name='body_en',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='maqollar',
            name='body_ru',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='maqollar',
            name='body_uz',
            field=redactor.fields.RedactorField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='maqollar',
            name='title_en',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='maqollar',
            name='title_ru',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='maqollar',
            name='title_uz',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
