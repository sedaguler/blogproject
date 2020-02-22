from django.db import models

# Create your models here.

class BlogTopic(models.Model):
    title = models.CharField(max_length=35)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


class BlogUser(models.Model):
    username = models.CharField(max_length=30, unique = True)
    password = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.username


class BlogPost(models.Model):
    title = models.CharField(max_length=36)
    message = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(null=True)
    topic = models.ForeignKey(BlogTopic, on_delete=models.CASCADE)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
