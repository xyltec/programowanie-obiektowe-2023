import unittest
from blik_server import *


class BlikTests(unittest.TestCase):

    def setUp(self):
        self.server = BlikServer()

    def test_can_create_account(self):
        account_id = self.server.create_account('kadabra')
        # no exception thrown
        self.assertIsNotNone(account_id)

    def test_can_login(self):
        account_id = self.server.create_account('kadabra')
        auth_token = self.server.login(account_id, 'kadabra')
        # no exception thrown

        funds = self.server.get_funds(auth_token)
        self.assertEquals(funds, 0)

    def test_can_deposit_funds(self):
        account_id = self.server.create_account('kadabra')
        auth_token = self.server.login(account_id, 'kadabra')
        self.server.deposit_funds(auth_token, amount=100)

        funds = self.server.get_funds(auth_token)
        self.assertEquals(funds, 100)

    def test_can_generate_blik_code(self):
        account_id = self.server.create_account('kadabra')
        auth_token = self.server.login(account_id, 'kadabra')
        blik = self.server.generate_blik_code(auth_token)

        self.assertIsNotNone(blik)
        self.assertEquals(self.server.get_blik_status(blik.code, auth_token), BlikStatus.CREATED)

    def test_can_make_payment(self):
        account_id1 = self.server.create_account('kadabra')
        account_id2 = self.server.create_account('kadabra')

        auth_token = self.server.login(account_id1, 'kadabra')
        auth_token_2 = self.server.login(account_id2, 'kadabra')

        self.server.deposit_funds(auth_token, 100)
        self.assertEquals(self.server.get_funds(auth_code=auth_token), 100)
        self.assertEquals(self.server.get_funds(auth_code=auth_token_2), 0)

        blik = self.server.generate_blik_code(auth_token)
        self.assertEquals(self.server.get_blik_status(blik.code, auth_token), BlikStatus.CREATED)
        payment_id = self.server.make_payment(receipent_account_id=account_id2, blik_code=blik.code, amount=10,
                                              title='test payment')

        self.assertIsNotNone(payment_id)

        self.server.confirm_payment(blik_code=blik.code, auth_code=auth_token)
        self.assertEquals(self.server.get_blik_status(blik.code, auth_token), BlikStatus.USED)

        self.assertEquals(self.server.get_funds(auth_code=auth_token), 90)
        self.assertEquals(self.server.get_funds(auth_code=auth_token_2), 10)

