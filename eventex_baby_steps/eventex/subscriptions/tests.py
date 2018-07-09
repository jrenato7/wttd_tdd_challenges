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
        """Must contain HTML form"""
        response = self.client.get('/inscricao/')
        self.assertContains(response, '<form', 1)
        self.assertContains(response, '<input', 6)
        self.assertContains(response, 'type="submit"', 1)
        self.assertContains(response, 'type="text"', 3)
        self.assertContains(response, 'type="email"', 1)

    def test_csrf(self):
        """Must contain csrf token"""
        response = self.client.get('/inscricao/')
        self.assertContains(response, 'csrfmiddlewaretoken')
