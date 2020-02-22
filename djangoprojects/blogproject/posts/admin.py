from django.contrib import admin
from .models import BlogPost
from .models import BlogUser
from .models import BlogTopic

# Register your models here.
admin.site.register(BlogTopic)
admin.site.register(BlogUser)
admin.site.register(BlogPost)