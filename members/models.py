from django.db import models

# Create your models here.

class Members(models.Model):
    username = models.CharField(max_length=64, verbose_name="사용자")
    useremail = models.EmailField(max_length=128, verbose_name="이메일")
    created = models.DateTimeField(auto_now_add=True, verbose_name="가입일시")
    update = models.DateTimeField(auto_now_add=True, verbose_name="수정일시")

    class Meta:
        db_table = "o2_users"
        verbose_name = '오픈튜토리얼스 사용자'
        verbose_name_plural = 'o2 사용자'

