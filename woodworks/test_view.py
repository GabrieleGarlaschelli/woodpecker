from django.test import TestCase, Client
from django.urls import reverse
from woodworks.models import Woodwork
from accounts.models import CustomUser, Customer
import datetime
from django.utils import timezone


class TestViews(TestCase):
    def setUp(self):
        Woodwork.objects.create(id=1, title="lion", description="roar", publication_date=datetime.datetime.now(tz=timezone.utc), created_at=datetime.datetime.now(tz=timezone.utc))
        self.adminuser = CustomUser.objects.create_user('admin', 'admin@test.com', 'pass')
        self.adminuser.save()
        self.adminuser.is_staff = True
        self.adminuser.save()

        customer = Customer.objects.create(user_id=self.adminuser.id)
        customer.save()

        self.client.login(username='admin', password='pass')

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 302)
    
    def test_detail(self):
        response = self.client.get(reverse('woodwork_detail', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_rate(self):
        response = self.client.post(reverse('rate', args=[1]), {'rate': 5})
        self.assertEquals(response.status_code, 200)

    def test_is_liked(self):
        response = self.client.get(reverse('is_liked', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_like(self):
        response = self.client.get(reverse('like', args=[1]))
        self.assertEquals(response.status_code, 200)
        