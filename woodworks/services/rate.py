from woodworks.models import Rating
import datetime

def rate_woodwork(woodwork_id, customer_id, rate, comment):
  record_count = Rating.objects.filter(woodwork_id=woodwork_id, customer_id=customer_id).count()
  if record_count == 0:
    rating = Rating.objects.create(
      woodwork_id=woodwork_id,
      customer_id=customer_id,
      rate=rate,
      comment=comment
    )
    return rating.save()
  else:
    return False