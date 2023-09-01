from django.urls import path
from . import views

app_name = "news"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:article_id>/", views.article, name="article"),
    path("<int:article_id>/edit", views.ArticleEdit.as_view(), name="article_edit"),
    path("sign-up/", views.sign_up, name="sign-up"),
    path("<int:article_id>/delete", views.delete_news, name="article_delelte"),
]