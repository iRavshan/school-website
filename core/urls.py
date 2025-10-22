from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import core.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('blog.urls')),
    path('', views.home, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)