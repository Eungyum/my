from django.db import models

class Menu(models.Model):
    logoimg = models.ImageField("로고이미지", upload_to='site/', blank=True, null=True)
    menu1 = models.CharField("메뉴1", max_length=20, blank=True, null=True)
    menu1_link = models.CharField("메뉴1 url 네임", max_length=100, blank=True, null=True)
    menu2 = models.CharField("메뉴2", max_length=20, blank=True, null=True)
    menu2_link = models.CharField("메뉴2 url 네임", max_length=100, blank=True, null=True)
    menu3 = models.CharField("메뉴3", max_length=20, blank=True, null=True)
    menu3_link = models.CharField("메뉴3 url 네임", max_length=100, blank=True, null=True)
    menu4 = models.CharField("메뉴4", max_length=20, blank=True, null=True)
    menu4_link = models.CharField("메뉴4 url 네임", max_length=100, blank=True, null=True)
    menu5 = models.CharField("메뉴5", max_length=20, blank=True, null=True)
    menu5_link = models.CharField("메뉴5 url 네임", max_length=100, blank=True, null=True)
    menu6 = models.CharField("메뉴6", max_length=20, blank=True, null=True)
    menu6_link = models.CharField("메뉴6 url 네임", max_length=100, blank=True, null=True)
    class Meta:
        verbose_name = "헤더"
        verbose_name_plural = "헤더"
    def __str__(self):
        return f"{self.menu1}_{self.menu2}_{self.menu3}_{self.menu4}_{self.menu5}_{self.menu6}"