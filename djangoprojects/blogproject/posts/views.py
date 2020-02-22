from django.shortcuts import render
from .models import BlogPost
from .models import BlogTopic
from .models import BlogUser
from django.db.models import Count


def topic_list(request):
    all_topics = BlogTopic.objects.filter(pk__in=BlogPost.objects.values('topic').annotate(count=Count('topic')).values('topic')).annotate(tcount=Count('title')).values('title')
    return render(request, 'posts/topics.html', {'listoftopics':all_topics})

def single_topic_list(request, topic):
    print("burda1")
    print(topic)
    single_topic_list = BlogPost.objects.filter(topic = BlogTopic.objects.get(title=topic)).annotate(tcount=Count('title')).values('topic','title').annotate(count=Count('topic')).values('topic','title')
    return render(request, 'posts/blogtopictitle.html', {'singletopiclist':single_topic_list, 'tpc':topic})

def topic_title_detail(request, topic, title):
    print("burda2")
    print(topic)
    print(title)
    t = BlogTopic.objects.get(title=topic)
    topic_detail = BlogPost.objects.filter(topic = t, title=title)
    return render(request, 'posts/blogpost.html', {'topicdetail':topic_detail})

def topic_title_user_detail(request, topic, title, user):
    print("burda3")
    u = BlogUser.objects.get(username=user)
    t = BlogTopic.objects.get(title__contains=topic)
    topic_detail = BlogPost.objects.filter(topic = t, title=title, user=u)
    return render(request, 'posts/blogpost.html', {'topicdetail':topic_detail})