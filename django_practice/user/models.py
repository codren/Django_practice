from django.db import models
class User(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(verbose_name='비밀번호', max_length=128)
    register_date = models.DateTimeField(verbose_name='등록날짜', auto_now_add=True)

    def __str__(self):
        return self.email
    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자' 
