"""mydj006 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from app01 import views
urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'book/add/$',views.add_book),
    re_path('index/', views.index),
    re_path(r'book/$',views.index),
    re_path(r'book/(\d+)/edit/$',views.edit_book),
    re_path(r'book/(\d+)/del/$',views.del_book),

    re_path(r'publish/add/$',views.add_publish),
    re_path(r'publish/$',views.publish),
    re_path(r'publish/(\d+)/edit/$', views.edit_publish),
    re_path(r'publish/(\d+)/del/$', views.del_publish),

    re_path(r'author/add/$',views.add_author),
    re_path(r'author/$',views.author),
    re_path(r'author/(\d+)/edit/$', views.edit_author),
    re_path(r'author/(\d+)/del/$', views.del_author),
]
