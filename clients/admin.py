from django.contrib import admin
from .models import Clients

# Register your models here.

class ClientsAdmin(admin.ModelAdmin):
  list_display = ('cpnumber', 'channel_name', 'channel_status', 'cp_status','connection_id', 'authorized_tag', )

admin.site.register(Clients, ClientsAdmin)
