from django.contrib import admin
from .models import Clients

# Register your models here.

class ClientsAdmin(admin.ModelAdmin):
  list_display = ('cpnumber', 'cp_status','channel_name', 'connection_id', 'channel_status',)

admin.site.register(Clients, ClientsAdmin)
