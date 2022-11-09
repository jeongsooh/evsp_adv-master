from django.db import models

# Create your models here.

class Clients(models.Model):
  cpnumber = models.CharField(max_length=64, blank=True, verbose_name='충전기번호')
  channel_name = models.CharField(max_length=64, blank=True, verbose_name='채널이름')
  channel_status = models.CharField(max_length=64, blank=True, verbose_name='채널상태')
  cp_status = models.CharField(max_length=64, blank=True, verbose_name='충전기상태')
  connection_id = models.CharField(max_length=256, blank=True, verbose_name='커넥션아이디')
  authorized_tag = models.CharField(max_length=64, verbose_name='승인된 카드테그')

  def __str__(self):
    return self.cpnumber

  class Meta:
    db_table = 'my_ocpp_clients'
    verbose_name = '충전기채널'
    verbose_name_plural = '충전기채널'
