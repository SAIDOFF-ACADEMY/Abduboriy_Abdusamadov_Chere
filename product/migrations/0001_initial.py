# Generated by Django 4.2.13 on 2024-07-10 04:55

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("name_uz", models.CharField(max_length=255, null=True)),
                ("name_ru", models.CharField(max_length=255, null=True)),
                ("content", ckeditor_uploader.fields.RichTextUploadingField()),
                (
                    "content_uz",
                    ckeditor_uploader.fields.RichTextUploadingField(null=True),
                ),
                (
                    "content_ru",
                    ckeditor_uploader.fields.RichTextUploadingField(null=True),
                ),
                ("price", models.BigIntegerField()),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "product",
                "verbose_name_plural": "products",
            },
        ),
        migrations.CreateModel(
            name="FreeProductModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("count", models.IntegerField()),
                ("free_count", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="freeProducts",
                        to="product.productmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "freeProduct",
                "verbose_name_plural": "freeProducts",
            },
        ),
    ]
