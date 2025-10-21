from django.contrib import admin
from django.urls import path, include
import core.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('events/', include('blog.urls')),
    path('', views.home, name='home')
]