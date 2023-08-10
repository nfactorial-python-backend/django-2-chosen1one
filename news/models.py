from django.db import models

class News(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)