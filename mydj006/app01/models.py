from django.db import models

# Create your models here.

class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    # 一对一关联  作者详情表
    authordetail = models.OneToOneField(to="AuthorDetail",to_field='nid',on_delete=models.CASCADE)

class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)

# 出版社
class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

# Book

class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5,decimal_places=2)

    zan = models.IntegerField(default=0)
    cai = models.IntegerField(default=0)


    publish = models.ForeignKey(to="Publish",to_field='nid',on_delete=models.CASCADE)

    authors = models.ManyToManyField(to="Author");

'''
1.列出图书列表、出版社列表、作者列表
2.点击作者，会列出其出版的图书列表
3.点击出版社，会列出旗下图书列表
4.可以创建、修改、删除 图书、作者、出版社
'''

