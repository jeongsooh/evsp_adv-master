from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
  re_path(r'webServices/ocpp/', consumers.Ocpp16Consumer.as_asgi())
]
