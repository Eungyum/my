from django.db import models

class Message(models.Model):
    name = models.CharField("이름", max_length=100)
    phone = models.CharField("전화번호", max_length=20)
    email = models.CharField("이메일", max_length=100)
    content = models.TextField("내용")
    created_at = models.DateTimeField("작성일", auto_now_add=True)
    class Meta:
        verbose_name = "메시지"
        verbose_name_plural = "메시지"
    def __str__(self):
        return f"{self.name}_{self.phone}_{self.email}"