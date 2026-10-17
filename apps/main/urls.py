from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('education/', views.education, name='education'),
    path('about/', views.about, name='about'),
    path('admission/', views.admission, name='admission'),
    path('academic-calendar/', views.academic_calendar, name='academic_calendar'),
]
