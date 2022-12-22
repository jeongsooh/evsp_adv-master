from django.contrib import admin
from .models import Budget

# Register your models here.

class BudgetAdmin(admin.ModelAdmin):
  list_display = ('userid', 'points', 'reserved', 'consumed', 'status', 'method', 'register_dttm')

admin.site.register(Budget, BudgetAdmin)
