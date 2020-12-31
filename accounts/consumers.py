import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
  def connect(self):
    self.user_id = self.scope['url_route']['kwargs']['user_id']
    self.group_chat_name = 'chat_' + self.user_id
    print(self.group_chat_name)
    
    async_to_sync(self.channel_layer.group_add)(
      self.group_chat_name,
      self.channel_name
    )

    async_to_sync(self.channel_layer.group_send)(
      self.group_chat_name,
      {
        'type': 'chat_message',
        'message': "Ciao, in cosa posso esserti utile?",
        'from': "woodpecker_admin"
      }
    )

    self.accept()

  def disconnect(self, close_code):
    pass

  def receive(self, text_data):
    text_data_json = json.loads(text_data)
    message = text_data_json['message']

    async_to_sync(self.channel_layer.group_send)(
      self.group_chat_name,
      {
        'type': 'chat_message',
        'message': message,
        'from': self.user_id
      }
    )

  def chat_message(self, event):
    message = event['message']
    message_from = event['from']

    self.send(text_data=json.dumps({
      'message': message,
      'message_from': message_from
    }))