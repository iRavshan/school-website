from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('leadership/', views.leadership, name='leadership'),
    path('teachers/', views.teachers, name='teachers'),
]
