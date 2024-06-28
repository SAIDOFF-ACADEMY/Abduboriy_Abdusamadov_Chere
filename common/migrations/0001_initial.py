# Generated by Django 4.2.13 on 2024-06-28 10:14

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPhotoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='gallery/2024/6/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('content_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
            },
        ),
        migrations.CreateModel(
            name='SettingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact_telegram', models.CharField(max_length=255)),
                ('contact_phone', models.CharField(blank=True, max_length=13, null=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('location_text', models.CharField(max_length=255)),
                ('location_text_uz', models.CharField(max_length=255, null=True)),
                ('location_text_ru', models.CharField(max_length=255, null=True)),
                ('working_hours_start', models.TimeField()),
                ('working_hours_end', models.TimeField()),
                ('telegram_bot', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'setting',
                'verbose_name_plural': 'settings',
            },
        ),
    ]
