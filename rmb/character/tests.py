from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

# Create your tests here.
class CharacterViewTests(TestCase):
    def test_graffiti_page_exist(self):
        """
        ページが存在するか
        """
        response = self.client.get(reverse('character:graffiti'))
        self.assertEqual(response.status_code, 200)

