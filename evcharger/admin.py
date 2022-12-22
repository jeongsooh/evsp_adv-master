from django.contrib import admin
from .models import Evcharger

# Register your models here.

class EvchargerAdmin(admin.ModelAdmin):
  list_display = ('cpname', 'cpnumber', 'partner_id', 'public_use', 'cpstatus', 'connector_id_0', 'connector_id_0_status', 'connector_id_1', 'connector_id_1_status', 'address', 'manager_id', 'cpversion', 'register_dttm', 'last_modified_dttm', 'fw_version')

admin.site.register(Evcharger, EvchargerAdmin)
