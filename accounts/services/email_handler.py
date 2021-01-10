from django.core.mail import send_mail

def send(to, subject, text):
  send_mail(
    subject,
    text,
    'thewood.pecker@gmail.com',
    [to]
  )