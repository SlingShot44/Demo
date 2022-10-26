from django.urls import path
from .consumers import DemoConsumer

websocket_urlpatterns = [
    path("ws/", DemoConsumer.as_asgi()),
]