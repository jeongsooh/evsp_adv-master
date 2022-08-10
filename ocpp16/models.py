from django.db import models

# Create your models here.

class Ocpp16(models.Model):
  cpname = models.CharField(max_length=64, blank=True)
  consumer = models.CharField(max_length=255, blank=True)

  class Meta:
    db_table = 'evsp_ocpp16'
    verbose_name = 'CP커넥션'
    verbose_name_plural = 'CP커넥션'