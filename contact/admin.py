from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at')
    list_display_links = ('name', 'phone', 'email', 'created_at')
    list_filter = ('name', 'phone', 'email', 'created_at')
    search_fields = ('name', 'phone', 'email', 'created_at')
    