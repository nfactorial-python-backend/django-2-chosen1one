from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from .models import News, Comment

def index(request):
    if request.POST:
        article = News(title=request.POST["title"], content=request.POST["content"])
        article.save()
        return redirect("news:article", article_id=article.id)
    articles = News.objects.order_by("-created_at")
    context = {"articles": articles}
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