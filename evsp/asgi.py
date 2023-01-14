import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import ocpp16.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evsp.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket': AuthMiddlewareStack(
    URLRouter(
      ocpp16.routing.websocket_urlpatterns 
    )
  ) 
})
