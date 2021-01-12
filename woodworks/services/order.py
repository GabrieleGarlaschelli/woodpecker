from woodworks.models import Order
import datetime
from django.db.models import Q
from accounts.services.messages_handler import telegram_notify

def order_woodwork(woodwork_id, customer_id, notes, quantity, expiration, address_id):
  record_count = Order.objects.filter(woodwork_id=woodwork_id, customer_id=customer_id).filter(~Q(status=Order.DELIVERED)).count()
  if record_count == 0:
    order = Order.objects.create(
      woodwork_id=woodwork_id,
      customer_id=customer_id,
      order_at=datetime.datetime.now(),
      quantity=quantity,
      notes=notes,
      expiration_on=expiration,
      to_address_id=address_id
    )
    order.save()
    telegram_notify("Ordine ricevuto:\n%s ha ordinato %s\nemail:%s" % (order.customer.fullname(), order.woodwork.title, order.customer.user.email))
    return True
  else:
    return False