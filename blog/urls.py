from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.blog_title, name="blog_title"),
    url('(?P<article_id>\d)/$', views.blog_article, name="blog_detail"),
]
