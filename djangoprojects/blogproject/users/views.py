from django.shortcuts import render
from posts.models import BlogPost
from posts.models import BlogTopic
from posts.models import BlogUser
from django.db.models import Count


def user_list(request):
    all_users = BlogUser.objects.all()
    print("burda0")
    print(all_users)
    return render(request, 'users/users.html', {'listofusers':all_users})

def single_user_posts(request, username):
    print("burda1")
    u = BlogUser.objects.get(username=username)
    tlist = BlogPost.objects.filter(user=u).annotate(tcount=Count('topic')).values('topic')
    single_user_list = BlogPost.objects.filter(user = u, topic__in=tlist).values('topic','user').annotate(tcount=Count('topic'))
    single_usertopic_list = BlogTopic.objects.filter(pk__in=tlist).values('title')
    return render(request, 'users/blogusertitle.html', {'singleuserlist':single_usertopic_list, 'usr':username})

def user_topic_detail(request, username, topic):
    print("burda2")
    print(username)
    print(topic)
    t = BlogTopic.objects.filter(title=topic)
    u = BlogUser.objects.get(username=username)
    blog_detail = BlogPost.objects.filter(topic__in=t, user = u)
    return render(request, 'users/blogpost.html', {'blogdetail':blog_detail})

def user_topic_title_detail(request, topic, title, user):
    print("burda3")
    u = BlogUser.objects.get(username=user)
    t = BlogTopic.objects.get(title=topic)
    blog_detail = BlogPost.objects.filter(topic = t, title=title, user=u)
    return render(request, 'users/blogpost.html', {'blogdetail':blog_detail})