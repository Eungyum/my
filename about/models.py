from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class About(models.Model):
    photo = models.ImageField("프로필사진", upload_to='about/', blank=True, null=True)
    name = models.CharField("이름", max_length=10, blank=True, null=True)
    age = models.IntegerField("나이", blank=True, null=True)
    major1 = models.CharField("대학원전공", max_length=20, blank=True, null=True)
    major2 = models.CharField("학부전공", max_length=20, blank=True, null=True)
    social = models.CharField("소셜링크", max_length=20, blank=True, null=True)
    title = models.TextField("제목", blank=True, null=True)
    content = RichTextUploadingField("본문 내용")
    ongoing_pl = models.ImageField("진행중프로젝트 이미지", upload_to='about/', blank=True, null=True)
    is_active = models.BooleanField("활성여부", default=False)
    created_at = models.DateTimeField("작성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)
    class Meta:
        verbose_name = "어바웃 페이지 설정"
        verbose_name_plural = "어바웃 페이지 설정"
    def __str__(self):
        return self.title
    
class RAG(models.Model):
    title = models.CharField("제목", max_length=100, blank=True, null=True)
    content = models.TextField("본문 내용")
    created_at = models.DateTimeField("작성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)
    is_active = models.BooleanField("활성여부", default=False)
    class Meta:
        verbose_name = "RAG"
        verbose_name_plural = "RAG"
    def __str__(self):
        return self.title
    
class AIConvHistory(models.Model):
    created_at = models.DateTimeField("작성일", auto_now_add=True)
    ask = models.TextField("질문내용", blank=True, null=True)
    ip = models.CharField("사용자ip", max_length=225, blank=True, null=True)
    answer = models.TextField("답변내용", blank=True, null=True)
    model = models.CharField("LLM모델명", max_length=225, blank=True, null=True)
    rag = models.ForeignKey(RAG, verbose_name="RAG", on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name = "방문자대화기록"
        verbose_name_plural = "방문자대화기록"
    def __str__(self):
        return self.ask
    