from django.core import mail
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
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_form.html')

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


class SubscriptionPostTest(TestCase):

    def setUp(self):
        data = dict(
            name='Renato B',
            cpf='12345678901',
            email='jose.renato77@gmail.com',
            phone='86995925144')
        self.resp = self.client.post('/inscricao/', data=data)
        self.mail = mail.outbox[0]

    def test_post(self):
        self.assertEqual(self.resp.status_code, 302)

    def test_send_mail(self):
        self.assertEqual(len(mail.outbox), 1)

    def test_mail_content_subject(self):
        self.assertEqual(self.mail.subject, 'Inscrição no Eventex')

    def test_mail_content_from(self):
        self.assertEqual(self.mail.from_email, 'contato@eventex.com.br')

    def test_mail_content_to(self):
        self.assertIn('jose.renato77@gmail.com', self.mail.to)

    def test_mail_content_cc(self):
        self.assertIn('contato@eventex.com.br', self.mail.to)

    def test_mail_content_body_name(self):
        self.assertIn('Renato B', self.mail.body)

    def test_mail_content_body_cpf(self):
        self.assertIn('12345678901', self.mail.body)

    def test_mail_content_body_phone(self):
        self.assertIn('86995925144', self.mail.body)


class SubscriptionPostErrors(TestCase):
    def setUp(self):
        data = {}
        self.resp = self.client.post('/inscricao/', data=data)

    def test_no_redirect(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_form.html')

    def test_has_errors_form(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)


class SubscriptionSuccessMessage(TestCase):
    def test_success_message(self):
        data = dict(
            name='Renato B',
            cpf='12345678901',
            email='jose.renato77@gmail.com',
            phone='86995925144')
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')
