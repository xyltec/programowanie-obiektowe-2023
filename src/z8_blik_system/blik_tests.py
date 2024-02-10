import unittest
from time import sleep

from blik_server import *
from errors import *


class BlikTests(unittest.TestCase):

    def setUp(self):
        self.server = BlikServer(token_expiry_ms=10)

    # "fixtures"
    def user(self) -> tuple[AuthCode, AccountId]:
        account_id = self.server.create_account('kadabra')
        auth_token = self.server.login(account_id, 'kadabra')
        return auth_token, account_id

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
        auth_token, account_id = self.user()

        self.server.deposit_funds(auth_token, amount=100)

        funds = self.server.get_funds(auth_token)
        self.assertEquals(funds, 100)

    def test_can_generate_blik_code(self):
        auth_token, account_id = self.user()

        blik = self.server.generate_blik_code(auth_token)

        self.assertIsNotNone(blik)
        self.assertEquals(self.server.get_blik_status(blik.code, auth_token), BlikStatus.CREATED)

    def test_can_make_payment(self):
        auth_token, account_id1 = self.user()
        auth_token_2, account_id2 = self.user()

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

    def test_blik_token_expires(self):
        auth_token, account_id = self.user()

        blik = self.server.generate_blik_code(auth_token)
        validity = self.server.get_token_expiry_ms()
        sleep(validity + 0.01)

        self.assertEquals(self.server.get_blik_status(blik.code, auth_token), BlikStatus.EXPIRED)

    def test_cannot_user_used_blik_code(self):
        auth_token, account_id1 = self.user()
        auth_token_2, account_id2 = self.user()

        blik = self.server.generate_blik_code(auth_token)
        payment_id = self.server.make_payment(receipent_account_id=account_id2, blik_code=blik.code, amount=10,
                                              title='test payment')

        # this one should raise
        with self.assertRaises(BlikInvalid):
            self.server.make_payment(receipent_account_id=account_id2, blik_code=blik.code, amount=10,
                                     title='ha ha ha using same blik for 2nd time')

    def test_user_can_cancel_payment(self):
        auth_token, account_id1 = self.user()
        auth_token_2, account_id2 = self.user()

        blik = self.server.generate_blik_code(auth_token)
        payment_id = self.server.make_payment(receipent_account_id=account_id2, blik_code=blik.code, amount=10,
                                              title='test payment')

        # ACT
        self.server.cancel_payment(blik.code, auth_token)

        # ASSERT
        status = self.server.get_blik_status(blik.code, auth_token)
        self.assertEquals(status, BlikStatus.CANCELLED)
        payment_status = self.server.get_payment_status(payment_id, auth_token)
        self.assertEquals(payment_status, PaymentStatus.CANCELLED)

    def test_user_and_receipent_can_check_payment_status_but_not_3rd_persons(self):
        auth_token, account_id1 = self.user()
        auth_token_2, account_id2 = self.user()
        auth_token_3, account_id3 = self.user()

        blik = self.server.generate_blik_code(auth_token)
        payment_id = self.server.make_payment(receipent_account_id=account_id2, blik_code=blik.code, amount=10,
                                              title='test payment')

        # ACT
        payment_status = self.server.get_payment_status(payment_id, auth_token)  # blik owner
        payment_status = self.server.get_payment_status(payment_id, auth_token)  # receipent

        with self.assertRaises(BlikUnauthorized):
            payment_status = self.server.get_payment_status(payment_id, auth_token_3)  # receipent


if __name__ == '__main__':
    unittest.main()
