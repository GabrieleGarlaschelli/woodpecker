from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def test_superuser_check(self):
        response = self.client.get(reverse('woodworks:superuser_check'))
        self.assertEquals(response.status_code, 302)

    def test_index(self):
        response = self.client.get(reverse('woodworks:index', args=[2]))
        self.assertEquals(response.status_code, 200)
#da farne almeno 5/6