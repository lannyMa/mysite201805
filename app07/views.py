from django.shortcuts import render

# Create your views here.
from app07.forms import ArticleForm
from app07.models import Article


def index(request):
    article = Article.objects.get(pk=1)
    article_form = ArticleForm(instance=article)
    return render(request, 'app07/index.html', {'article_form': article_form})
