from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('character:graffiti'))
        self.assertEqual(response.status_code, 200)