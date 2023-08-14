from django.db import models

class News(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def has_comments(self):
        comments = self.comment_set.all()
        return len(comments) > 0


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.content