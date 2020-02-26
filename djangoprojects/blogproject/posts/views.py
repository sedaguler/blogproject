from django.shortcuts import render, redirect
from .models import BlogPost
from .models import BlogTopic
from .models import BlogUser
from .forms import BlogPostForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login/")
def topic_list(request):
    all_topics = BlogTopic.objects.filter(pk__in=BlogPost.objects.values('topic').annotate(count=Count('topic')).values('topic')).annotate(tcount=Count('title')).values('title')
    return render(request, 'posts/topics.html', {'listoftopics':all_topics})

@login_required(login_url="/accounts/login/")
def single_topic_list(request, topic):
    single_topic_list = BlogPost.objects.filter(topic = BlogTopic.objects.get(title=topic)).annotate(tcount=Count('title')).values('topic','title').annotate(count=Count('topic')).values('topic','title')
    return render(request, 'posts/blogtopictitle.html', {'singletopiclist':single_topic_list, 'tpc':topic})

@login_required(login_url="/accounts/login/")
def topic_title_detail(request, topic, title):
    t = BlogTopic.objects.get(title=topic)
    topic_detail = BlogPost.objects.filter(topic = t, title=title)
    return render(request, 'posts/blogpost.html', {'topicdetail':topic_detail})

@login_required(login_url="/accounts/login/")
def topic_title_user_detail(request, topic, title, user):
    u = BlogUser.objects.get(username=user)
    t = BlogTopic.objects.get(title__contains=topic)
    topic_detail = BlogPost.objects.filter(topic = t, title=title, user=u)
    return render(request, 'posts/blogpost.html', {'topicdetail':topic_detail})

@login_required(login_url="/accounts/login/")
def publish(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']
            topic = form.cleaned_data['topic']
            t = BlogTopic.objects.filter(title=topic)[0]
            u = BlogUser.objects.filter(username=user)[0]
            p = BlogPost(user=u, topic=t, title=title, message=message)
            p.save()
            return redirect('select')
    else:
        form = BlogPostForm()
    return render(request, 'posts/publish.html', {'form': form})
