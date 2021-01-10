from woodworks.models import Order
from accounts.services.email_handler import send
import datetime

def update_woodwork_order_status(order_id, status):
  order = Order.objects.get(pk=order_id)
  order.status = status
  order.save()

  if order.status == Order.DONE:
    text = "Gentile signor %s,\nLa informiamo che il suo ordine del woodwork %s è in attesa di consegna. Ci contatti per il ritiro" % (order.customer.customuser.fullname, order.woodwork.title)
    send(order.customer.customuser.email, 'Ordine in attesa di consegna', text)