from django.contrib import admin
from .models import Event

admin.site.register(Event)

admin.site.site_header = "Karshi Presidential School"
admin.site.site_title = "Karshi Presidential School"
admin.site.index_title = "Dashboard"