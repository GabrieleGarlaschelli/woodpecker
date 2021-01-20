from django.test import TestCase
from woodworks.services import order
import datetime
from django.utils import timezone

class TestOrder(TestCase):
    def test_order(self):
      Woodwork.objects.order(woodwork_id=1, customer_id=1, notes'ciao', quantity=2, expiration=datetime.datetime.now(tz=timezone.utc address_id=1))
        