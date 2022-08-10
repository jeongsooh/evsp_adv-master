from django.contrib import admin
from .models import Cardinfo

# Register your models here.

class CardinfoAdmin(admin.ModelAdmin):
  list_display = ('cardname', 'cardtag','cardstatus',)

admin.site.register(Cardinfo, CardinfoAdmin)