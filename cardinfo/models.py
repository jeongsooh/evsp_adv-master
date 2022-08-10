from django.db import models

# Create your models here.

class Cardinfo(models.Model):
  cardname = models.CharField(max_length=64, verbose_name='카드이름')
  cardtag = models.CharField(max_length=64, verbose_name='카드테그')
  cardstatus = models.CharField(max_length=64, verbose_name='배포상태')
  register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='카드등록일시')
  userid = models.CharField(max_length=64, verbose_name='회원아이디')

  class Meta:
    db_table = 'evsp_cardinfo'
    verbose_name = '카드정보'
    verbose_name_plural = '카드정보'