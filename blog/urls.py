from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles, name='articles'),
    path('<slug:article_slug>', views.get_article, name='article'),
]