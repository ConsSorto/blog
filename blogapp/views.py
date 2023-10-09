from django.shortcuts import render
from .models import Article, Category
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    articles = Article.objects.filter(public=True).order_by('created_at')

    paginator = Paginator(articles, 5)

    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/articles.html', {'articles': page_articles})


def category_articles(request, category_id):
    category = Category.objects.get(id=category_id)

    articles = Article.objects.filter(
        public=True, categories=category_id).order_by('created_at')

    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'categories/category.html', {'category': category, 'articles': page_articles})


def article(request, article_id):
    article = Article.objects.get(id=article_id, public=True)
    return render(request, 'articles/article.html', {'article': article})
