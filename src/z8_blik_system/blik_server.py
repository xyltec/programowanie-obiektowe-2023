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

    def login(self, account_id: AccountId, password: str) -> AuthCode:
        pass

    def generate_blik_code(self, auth_code: AuthCode) -> BlikClientVersion:
        pass

    def make_payment(self, receipent_account_id: AccountId, blik_code: str, amount: float, title: str) -> str:
        pass

    def confirm_payment(self, blik_code: str, auth_code: AuthCode):
        pass





