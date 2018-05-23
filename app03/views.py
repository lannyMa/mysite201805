from django.db.models import Avg, Max, Min, Sum, Count
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import F, Q
# Create your views here.
from app03.models import Publish, Author, Book


def addbook(request):
    # 1.创建出版社
    # Publish.objects.create(name="人民出版社",city="北京")
    #
    # p = Publish()
    # p.name = "邮电出版社"
    # p.city = "西安"
    # p.save()
    #
    # p2 = Publish(name="机械出版社")
    # p2.city = "上海"
    # p2.save()
    #
    # print(Publish.objects.all())

    # 2，创建图书
    # Book.objects.create(name="python", price=89,pub_date='2017-01-07', publish_id=1)
    # Book.objects.create(name="go", price=99, pub_date='2017-04-01',publish_id=2)
    # Book.objects.create(name="ios", price=39,pub_date='2017-06-01', publish_id=3)
    # Book.objects.create(name="java", price=69, pub_date='2017-12-24',publish_id=3)

    # 3，创建作者
    # Author.objects.create(name="龟叔",age=17)
    # Author.objects.create(name="林纳斯",age=20)
    # Author.objects.create(name="毛台",age=25)
    # Author.objects.create(name="Jeff",age=33)

    # 龟叔还写了ios
    # book_obj = Book.objects.get(name="ios")
    # author_obj = Author.objects.get(id=1)
    # print(book_obj.author.all()) # ios谁写的?
    # # book_obj.author.add(author_obj)

    # 龟叔出过的书
    # res = Book.objects.filter(author__name="龟叔").values('name', 'price')
    # print(res)
    #
    # # python这本书谁写的
    # res2 = Author.objects.filter(book__name="python")
    # print(res2)
    #
    # Book_Author.objects.create(book_id=2,author_id=1)
    #
    # book_obj = Book.objects.get(id=2)
    # # book_obj.book_author_set.all() # book_author的queryset对象
    # print(book_obj.book_author_set.all()[0].author)
    #
    # Book.objects.filter(book_author__author_id__name="龟叔").values('name','price')
    #
    #
    # # 创建自定义book_author表
    # # Book.objects.filter(book_author__author__name="alex").values("name","price")
    #
    # # 1, python这本书对应的出版社的名字
    # Book.objects.filter(name="python").values('publish__name')
    # Publish.objects.filter(book__name="python").values('name')
    # print('#'*20)
    #
    # # 2, 邮电出版社出版的所有书
    # print(Publish.objects.filter(name="邮电出版社").values('book__name'))
    # print(Book.objects.filter(publish__name="邮电出版社").values('name'))
    # print('#'*20)
    #
    # # 3通author找出他的book: 龟叔写的书找出来
    # print(Book.objects.filter(author__name="龟叔"))
    # print(Author.objects.filter(name="龟叔").values('book__name'))
    #
    # # 4,python这本书的作者
    # print(Book.objects.filter(name="python").values('author__name'))
    # print(Author.objects.filter(book__name="python").values('name'))

    # print(Book.objects.aggregate(Min('price')))
    # print(Book.objects.aggregate(Sum('price')))
    # print(Book.objects.aggregate(Avg('price')))
    #
    # # 龟叔书的价格总和
    # print(Book.objects.filter(author__name="龟叔").aggregate(Sum('price')))
    #
    # # 龟叔出了几本书
    # print(Book.objects.filter(author__name="龟叔").aggregate(Count('name')))
    #
    # print(Book.objects.all().values("author__name").annotate(Sum("price")))
    # # print(Book.objects.values)
    # print(Publish.objects.values('name').annotate(Min("book__price")))

    # # print(Book.objects.get(name="python", price=77))
    #
    # # Book.objects.all().update(price=price+10)
    # Book.objects.all().update(price=F('price') + 10)
    # print(Book.objects.filter(Q(name='go') | Q(price=109)).values('name', 'price'))
    # print(Book.objects.filter(Q(name='go') | ~Q(price=109)).values('name', 'price'))
    # print(Book.objects.filter(Q(name__contains='go')).values('name', 'price'))

    res = Book.objects.filter(price=100)
    if res.exists():
        print('ok')



    # return HttpResponse("结果请查看console")




