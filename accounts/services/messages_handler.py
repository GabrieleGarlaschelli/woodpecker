from accounts.models import CustomUser, Chat, Message
from django.urls import reverse
import datetime
import requests

def handle_received_message(message, from_user, user_chat_id):
  chat = Chat.objects.filter(user_id=user_chat_id).first()
  text = "%s ha detto:\n%s" % (from_user, message)

  message = Message.objects.create(
      chat_id=chat.id,
      body=message,
      sender=from_user,
      created_at=datetime.datetime.now(),
    )

  telegram_notify(text)

  return True

def open_chat(user_id):
  user = CustomUser.objects.filter(id=user_id).first()

  chat = None
  notify_on_telegram = False
  existing_chat = Chat.objects.filter(user_id=user_id).first()
  if(existing_chat):
    if(existing_chat.status != Chat.OPENED):
      notify_on_telegram = True
      existing_chat.status = Chat.OPENED
      existing_chat.save()
  else:
    notify_on_telegram = True
    chat = Chat.objects.create(
      user_id=user_id,
      created_at=datetime.datetime.now(),
    )

  if notify_on_telegram:
    text = "%s ha chiesto assistenza sul sito dei woodpecker, vai ad aiutarlo! %s" % (user, reverse('chat_with', args=(user_id)))
    telegram_notify(text)

  return {'has_opened_new_chat': notify_on_telegram}

def close_chat_with_user(chat_user_id):
  chat = Chat.objects.filter(user_id=chat_user_id).first()
  chat.status = Chat.CLOSED
  chat.save()

  telegram_notify("È stata chiusa la chat con %s" % chat_user_id)
  return True

def has_open_chat(chat_user_id):
  return Chat.objects.filter(user_id=chat_user_id, status=Chat.OPENED).count() > 0

def telegram_notify(text):
  r = requests.post('https://api.telegram.org/bot1368119163:AAGjwaTG0LWVWnXCUCNQP6yWL-PbfrkiMZY/sendMessage', data = {'text':text, 'chat_id': 270875692})
  r = requests.post('https://api.telegram.org/bot1368119163:AAGjwaTG0LWVWnXCUCNQP6yWL-PbfrkiMZY/sendMessage', data = {'text':text, 'chat_id': 270110844})


