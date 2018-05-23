from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app02.models import Publish, Author, Book


def addbook(reuqest):
    Book.objects.create(name="流畅的python", price=89, pub_date="2017-06-06", publish_id=3)
    return HttpResponse("添加图书成功")


def addbook2(reuqest):
    publish_obj = Publish.objects.filter(name="人民出版社")[0]
    Book.objects.create(name="go action", price=22, pub_date="2018-04-04", publish=publish_obj)
    return HttpResponse("添加图书成功(addbook2)")


def home(request):
    book_obj = Book.objects.get(name__contains="go")
    print(book_obj.name)
    print(book_obj.price)
    print(book_obj.pub_date)
    print(book_obj.publish)  # 是一个publish对象,print调用其类的def __str__,所以是name,本质是一条publish记录
    print(book_obj.publish.name)  # 人民出版社
    print(book_obj.publish.city)  # 北京
    print(type(book_obj.publish))  # <class 'app02.models.Publish'>
    # 方法1:
    # select name, price from Book where publish="人民出版社", 这里思维要留意,Book里并无出版社名字的字段.
    pub_obj = Publish.objects.get(name="人民出版社")
    res = Book.objects.filter(publish=pub_obj).values('name', 'price')
    print("1,通过sql查询: ", res)
    print("-" * 50)

    # 方法2: book_set方法
    pub_obj = Publish.objects.filter(name="人民出版社")[0]
    print(pub_obj.book_set.all())
    print("2,通过django内置的book_set方法查询: ", type(pub_obj.book_set.all()))
    print("-" * 50)

    # 方法3: 1,先连 2,后取字段
    res = Book.objects.filter(publish__name="人民出版社").values('name', 'price')  # 这里的publish是外键名
    print("3,通过__方法查找结果: ", res)
    print("-" * 50)

    # python这本书的出版社名字
    # 表名
    print(Publish.objects.filter(book__name="python").values('name'))  # 这里的book是表名, 这里name是publish表里的字段name

    # 逆向查询
    res = Book.objects.filter(name="python").values("publish__name")
    print(res)

    # 在北京出版社出版的书
    Book.objects.filter(publish__city="北京").values('name')

    # 2017年上半年出的书
    res = Book.objects.filter(pub_date__lt="2017-07-01", pub_date__gt="2017-01-01").values('name', 'price')

    # 多对多的关系, id=3的所有作者信息
    book_obj = Book.objects.get(id=3)
    book_obj.author.all()
    print(type(book_obj.author.all()))

    return HttpResponse("查询完毕, 结果请查看console")



# 1. 通过book查publish消息?
# 2. 查看人民出版社出版过哪些书?
def home2(request):
    pass
