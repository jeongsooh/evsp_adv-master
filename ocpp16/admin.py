from django.contrib import admin
from .models import Ocpp16

# Register your models here.

class Ocpp16Admin(admin.ModelAdmin):
  list_display = ('cpnumber', 'msg_direction','connection_id', 'msg_name', 'msg_content', 'register_dttm',)

admin.site.register(Ocpp16, Ocpp16Admin)
