from django.urls import path 
from . import consumers 

websocket_urlpatterns = [
    path('accounts/home/',consumers.ChatConsumer.as_asgi()),
]