from model import *


class BlikServer:

    def __init__(self, token_expiry_ms: int = 90000):
        self.accounts = dict()  # account_id -> Account
        self.blik_codes = dict()
        self.payments = dict()
        self.token_expiry_ms = token_expiry_ms

    def create_account(self, password: str) -> AccountId:
        pass

    def deposit_funds(self, auth_code: AuthCode, amount: float):
        pass

    def get_token_expiry_ms(self) -> int:
        return self.token_expiry_ms

    def get_funds(self, auth_code: AuthCode) -> float:
        pass

    def get_blik_status(self, blik_code: str, auth_code: AuthCode) -> BlikStatus:
        """
        Returns blik status only if account associated with auth_code is the owner of the blik_code
        :param blik_code:
        :param auth_code:
        :return:
        """
        pass

    def get_payment_status(self, payment_id: UUID, auth_code: AuthCode):
        """
        Returns payment status only if account associated with auth_code is either the source, or the receipent of
        funds in the payment.
        :return:
        """
        pass

    def login(self, account_id: AccountId, password: str) -> AuthCode:
        pass

    def generate_blik_code(self, auth_code: AuthCode) -> BlikClientVersion:
        pass

    def make_payment(self, receipent_account_id: AccountId, blik_code: str, amount: float, title: str) -> UUID:
        """
        Action performed e.g. in a shop's terminal (receipent_account_id relates to shop's account in blik system).

        :param receipent_account_id:
        :param blik_code:
        :param amount:
        :param title:
        :return: payment_id UUID of the payment
        """
        pass

    def confirm_payment(self, blik_code: str, auth_code: AuthCode):
        """
        Action performed on blik-owner's mobile device.

        :param blik_code:
        :param auth_code:
        :return:
        """
        pass

    def cancel_payment(self, blik_code: str, auth_code: AuthCode):
        """
        Action performed on blik-owner's mobile device.
        BlikStatus -> CANCELLED
        PaymentStatus -> CANCELLED
        :param blik_code:
        :param auth_code:
        :return:
        """
        pass
