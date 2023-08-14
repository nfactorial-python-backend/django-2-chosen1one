from django.test import TestCase

from .models import News, Comment


class NewsModelTests(TestCase):
    def test_has_comments_False(self):
        temp_news = News(title="YEEEESSS")
        temp_news.save()
        self.assertFalse(temp_news.has_comments())

    def test_has_comments_True(self):
        temp_news = News(title="YEEEESSS")
        temp_news.save()
        temp_news.comment_set.create(content="fine!")
        temp_news.save()
        self.assertTrue(temp_news.has_comments())
    
    def test_index_sorted(self):
        temp_news1 = News(title="Article_1")
        temp_news1.save()
        temp_news2 = News(title="Article_2")
        temp_news2.save()
        response = self.client.get("/news/")
        articles  = list(response.context["articles"])
        self.assertListEqual(articles, [temp_news2, temp_news1])
    
    def test_article(self):
        temp_news = News(title="Article_1")
        temp_news.save()
        response = self.client.get(f"/news/{temp_news.id}/")
        self.assertContains(response, "Article_1", 1, 200)
  
    def test_article_comments(self):
        temp_news = News(title="Article_1")
        temp_news.save()
        temp_news.comment_set.create(content="Comment1")
        temp_news.save()
        temp_news.comment_set.create(content="Comment2")
        temp_news.save()

        response = self.client.get(f"/news/{temp_news.id}/")
        print(response)
        comments = list(response.context["comments"])
        self.assertEqual(comments[0].content, "Comment2")
        self.assertEqual(comments[1].content, "Comment1")
