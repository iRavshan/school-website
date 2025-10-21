from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Event


def all_events(request):
    events = get_list_or_404(Event)
    context = {
        'events': events
    }
    return render(request, 'blog/events.html', context)


def get_event(request, event_slug):
    event = get_object_or_404(Event, slug=event_slug)
    context = {
        'event': event
    }
    return render(request, 'blog/event.html', context)