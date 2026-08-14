from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'department', 'occupation', 'is_local')
    list_filter = ('department', 'is_local')
    search_fields = ('first_name', 'last_name', 'occupation')
