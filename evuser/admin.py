from django.contrib import admin
from .models import Evuser

# Register your models here.

class EvuserAdmin(admin.ModelAdmin):
  list_display = ('userid', 'name', 'email', 'phone', 'address', 'category', 'status', 'level', 'last_use_dttm', 'register_dttm')

admin.site.register(Evuser, EvuserAdmin)
