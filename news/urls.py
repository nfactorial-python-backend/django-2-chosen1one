from django.urls import path
from . import views

app_name = "news"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:article_id>/", views.article, name="article"),
    path("<int:article_id>/edit", views.ArticleEdit.as_view(), name="article_edit"),
]