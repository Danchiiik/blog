from django.contrib import admin
from applications.posts.models import Category, Post, Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)