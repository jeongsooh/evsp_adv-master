from django.contrib import admin
from .models import Msglog

# Register your models here.

class MsglogAdmin(admin.ModelAdmin):
  list_display = ('cpname', 'connection_id', 'msg_direction', 'msg_name', 'msg_content', 'register_dttm',)

admin.site.register(Msglog, MsglogAdmin)
