from django.test import TestCase
from woodworks.services.order import order_woodwork
import datetime
from django.utils import timezone

from woodworks.models import Woodwork
from accounts.models import CustomUser, Customer, Address

# test per la funzione order_woodwork
class TestOrder(TestCase):
    def setUp(self):
        Woodwork.objects.create(id=1, title="lion", description="roar", publication_date=datetime.datetime.now(tz=timezone.utc), created_at=datetime.datetime.now(tz=timezone.utc))
        self.adminuser = CustomUser.objects.create_user('admin', 'admin@test.com', 'pass')
        self.adminuser.save()
        self.adminuser.is_staff = True
        self.adminuser.save()

        customer = Customer.objects.create(user_id=self.adminuser.id)
        customer.save()

        Address.objects.create(id=1, customer_id=customer.id)
        self.client.login(username='admin', password='pass')

    def test_order(self):
      result = order_woodwork(
        woodwork_id=1, 
        customer_id=1, 
        notes='ciao', 
        quantity=2, 
        expiration=datetime.datetime.now(tz=timezone.utc), 
        address_id=1
      )
      # se l'ordine viene creato la funziona ritorna true
      self.assertTrue(result)
        