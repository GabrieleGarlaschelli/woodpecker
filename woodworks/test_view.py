from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 302)
    
    def test_detail(self):
        response = self.client.get(reverse('woodwork_detail', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_rate(self):
        response = self.client.get(reverse('rate', args=[1]))
        self.assertEquals(response.status_code, 200)

    # def test_order(self):
    #     response = self.client.get(reverse('order'))
    #     self.assertEquals(response.status_code, 200)

    def test_is_liked(self):
        response = self.client.get(reverse('is_liked', args=[1]))
        self.assertEquals(response.status_code, 302)

    def test_like(self):
        response = self.client.get(reverse('like', args=[1]))
        self.assertEquals(response.status_code, 302)
        