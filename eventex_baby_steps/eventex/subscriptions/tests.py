from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/inscricao/') 

    def test_access_subscription(self):
        """Mus return status code 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Must use template subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        """Must contain HTML form"""
        self.assertContains(self.resp, '<form', 1)
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="submit"', 1)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"', 1)

    def test_csrf(self):
        """Must contain csrf token"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_instance_form(self):
        self.assertIsInstance(self.resp.context['form'], SubscriptionForm)

    def test_form_has_fields(self):
        form = self.resp.context['form']
        fields = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(fields, list(form.fields))


'''class SubscriptionPostTest(TestCase):

    def test_post(self):
        data = dict(
            name='Renato B',
            cpf='12345678901',
            email='jose.renato77@gmail.com',
            phone='86995925144')
        response = self.client.post('/inscricao/', data=data)

        self.assertEqual(response.context['form'].email, 'jose.renato77@gmail.com')
        self.assertEqual(response.context['form']['name'], 'Renato J')
        self.assertEqual(response.context['form']['cpf'], '12345678901')
        self.assertEqual(response.context['form']['phone'], '86995925144')
'''