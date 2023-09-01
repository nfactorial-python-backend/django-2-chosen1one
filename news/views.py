from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required

from .models import News, Comment
from .forms import ArticleForm, SignUpForm

@login_required(login_url="/login/")
@permission_required("news.add_news", login_url="/login/")
def index(request):
    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            db_article = form.save(commit=False)
            db_article.author = request.user
            db_article.save()
        return redirect("news:article", article_id=db_article.id)
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
            db_article = form.save(commit=False)
            db_article.author = request.user
            db_article.save()
            return redirect("news:article", article_id=article.id)

def sign_up(request):
   if request.method == 'POST':
       form = SignUpForm(request.POST)
       if form.is_valid():
           user = form.save()
           group = Group.objects.get(name="default")
           group.user_set.add(user) 
           login(request, user)
           return redirect('news:index')
   else:
       form = SignUpForm()
   return render(request, 'registration/sign-up.html', {"form": form})

def delete_news(request, article_id):
    article = get_object_or_404(News, pk=article_id)
    if request.POST:
        if request.user == article.author or request.user.has_perm("news.delete_news"):
            article.delete()
    return redirect('news:index')