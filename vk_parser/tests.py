from rest_framework.test import APITestCase
from django.urls import reverse


class TestEndpoint(APITestCase):
    def test_parser1(self):
        response = self.client.get(reverse('vk_parses:api:parser', kwargs={'wall_url': 'public207473117'}))
        right_result = 'один два два три три три четыре четыре четыре'
        self.assertEqual(response.data['words'], right_result)

    def test_parser2(self):
        response = self.client.get(reverse('vk_parses:api:parser', kwargs={'wall_url': 'club4256571743242353534'}))
        self.assertEqual(response.data['success'], False)

    def test_parser3(self):
        response = self.client.get(reverse('vk_parses:api:parser', kwargs={'wall_url': '42565717432423555555553534'}))
        self.assertEqual(response.data['success'], False)
