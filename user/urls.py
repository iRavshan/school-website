from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.sign_in, name='signin'),
    path('logout/', views.log_out, name='logout'),
]