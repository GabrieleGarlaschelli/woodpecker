from django.test import TestCase, Client
from django.urls import reverse, resolve

from woodworks.views import detail, order, like, update_order_status, about_us, rate, unlike

#qui eseguiamo i test per gli urls
class TestUrls(TestCase):

    def test_dettaglioWoodwork(self):
        url = reverse('woodwork_detail', args=[1])
        self.assertEqual(resolve(url).func, detail)

    # def test_listaWoodwork(self):
    #     url = reverse('woodworks:list')
    #     self.assertEqual(resolve(url).func, list)

    def test_formOrdina(self):
        url = reverse('order', args=[1])
        self.assertEqual(resolve(url).func, order)

    def test_like(self):
        url = reverse('like', args=[1])
        self.assertEqual(resolve(url).func, like)

    def test_update_order_status(self):
        url = reverse('update_order_status', args=[1])
        self.assertEqual(resolve(url).func, update_order_status)

    def test_rate(self):
        url = reverse('rate', args=[1])
        self.assertEqual(resolve(url).func, rate)

    def test_unlike(self):
        url = reverse('unlike', args=[1])
        self.assertEqual(resolve(url).func, unlike)

    def test_about_us(self):
        url = reverse('about_us')
        self.assertEqual(resolve(url).func, about_us)