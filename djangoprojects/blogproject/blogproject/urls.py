from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from blogproject import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls')),
    url(r'^publish/', views.publish),
    url(r'^users/', include('users.urls')),
    url(r'^$', views.home),
]

urlpatterns += staticfiles_urlpatterns()