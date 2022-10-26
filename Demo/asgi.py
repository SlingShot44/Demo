import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'BackendSchluesselKasten.settings')

async def lifespan_app(scope, receive, send):
    if scope['type'] == 'lifespan':
        while True:
            message = await receive()
            if message['type'] == 'lifespan.startup':
                await send({'type': 'lifespan.startup.complete'})
            elif message['type'] == 'lifespan.shutdown':
                await send({'type': 'lifespan.shutdown.complete'})
                return
                
django_asgi_app = get_asgi_application()

import DemoApp.routing
import logging

class TestMiddleware():
    def __init__(self, inner):
        self.inner = inner
    async def __call__(self, scope, receive, send):
        logger = logging.getLogger('django')
        logger.info(scope)
        return await self.inner(scope, receive, send)

application = ProtocolTypeRouter({
    "http": TestMiddleware(django_asgi_app),
    "websocket": AllowedHostsOriginValidator(
        TestMiddleware(
            AuthMiddlewareStack(
                URLRouter(
                    DemoApp.routing.websocket_urlpatterns
                )
            ),
        )
    ),
    "lifespan": lifespan_app,
})
