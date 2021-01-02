from accounts.models import CustomUser, Chat, Message
import datetime
import requests

def handle_received_message(message, from_user, user_chat_id):
  chat = Chat.objects.filter(user_id=user_chat_id).first()
  text = "%s ha detto: %s" % (from_user, message)

  print('creating')
  message = Message.objects.create(
      chat_id=chat.id,
      body=message,
      sender=from_user,
      created_at=datetime.datetime.now(),
    )

  r = requests.post('https://api.telegram.org/bot1368119163:AAGjwaTG0LWVWnXCUCNQP6yWL-PbfrkiMZY/sendMessage', data = {'text':text, 'chat_id': 270875692})

  return True

def handle_connection_opened(user_id):
  user = CustomUser.objects.filter(id=user_id).first()

  chat = None
  notify_on_telegram = False
  existing_chat = Chat.objects.filter(user_id=user_id).first()
  if(existing_chat):
    if(existing_chat.status != Chat.OPENED):
      notify_on_telegram = True
      chat.update(status=Chat.OPENED)
  else:
    notify_on_telegram = True
    chat = Chat.objects.create(
      user_id=user_id,
      created_at=datetime.datetime.now(),
    )

  if notify_on_telegram: 
    text = "%s ha chiesto assistenza sul sito dei woodpecker, vai ad aiutarlo!" % user
    r = requests.post('https://api.telegram.org/bot1368119163:AAGjwaTG0LWVWnXCUCNQP6yWL-PbfrkiMZY/sendMessage', data = {'text':text, 'chat_id': 270875692})

  return True


