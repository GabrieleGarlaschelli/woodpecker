from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 302)
#da farne almeno 5/6