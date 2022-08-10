from django.contrib import admin
from .models import Evuser

# Register your models here.

class EvuserAdmin(admin.ModelAdmin):
  list_display = ('userid', 'name', 'phone', 'address', 'status', 'register_dttm')

admin.site.register(Evuser, EvuserAdmin)
