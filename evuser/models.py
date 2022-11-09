from django.db import models

# Create your models here.

class Evuser(models.Model):
  CONTRACTED = 'CONT'
  NORMAL = 'NOR'
  USER_STATUS = [
    ('정상', '정상'),
    ('해지', '해지'),
    ('유예', '유예'),
  ]
  USER_CATEGORY = [
    ('일반', '일반'),
    ('법인', '법인'),
    ('기타', '기타'),
  ]

  userid = models.CharField(max_length=64, verbose_name='회원아이디')
  password = models.CharField(max_length=128, verbose_name='비밀번호')
  name = models.CharField(max_length=64, verbose_name='회원이름')
  email = models.EmailField(max_length=128, verbose_name='이메일')
  phone = models.CharField(max_length=64, verbose_name='전화번호')
  category = models.CharField(max_length=64, 
    choices=USER_CATEGORY, default= '일반', verbose_name='회원구분')
  status = models.CharField(max_length=64, 
    choices=USER_STATUS, default= '정상', verbose_name='회원상태')
  address = models.TextField(verbose_name='주소')
  level = models.CharField(max_length=8, verbose_name='등급', 
    choices=(
      ('admin', 'admin'), 
      ('user', 'user')
  ))
  last_use_dttm = models.DateTimeField(auto_now_add=True, verbose_name='최근사용시간')
  register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

  def __str__(self):
    return self.userid

  class Meta:
    db_table = 'evsp_evuser'
    verbose_name = '회원'
    verbose_name_plural = '회원'


