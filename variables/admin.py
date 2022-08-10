from django.contrib import admin
from .models import Variables

# Register your models here.

class VariablesAdmin(admin.ModelAdmin):
  list_display = ('group', 'interval',)

admin.site.register(Variables, VariablesAdmin)
