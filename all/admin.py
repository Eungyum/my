from django.contrib import admin
from .models import Menu
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
        
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu1', 'menu2', 'menu3', 'menu4', 'menu5', 'menu6')
    list_display_links = ('menu1', 'menu2', 'menu3', 'menu4', 'menu5', 'menu6')
    list_filter = ('menu1', 'menu2', 'menu3', 'menu4', 'menu5', 'menu6')
    search_fields = ('menu1', 'menu2', 'menu3', 'menu4', 'menu5', 'menu6')