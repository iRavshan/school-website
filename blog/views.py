from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post


def all_articles(request):
    articles = get_list_or_404(Post)
    context = {
        'articles': articles
    }
    return render(request, 'blog/blog.html', context)


def get_article(request, article_slug):
    article = get_object_or_404(Post, slug=article_slug)
    context = {
        'post': article
    }
    return render(request, 'blog/post.html', context)