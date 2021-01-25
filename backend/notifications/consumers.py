import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
  async def websocket_connect(self, event):
    await self.channel_layer.group_add(
      'notifications_for_user_id_{}'.format(self.scope['user'].pk),
      self.channel_name
    )
    await self.accept()

  async def websocket_disconnect(self, event):
     await self.channel_layer.group_discard(
            'notifications_for_user_id_{}'.format(self.scope['user'].pk),
            self.channel_name
        )

  async def user_notification(self, event):
      await self.send(text_data = event['message'])