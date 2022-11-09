from django.db import models

# Create your models here.

class Charginginfo(models.Model):
  cpnumber = models.CharField(max_length=64, verbose_name='충전기번호')
  userid = models.CharField(max_length=64, verbose_name='회원아이디')
  # chargedphone = models.ForeignKey('evuser.Evuser', on_delete=models.CASCADE, verbose_name='전화번호')
  energy = models.IntegerField(verbose_name='충전량')
  amount = models.IntegerField(verbose_name='충전금액')
  start_dttm = models.DateTimeField(auto_now_add=False, verbose_name='충전시작일시')
  end_dttm = models.DateTimeField(auto_now_add=False, verbose_name='충전완료일시')

  # def __str__(self):
  #   return self.chargedname

  class Meta:
    db_table = 'evsp_charginginfo'
    verbose_name = '충전정보'
    verbose_name_plural = '충전정보'

