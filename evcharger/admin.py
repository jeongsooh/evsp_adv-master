from django.contrib import admin
from .models import Evcharger

# Register your models here.

class EvchargerAdmin(admin.ModelAdmin):
  list_display = ('cpnumber', 'cpname','cpstatus',)

admin.site.register(Evcharger, EvchargerAdmin)
