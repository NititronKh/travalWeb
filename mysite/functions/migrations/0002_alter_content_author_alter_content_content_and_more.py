# Generated by Django 5.0.4 on 2024-09-22 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("functions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="author",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="คนเขียน"
            ),
        ),
        migrations.AlterField(
            model_name="content",
            name="content",
            field=models.TextField(blank=True, null=True, verbose_name="เนื้อหา"),
        ),
        migrations.AlterField(
            model_name="content",
            name="date",
            field=models.DateField(blank=True, null=True, verbose_name="วันที่"),
        ),
        migrations.AlterField(
            model_name="content",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="media/images/",
                verbose_name="ภาพประกอบ",
            ),
        ),
        migrations.AlterField(
            model_name="content",
            name="title",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="พาดหัว"
            ),
        ),
    ]
