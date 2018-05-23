from django.db import models


# Create your models here.
class Publish(models.Model):
    name = models.CharField(max_length=40, verbose_name="出版社")
    city = models.CharField(max_length=40, verbose_name="出版社所在城市")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = verbose_name


class Author(models.Model):
    name = models.CharField(max_length=40, verbose_name="作者")
    age = models.IntegerField(default=17, verbose_name="年龄")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "作者"
        verbose_name_plural = verbose_name


class Book(models.Model):
    name = models.CharField(max_length=40, verbose_name="书名")
    price = models.IntegerField(default=99, verbose_name="价格")
    pub_date = models.DateField(verbose_name="出版时间")
    publish = models.ForeignKey(Publish, on_delete=models.CASCADE, verbose_name="出版社")

    author = models.ManyToManyField(Author, verbose_name="作者")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "图书"
        verbose_name_plural = verbose_name

#
# class Book_Author(models.Model):
#     book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
#     author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
