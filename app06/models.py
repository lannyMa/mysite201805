from django.db import models
from datetime import datetime


# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间", null=True, blank=True)
    image = models.ImageField(upload_to="image/", default="image/default.png", verbose_name="封面图")
