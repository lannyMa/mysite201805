from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="分类")
    nick_name = models.CharField(max_length=20, verbose_name="分类别名")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name="分类")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Post(models.Model):
    title = models.CharField(max_length=40, verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    tag = models.ManyToManyField(Tag, verbose_name="标签")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
