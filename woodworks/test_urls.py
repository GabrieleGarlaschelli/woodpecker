from django.test import TestCase, Client
from django.urls import reverse, resolve

from woodworks.views import index, detail, order, like, update_order_status, about_us, rate, unlike

#qui eseguiamo i test per gli urls
class TestUrls(TestCase):
    def test_homepage(self):
        url = reverse('woodworks:index')
        self.assertEqual(resolve(url).func, index)

    def test_dettaglioWoodwork(self):
        url = reverse('woodworks:detail', args=[1])
        self.assertEqual(resolve(url).func, detail)

    # def test_listaWoodwork(self):
    #     url = reverse('woodworks:list')
    #     self.assertEqual(resolve(url).func, list)

    def test_formOrdina(self):
        url = reverse('woodworks:order', args=[1])
        self.assertEqual(resolve(url).func, order)

    def test_like(self):
        url = reverse('woodworks:like', args=[1])
        self.assertEqual(resolve(url).func, like)

    def test_update_order_status(self):
        url = reverse('woodworks:update_order_status', args=[1])
        self.assertEqual(resolve(url).func, update_order_status)

    def test_rate(self):
        url = reverse('woodworks:rate', args=[1])
        self.assertEqual(resolve(url).func, rate)

    def test_unlike(self):
        url = reverse('woodworks:unlike', args=[1])
        self.assertEqual(resolve(url).func, unlike)

    def test_about_us(self):
        url = reverse('woodworks:about_us')
        self.assertEqual(resolve(url).func, about_us)