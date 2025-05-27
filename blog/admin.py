from django.contrib import admin
from .models import Post

class PostModel(admin.ModelAdmin):
    list_display = ['title','author','body']

admin.site.register(Post, PostModel)
