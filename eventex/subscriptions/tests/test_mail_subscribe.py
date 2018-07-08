from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

class SubscribeEmail(TestCase):

    def setUp(self):
        data = dict(name='André Menezes', cpf='12345678901', email='andrelfm@gmail.com', phone='34-98801-0797')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'andrelfm@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'André Menezes',
            '12345678901',
            'andrelfm@gmail.com',
            '34-98801-0797',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)