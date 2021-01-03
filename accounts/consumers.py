import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from accounts.services.messages_handler import handle_received_message, open_chat, has_open_chat

class ChatConsumer(WebsocketConsumer):
  def connect(self):
    self.user_id = self.scope['url_route']['kwargs']['user_id']
    self.group_chat_name = 'chat_' + self.user_id
    self.first_message = True
    
    async_to_sync(self.channel_layer.group_add)(
      self.group_chat_name,
      self.channel_name
    )
    self.is_admin = self.scope['url_route']['kwargs']['is_admin'] == "true"

    if not self.is_admin and not has_open_chat(self.user_id):
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
    from_user = text_data_json['from']
    message_type = text_data_json['message_type']

    async_to_sync(self.channel_layer.group_send)(
      self.group_chat_name,
      {
        'type': message_type,
        'message': message,
        'from': from_user
      }
    )


    if self.first_message and from_user != 'woodpecker_admin':
      open_chat(self.user_id)
      self.first_message = False

    handle_received_message(message, from_user, self.user_id)

  def chat_message(self, event):
    message = event['message']
    message_from = event['from']

    self.send(text_data=json.dumps({
      'message': message,
      'message_from': message_from,
      'type': 'chat_message'
    }))

  def close_chat_message(self, event):
    message = event['message']
    message_from = event['from']

    self.send(text_data=json.dumps({
      'message': message,
      'message_from': message_from,
      'type': 'close_chat_message'
    }))