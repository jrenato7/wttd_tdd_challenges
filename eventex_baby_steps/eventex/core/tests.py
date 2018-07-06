# coding: utf-8

from django.test import TestCase

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_status_200(self):
        """Deve retornar o status 200 ao acessar a página inicial"""
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        """Deve utilizar o template index.html ao acessar a página inicial"""
        self.assertTemplateUsed(self.response, 'index.html')