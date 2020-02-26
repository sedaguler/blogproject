from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.topic_list, name='topic_list'),
    url(r'^publish/$', views.publish, name='publish'),
    url(r'^(?P<topic>[\w|\W]+)/(?P<title>[\w|\W]+)/(?P<user>[\w|\W]+)/$', views.topic_title_user_detail, name='topic_title_user_detail'),
    url(r'^(?P<topic>[\w|\W]+)/(?P<title>[\w|\W]+)/$', views.topic_title_detail, name='topic_title_detail'),
    url(r'^(?P<topic>[\w|\W]+)/$', views.single_topic_list, name='single_topic_list'),
]
