from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=255, verbose_name="พาดหัว", null=True, blank=True)
    author = models.CharField(max_length=100, verbose_name="คนเขียน", null=True, blank=True)
    date = models.DateField(verbose_name="วันที่", null=True, blank=True)
    content = models.TextField(verbose_name="เนื้อหา", null=True, blank=True)  # เปลี่ยนกลับไปเป็น TextField
    image = models.ImageField(upload_to='images/', verbose_name="ภาพประกอบ", null=True, blank=True)
    caption = models.CharField(max_length=255, blank=True, null=True, verbose_name="แคปชั่น")
    youtube_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="ลิงก์ YouTube")

    def __str__(self):
        return self.title if self.title else "Untitled"
