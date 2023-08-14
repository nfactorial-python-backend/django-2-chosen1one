from django.contrib import admin

from .models import News, Comment

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 5

class AdminNews(admin.ModelAdmin): 
    fields = ["title", "content"]
    inlines = [CommentInLine]
    list_display = ["title", "content", "created_at", "has_comments"]

admin.site.register(News, AdminNews)
admin.site.register(Comment)