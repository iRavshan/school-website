from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Event


def all_events(request):
    #articles = get_list_or_404(Post)
    #context = {
        #'articles': articles
    #}
    return render(request, 'blog/events.html')


def get_event(request, event_slug):
    article = get_object_or_404(Event, slug=event_slug)
    context = {
        'post': article
    }
    return render(request, 'blog/post.html', context)