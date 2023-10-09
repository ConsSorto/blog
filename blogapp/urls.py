
from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.index, name='articles_index'),
    path('categorias/<int:category_id>',
         views.category_articles, name='category_articles'),
    path('article/<int:article_id>', views.article, name='article')
]
