from woodworks.models import Order
import datetime

def order_woodwork(woodwork_id, customer_id, notes, quantity, expiration, address_id):
  record_count = Order.objects.filter(woodwork_id=woodwork_id, customer_id=customer_id).count()
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
    return order.save()
  else:
    return False