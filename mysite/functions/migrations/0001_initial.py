# Generated by Django 5.1.2 on 2024-10-16 14:05

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
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="พาดหัว"
                    ),
                ),
                (
                    "author",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="คนเขียน"
                    ),
                ),
                (
                    "date",
                    models.DateField(blank=True, null=True, verbose_name="วันที่"),
                ),
                (
                    "content",
                    models.TextField(blank=True, null=True, verbose_name="เนื้อหา"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        verbose_name="ภาพประกอบ",
                    ),
                ),
                (
                    "image1",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        verbose_name="ภาพประกอบ",
                    ),
                ),
                (
                    "image2",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        verbose_name="ภาพประกอบ",
                    ),
                ),
                (
                    "caption",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="แคปชั่น"
                    ),
                ),
                (
                    "youtube_url",
                    models.URLField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="ลิงก์ YouTube",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("SOC", "สังคมไทบ้าน"),
                            ("ECO", "เศรษฐกิจไทยบ้าน"),
                            ("POL", "การเมืองไทยบ้าน"),
                            ("CUL", "วัฒนธรรมไทบ้าน"),
                            ("REV", "ไทบ้านรีวิว"),
                        ],
                        max_length=3,
                        verbose_name="ประเภท",
                    ),
                ),
            ],
        ),
    ]
