from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/accounts/chat/(?P<user_id>\w+)&(?P<is_admin>\w+)/$', consumers.ChatConsumer.as_asgi()),
]