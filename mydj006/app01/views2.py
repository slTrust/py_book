from django.shortcuts import render,HttpResponse

# Create your views here.
from app01.models import Book,Author,AuthorDetail,Publish

def index(request):
    # 插入记录
    # 作者详情  对应作者  ad(n)<--> a(n)
    # ad1 = AuthorDetail.objects.create(birthday='2000-01-01',telephone=110,addr='北京')
    # ad2 = AuthorDetail.objects.create(birthday='1990-01-01', telephone=110, addr='湖北')
    # ad3 = AuthorDetail.objects.create(birthday='2010-01-01', telephone=110, addr='成都')
    # ad4 = AuthorDetail.objects.create(birthday='1992-01-01', telephone=110, addr='天津')
    #
    # # 作者
    # a1 = Author.objects.create(name='alex', age=18, authordetail_id=1)
    # a2 = Author.objects.create(name='tom', age=28, authordetail_id=2)
    # a3 = Author.objects.create(name='hs', age=18, authordetail_id=3)
    # a4 = Author.objects.create(name='hjx',age=26,authordetail_id=4)
    #
    # # 出版社
    # p1 = Publish.objects.create(name='图灵出版社',city='北京',email='10000@qq.com')
    # p2 = Publish.objects.create(name='人民出版社', city='天津', email='20000@qq.com')
    #
    # book记录
    # b1 = Book.objects.create(title='金瓶梅',price=99,publishDate='2015-01-01',publish_id=2)
    # b2 = Book.objects.create(title='西游记', price=199, publishDate='2015-01-01', publish_id=2)
    # b3 = Book.objects.create(title='红楼梦', price=269, publishDate='2015-01-01', publish_id=2)
    # b4 = Book.objects.create(title='三国演义', price=59, publishDate='2015-01-01', publish_id=2)
    # b5 = Book.objects.create(title='python', price=99, publishDate='2015-01-01', publish_id=1)
    # b6 = Book.objects.create(title='javascript', price=115, publishDate='2015-01-01', publish_id=1)
    # b7 = Book.objects.create(title='php', price=79, publishDate='2015-01-01', publish_id=1)
    # b8 = Book.objects.create(title='mysql', price=129, publishDate='2015-01-01', publish_id=1)
    #
    # 书籍作者关系表
    # a1 = Author.objects.filter(name='alex').first()
    # a2 = Author.objects.filter(name='tom').first()
    # a3 = Author.objects.filter(name='hs').first()
    # a4 = Author.objects.filter(name='hjx').first()
    #
    # b1 = Book.objects.filter(title='金瓶梅').first()
    # b1.authors.add(a1,a2)
    #
    # b2 = Book.objects.filter(title='西游记').first()
    # b2.authors.add(a1)
    #
    # b3 = Book.objects.filter(title='红楼梦').first()
    # b3.authors.add(a3)
    #
    # b4 = Book.objects.filter(title='三国演义').first()
    # b4.authors.add(a2)
    #
    # b5 = Book.objects.filter(title='python').first()
    # b5.authors.add(a4)
    #
    # b6 = Book.objects.filter(title='javascript').first()
    # b6.authors.add(a4)
    #
    # b7 = Book.objects.filter(title='php').first()
    # b7.authors.add(a1)
    #
    # b8 = Book.objects.filter(title='mysql').first()
    # b8.authors.add(a4)

    # 跨表查询

    # # 基于对象——子查询
    # # 一对多  正   金瓶梅对应的出版社信息
    # b1 = Book.objects.filter(title='金瓶梅').first()
    # name = b1.publish.name;
    # print(name)
    #
    # # 一对多  反   图灵出版社出版的书籍
    # p1 = Publish.objects.filter(name='图灵出版社').first()
    # res = p1.book_set.all();
    # for i in res:
    #     print(i.title)
    # print('many to many---------')
    # # 多对多  正   金瓶梅对应的作者信息
    # b1 = Book.objects.filter(title='金瓶梅').first()
    # a_list = b1.authors.all();
    # for a in a_list:
    #     print(a.name)
    #
    # # 多对多  反   alex作者对应的图书信息
    # a1 = Author.objects.filter(name='alex').first()
    # res2 = a1.book_set.all()
    # for book in res2:
    #     print(book.title)
    #
    # print('one to one-----------')
    #
    # #正向 alex的手机号
    # a1 = Author.objects.filter(name='alex').first()
    # tel = a1.authordetail.telephone
    # print(tel)
    # # 反向 addr是 天津的作者名称
    # ad = AuthorDetail.objects.filter(addr='天津').first()
    # aname = ad.author.name
    # print(aname)


    # join查询
    # 一对多正向  查金瓶梅对应的出版社
    res = Book.objects.filter(title='金瓶梅').values('publish__name')
    print(res)

    # 一对多反向  查金瓶梅对应的出版社名字
    res2 = Publish.objects.filter(book__title='金瓶梅').values('name')
    print(res2)

    # 多对多正向  查金瓶梅对应的作者
    res3 = Book.objects.filter(title='金瓶梅').values('authors__name')
    print(res3)

    # 多对多反向  查金瓶梅对应的作者
    res4 = Author.objects.filter(book__title='金瓶梅').values('name')
    print(res4)

    # 一对一正向  查询alex地址
    res5 = Author.objects.filter(name='alex').values('authordetail__addr')
    print(res5)

    # 一对一反向  查询alex地址
    res6 = AuthorDetail.objects.filter(author__name='alex').values('addr')
    print(res6)


    return render(request,'index.html')


def query(request):
    # 练习: 手机号以110开头的作者出版过的所有书籍名称以及书籍出版社名称
    res = Book.objects.filter(authors__authordetail__telephone__startswith="110").values('title','publish__name','authors__name')


    from django.db.models import  Avg,Count,Min,Max
    ## 示例1 查询每一个出版社的名称以及出版的书籍个数



    res2 = Publish.objects.values('nid').annotate(c=Count("book__title")).values("name","c")
    # print(res2)


    ## 示例2 查询每一个作者的名字以及出版过的书籍的最高价格
    res3 = Author.objects.values("pk").annotate(max_price=Max("book__price")).values("name","max_price")
    # print(res3)
    # 总结 跨表的分组查询的模型:
    # 每一个后表模型.objects.values("pk").annotate(聚合函数(关联表__统计字段))

    # 示例3 查询每一个书籍的名称以及对应的作者个数
    res4 = Book.objects.values("pk").annotate(c=Count("authors__name")).values("title","c")
    # print(res4)

    #################### 跨表分组查询的另一种玩法  ####################

    # 示例1 查询每一个出版社的名称以及出版的书籍个数
    res5 = Publish.objects.values('pk').annotate(c=Count('book__title')).values('name','c')
    # print(res5)
    ##################### 练习   ####################

    # 统计每一本以py开头的书籍的作者个数：
    res6 = Book.objects.filter(title__startswith='金').values('pk').annotate(c=Count('authors__name')).values("title","c")
    # print(res6)

    # 每一个后的表模型.objects.values("pk").annotate(聚合函数(关联表__统计字段)).values("表模型的所有字段以及统计字段")
    # 统计不止一个作者的图书

    res7 = Book.objects.values('pk').annotate(c=Count('authors__name')).filter(c__gt=1).values("title","c")
    # print(res7)


    # f q查询
    from django.db.models import F

    res8 = Book.objects.filter(zan__gt=F('cai'))

    res9 = Book.objects.filter(zan__gt=F('cai') * 2)
    print(res9)
    for i in res9:
        print(i.title)
    Book.objects.all().update(price=F("price") + 30)
    print(Book.objects.all())
    return HttpResponse('ok')
