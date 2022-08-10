from django.contrib import admin
from .models import Ocpp16

# Register your models here.

class Ocpp16Admin(admin.ModelAdmin):
  list_display = ('cpname', 'consumer',)

admin.site.register(Ocpp16, Ocpp16Admin)
