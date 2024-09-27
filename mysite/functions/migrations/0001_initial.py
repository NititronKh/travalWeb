# Generated by Django 5.0.4 on 2024-09-22 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Content",
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
                (
                    "title",
                    models.CharField(max_length=255, null=True, verbose_name="พาดหัว"),
                ),
                (
                    "author",
                    models.CharField(max_length=100, null=True, verbose_name="คนเขียน"),
                ),
                ("date", models.DateField(null=True, verbose_name="วันที่")),
                ("content", models.TextField(null=True, verbose_name="เนื้อหา")),
                (
                    "image",
                    models.ImageField(
                        null=True, upload_to="media/images/", verbose_name="ภาพประกอบ"
                    ),
                ),
                (
                    "caption",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="แคปชั่น"
                    ),
                ),
            ],
        ),
    ]
