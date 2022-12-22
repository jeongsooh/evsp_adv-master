import django_filters
from .models import Evcharger

class EvchargerFilter(django_filters.FilterSet):
  class Meta:
    model = Evcharger
    fields = ['cpnumber', 'cpname', 'partner_id']