from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.views import View

from .models import News, Comment
from .forms import ArticleForm

def index(request):
    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
        return redirect("news:article", article_id=article.id)
    articles = News.objects.order_by("-created_at")
    form = ArticleForm()
    context = {"articles": articles, "form": form}
    return render(request, "news/index.html", context)

def article(request, article_id):
    article = get_object_or_404(News, pk=article_id)
    if request.POST:
        comment = Comment(content=request.POST["content"], news=article)
        comment.save()
        return redirect("news:article", article_id=article.id)

    comments = article.comment_set.all().order_by("-created_at")
    context = {
        "article": article,
        "comments": comments,
    }
    return render(request, "news/article.html", context)

class ArticleEdit(View):
    def get(self, request, article_id):
        article = get_object_or_404(News, pk=article_id)
        form = ArticleForm(instance=article)
        return render(request, "news/edit.html", {"form": form, "article_id": article_id})

    def post(self, request, article_id):
        article = get_object_or_404(News, pk=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("news:article", article_id=article.id)