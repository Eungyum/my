from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

# 블로그

class Category(models.Model):
    name = models.CharField("카테고리명", max_length=100)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    thumbnail1 = models.ImageField("워크섬네일", upload_to='thumbnails/', blank=True, null=True)
    thumbnail2 = models.ImageField("블로그섬네일", upload_to='thumbnails/', blank=True, null=True)
    is_index = models.BooleanField("메인페이지 게시 여부", default=False)
    pop_words = models.CharField("메인페이지 팝 문구", max_length=50, blank=True, null=True)
    is_visible = models.BooleanField("블로그리스트 노출 여부", default=False)
    title = models.CharField("제목", max_length=200)
    content = RichTextUploadingField("본문 내용")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="카테고리")
    tags = TaggableManager(verbose_name="태그", blank=True)
    created_at = models.DateTimeField("작성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)
    class Meta:
        verbose_name = "블로그"
        verbose_name_plural = "블로그"
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="게시글")
    author = models.CharField("작성자", max_length=100)
    author_email = models.CharField("작성자 이메일", max_length=200, blank=True, null=True)
    pw = models.CharField("비밀번호", max_length=50, blank=True, null=True)
    content = models.TextField("댓글 내용")
    created_at = models.DateTimeField("작성일", auto_now_add=True)
    is_visible = models.BooleanField("노출 여부", default=False)
    class Meta:
        verbose_name = "코멘트"
        verbose_name_plural = "코멘트"
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    