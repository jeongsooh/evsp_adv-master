from django.test import TestCase

# Create your tests here.
from .models import Charginginfo
from charginginfo.kepco_tariff import calculate_price

charginginfo = Charginginfo.objects.filter(cpnumber="100001", userid="jeongsooh1").values().last()
print('charginginfo: ', charginginfo)