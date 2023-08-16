from django.forms import ModelForm
from .models import News


class ArticleForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "content"]


'''
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=256)
    content = forms.CharField(max_length=256)
'''