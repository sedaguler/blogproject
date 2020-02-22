from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^$', views.user_list, name='user_list'),
    url(r'^(?P<username>[\w|\W]+)/(?P<topic>[\w|\W]+)/(?P<title>[\w|\W]+)/$', views.user_topic_title_detail, name='user_topic_title_detail'),
    url(r'^(?P<username>[\w|\W]+)/(?P<topic>[\w|\W]+)/$', views.user_topic_detail, name='user_topic_detail'),
    url(r'^(?P<username>[\w|\W]+)/$', views.single_user_posts, name='single_user_posts'),
]
