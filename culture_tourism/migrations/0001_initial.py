# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-15 12:28
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='gallery/')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='GeneralInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.SlugField(blank=True, max_length=150)),
                ('author', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lib_name', models.CharField(blank=True, max_length=255)),
                ('lib_name_en', models.CharField(blank=True, max_length=255, null=True)),
                ('lib_name_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('lib_name_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('lib_photo', models.ImageField(blank=True, upload_to='library/')),
                ('lib_file', models.FileField(blank=True, upload_to='library/')),
                ('lib_description', ckeditor.fields.RichTextField(verbose_name='Text')),
                ('lib_description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('lib_description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('lib_description_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('lib_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-lib_created'],
            },
        ),
        migrations.CreateModel(
            name='MainArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_tild', models.CharField(max_length=200, unique=True)),
                ('b_tild_en', models.CharField(max_length=200, null=True, unique=True)),
                ('b_tild_ru', models.CharField(max_length=200, null=True, unique=True)),
                ('b_tild_uz', models.CharField(max_length=200, null=True, unique=True)),
                ('b_box', models.CharField(blank=True, max_length=200, null=True)),
                ('b_box_en', models.CharField(blank=True, max_length=200, null=True)),
                ('b_box_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('b_box_uz', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maqollar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=512)),
                ('title_en', models.CharField(blank=True, max_length=512, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=512, null=True)),
                ('title_uz', models.CharField(blank=True, max_length=512, null=True)),
                ('body', ckeditor.fields.RichTextField(verbose_name='Maqol')),
                ('body_en', ckeditor.fields.RichTextField(null=True, verbose_name='Maqol')),
                ('body_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Maqol')),
                ('body_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Maqol')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Menyu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('name_en', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ru', models.CharField(max_length=100, null=True, unique=True)),
                ('name_uz', models.CharField(max_length=100, null=True, unique=True)),
                ('url', models.CharField(blank=True, max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='MostVisited',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_ru', models.CharField(max_length=200, null=True)),
                ('title_uz', models.CharField(max_length=200, null=True)),
                ('photo', models.ImageField(null=True, upload_to='most-visited/')),
                ('body', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('body_en', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('body_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('body_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('n_slug', models.SlugField(blank=True, max_length=250)),
                ('r_slug', models.SlugField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(blank=True, db_index=True, max_length=200)),
                ('news_title_en', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('news_title_ru', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('news_title_uz', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('news_photo', models.ImageField(blank=True, upload_to='news/')),
                ('news_body', ckeditor.fields.RichTextField(verbose_name='News')),
                ('news_body_en', ckeditor.fields.RichTextField(null=True, verbose_name='News')),
                ('news_body_ru', ckeditor.fields.RichTextField(null=True, verbose_name='News')),
                ('news_body_uz', ckeditor.fields.RichTextField(null=True, verbose_name='News')),
                ('news_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=250)),
            ],
            options={
                'ordering': ('-news_created',),
            },
        ),
        migrations.CreateModel(
            name='OtherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Text')),
                ('description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('description_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('promo_photo', models.ImageField(upload_to='')),
                ('address', models.CharField(blank=True, max_length=255)),
                ('address_en', models.CharField(blank=True, max_length=255, null=True)),
                ('address_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('address_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_1', models.CharField(blank=True, max_length=17)),
                ('phone_2', models.CharField(blank=True, max_length=17)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('title_en', models.CharField(max_length=70, null=True)),
                ('title_ru', models.CharField(max_length=70, null=True)),
                ('title_uz', models.CharField(max_length=70, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='regions/')),
                ('body', ckeditor.fields.RichTextField(verbose_name='Text')),
                ('body_en', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('body_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('body_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('title_en', models.TextField(blank=True, null=True)),
                ('title_ru', models.TextField(blank=True, null=True)),
                ('title_uz', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='slide/')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Text')),
                ('description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('description_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('title_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('body', ckeditor.fields.RichTextField(verbose_name='Text')),
                ('body_en', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('body_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('body_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='main_article/')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='main_article/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Tale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='tales/')),
                ('author', models.CharField(blank=True, max_length=100)),
                ('tale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tales', to='culture_tourism.SubArticle')),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200, null=True)),
                ('name_ru', models.CharField(max_length=200, null=True)),
                ('name_uz', models.CharField(max_length=200, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='writers/')),
                ('period', models.CharField(blank=True, max_length=50)),
                ('description', ckeditor.fields.RichTextField(verbose_name='Text')),
                ('description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
                ('description_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Text')),
            ],
        ),
        migrations.AddField(
            model_name='mostvisited',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='most_visiteds', to='culture_tourism.Regions'),
        ),
        migrations.AddField(
            model_name='mainarticle',
            name='subarticle',
            field=models.ManyToManyField(related_name='mainarticle', to='culture_tourism.SubArticle'),
        ),
        migrations.AddField(
            model_name='generalinfo',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='general_menus', to='culture_tourism.Menyu'),
        ),
        migrations.AddField(
            model_name='generalinfo',
            name='subarticle',
            field=models.ManyToManyField(related_name='generalinfo', to='culture_tourism.SubArticle'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='culture_tourism.Menyu'),
        ),
    ]
