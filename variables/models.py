from django.db import models

# Create your models here.

class Variables(models.Model):
  group = models.CharField(max_length=64, blank=True, verbose_name="기준변수")
  interval = models.IntegerField(null=True, verbose_name='확인주기')

  def __str__(self):
    return self.group

  class Meta:
    db_table = 'evsp_variables'
    verbose_name = '운용변수'
    verbose_name_plural = '운용변수'