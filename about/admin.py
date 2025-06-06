from django.contrib import admin
from .models import About, RAG, AIConvHistory
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class AboutAdminForm(forms.ModelForm):
    content = forms.CharField(
        label="본문 내용",
        widget=CKEditorUploadingWidget()
    )
    class Meta:
        model = About
        fields = '__all__'
        
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    form = AboutAdminForm
    list_display = ('is_active', 'title', 'created_at')
    list_display_links = ('is_active', 'title', 'created_at')
    list_filter = ('is_active', 'title', 'created_at')
    search_fields = ('is_active', 'title', 'created_at')
    
@admin.register(RAG)
class RAGAdmin(admin.ModelAdmin):
    list_display = ('updated_at', 'title', 'is_active')
    list_display_links = ('updated_at', 'title', 'is_active')
    list_filter = ('updated_at', 'title', 'is_active')
    search_fields = ('updated_at', 'title', 'is_active')
    
@admin.register(AIConvHistory)
class AIConvHistoryAdmin(admin.ModelAdmin):
    list_display = ('ask', 'answer', 'ip', 'model', 'created_at')
    list_display_links = ('created_at', 'ask', 'answer', 'ip', 'model')
    list_filter = ('created_at', 'ask', 'answer', 'ip', 'model')
    search_fields = ('created_at', 'ask', 'answer', 'ip', 'model')

# class AIConvHistory(models.Model):
#     created_at = models.DateTimeField("작성일", auto_now_add=True)
#     ask = models.TextField("질문내용", blank=True, null=True)
#     ip = models.CharField("사용자ip", max_length=225, blank=True, null=True)
#     answer = models.TextField("답변내용", blank=True, null=True)
#     model = models.CharField("LLM모델명", max_length=225, blank=True, null=True)