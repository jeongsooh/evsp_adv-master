from django.db import models

# Create your models here.
class Budget(models.Model):
  RESERVED_CATEGORY = [
    ('구매', '구매'),
    ('포인트취득', '포인트취득'),
    ('양수', '양수'),
    ('기타', '기타'),
  ]
  CONSUMED_CATEGORY = [
    ('충전', '충전'),
    ('양도', '양도'),
    ('기타', '기타'),
  ]
  RESERVED_STATUS = [
    ('정상', '정상'),
    ('부족', '부족'),
    ('정지', '정지'),
  ]

  userid = models.CharField(max_length=64, verbose_name='회원아이디')
  points = models.IntegerField(verbose_name='포인트')
  reserved = models.CharField(max_length=64, 
    choices=RESERVED_CATEGORY, default= '구매', verbose_name='적립구분')
  consumed = models.CharField(max_length=64, 
    choices=CONSUMED_CATEGORY, default= '충전', verbose_name='사용구분')
  status = models.CharField(max_length=64, 
    choices=RESERVED_STATUS, default= '정상', verbose_name='적립상태')
  method = models.CharField(max_length=64, verbose_name='적립또는사용수단')
  register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

  def __str__(self):
    return self.userid

  class Meta:
    db_table = 'evsp_budget'
    verbose_name = '충전가능금액'
    verbose_name_plural = '충전가능금액'
