import django_filters
from .models import Charginginfo

class CharginginfoFilter(django_filters.FilterSet):
  class Meta:
    model = Charginginfo
    fields = {
      'userid':['exact'],
      'cpnumber':['exact'],
      'start_dttm':['gt'],
      'end_dttm':['lt'],
    }