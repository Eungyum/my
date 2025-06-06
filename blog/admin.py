from django.contrib import admin
from .models import Post, Comment, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(
        label="본문 내용",
        widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = Post
        fields = '__all__'
        
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('is_index', 'is_visible','category', 'title', 'created_at')
    list_display_links = ('is_index', 'category', 'is_visible', 'title', 'created_at')
    list_filter = ('is_index', 'category', 'is_visible', 'created_at')
    search_fields = ('title',)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at', 'is_visible')
    list_filter = ('created_at', 'post', 'is_visible')
    search_fields = ('post',)