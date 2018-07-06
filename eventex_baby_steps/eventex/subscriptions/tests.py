from django.test import TestCase


class SubscriptionTest(TestCase):
    def test_access_subscription(self):
        """Mus return status code 200"""
        response = self.client.get('/inscricao/')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        """Must use template subscriptions/subscription_form.html"""
        response = self.client.get('/inscricao/')
        self.assertTemplateUsed(response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        response = self.client.get('/inscricao/')
        self.assertContains(response, 'input', 5)
        self.assertContains(response, 'submit', 1)
