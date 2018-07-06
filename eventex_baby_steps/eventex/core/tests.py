from django.test import TestCase

class HomeTest(TestCase):
    def test_status_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')