from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from .models import User


# Create your tests here.
class AccountsLoginViewTests(TestCase):
    def test_login_page_exist(self):
        """
        ページが存在するか
        """
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)


class AccountsAuthViewTests(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test', email='test1@test.com', password='password')

    def test_auth_success(self):
        data = {
            'username': 'test',
            'password': 'password',
        }

        response = self.client.post(reverse('accounts:auth'), data)
        self.assertRedirects(response, reverse('menu:main'), status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)


# class AccountsLogoutViewTests(TestCase):
#     def test_logout_page_exist(self):
#         """
#         ページが存在するか
#         """
#         # まずはログイン
#         response = self.client.get(reverse('accounts:logout'))
#         self.assertEqual(response.status_code, 200)