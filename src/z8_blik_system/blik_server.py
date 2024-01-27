from model import *


class BlikServer:

    def __init__(self):
        self.accounts = dict()   # account_id -> Account
        self.blik_codes = dict()
        self.payments = dict()

    def create_account(self, password: str) -> AccountId:
        pass

    def deposit_funds(self, auth_code: AuthCode, amount: float):
        pass

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

    def get_payment_status(self, payment_id: str, auth_code: AuthCode):
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

    def make_payment(self, receipent_account_id: AccountId, blik_code: str, amount: float, title: str) -> str:
        """

        :param receipent_account_id:
        :param blik_code:
        :param amount:
        :param title:
        :return: payment_id
        """
        pass

    def confirm_payment(self, blik_code: str, auth_code: AuthCode):
        pass





