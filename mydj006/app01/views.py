from django.shortcuts import render,HttpResponse,redirect

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

    res = Book.objects.all()
    return render(request,'index.html',{"book_list":res})

def add_book(request):
    p = Publish.objects.all()
    a = Author.objects.all()
    method = request.method
    if method=='POST':
        dataDic = request.POST

        title = dataDic.get('title')
        publishDate = dataDic.get('publishDate')
        price = dataDic.get('price')
        publish_id = dataDic.get('publish_id')
        author_id = dataDic.getlist('author_id')
        print(title,publishDate,price,publish_id,author_id)
        book = Book.objects.create(title=title,publishDate=publishDate,price=price,publish_id=publish_id)
        book.authors.add(*author_id)

        return redirect('/book/')
    else:
        return render(request,'addBook.html',{"publish_list":p,"author_list":a})

def edit_book(request,id):
    p = Publish.objects.all()
    a = Author.objects.all()
    edit_book = Book.objects.filter(nid=id).first()

    method = request.method
    if method == 'POST':
        dataDic = request.POST

        title = dataDic.get('title')
        publishDate = dataDic.get('publishDate')
        price = dataDic.get('price')
        publish_id = dataDic.get('publish_id')
        author_id = dataDic.getlist('author_id')
        print(title, publishDate, price, publish_id, author_id)
        Book.objects.filter(nid=id).update(title=title, publishDate=publishDate, price=price, publish_id=publish_id)
        edit_book.authors.set(author_id) # set的时候传递列表就行了

        return redirect('/book/')
    else:
        return render(request, 'editBook.html', {"publish_list": p, "author_list": a,"edit_book":edit_book})

def del_book(request,id):
    res = Book.objects.filter(nid=id).delete()
    return redirect('/book/')

def publish(request):
    res = Publish.objects.all()
    return render(request, 'publish.html', {"publish_list": res})

def add_publish(request):
    method = request.method
    if method == 'POST':
        dataDic = request.POST
        print(dataDic)
        name = dataDic.get('name')
        city = dataDic.get('city')
        email = dataDic.get('email')
        print(name, city,email)

        ad = Publish.objects.create(name=name,city=city,email=email)
        return redirect('/publish/')
    else:
        return render(request, 'addPublish.html')

def edit_publish(request,id):
    publish = Publish.objects.filter(nid=id).first()
    method = request.method
    if method == 'POST':
        dataDic = request.POST
        name = dataDic.get('name')
        city = dataDic.get('city')
        email = dataDic.get('email')

        Publish.objects.filter(nid=id).update(name=name,city=city,email=email)
        return redirect('/publish/')
    else:
        return render(request, 'editPublish.html', {"publish": publish})

def del_publish(request,id):
    res = Publish.objects.filter(nid=id).delete()
    return redirect('/publish/')

def author(request):
    res = Author.objects.all()
    return render(request, 'author.html', {"author_list": res})

def add_author(request):
    method = request.method
    if method=='POST':
        dataDic = request.POST
        print(dataDic)
        name = dataDic.get('name')
        age = dataDic.get('age')
        birthday = dataDic.get('birthday')
        telephone = dataDic.get('telephone')
        addr = dataDic.get('addr')
        print(name,age,birthday,telephone,addr)

        ad = AuthorDetail.objects.create(birthday=birthday,telephone=telephone,addr=addr)
        a = Author.objects.create(name=name,age=age,authordetail=ad)
        return redirect('/author/')
    else:
        return render(request,'addAuthor.html')

def edit_author(request,id):
    author = Author.objects.filter(nid=id).first()
    method = request.method
    if method == 'POST':
        dataDic = request.POST
        name = dataDic.get('name')
        age = dataDic.get('age')
        birthday = dataDic.get('birthday')
        telephone = dataDic.get('telephone')
        addr = dataDic.get('addr')

        Author.objects.filter(nid=id).update(name=name, age=age)
        ad_id = Author.objects.filter(nid=id).first().authordetail_id
        AuthorDetail.objects.filter(nid=ad_id).update(birthday=birthday, telephone=telephone, addr=addr)
        return redirect('/author/')
    else:
        return render(request, 'editAuthor.html',{"author":author})

def del_author(request,id):
    res = Author.objects.filter(nid=id).delete()
    return redirect('/author/')
