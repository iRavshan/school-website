from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('<slug:event_slug>', views.get_event, name='event'),
]