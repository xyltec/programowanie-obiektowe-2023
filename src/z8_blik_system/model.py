from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class BlikStatus(Enum):
    CREATED = 1
    USED = 2
    CANCELLED = 3
    EXPIRED = 4


class PaymentStatus(Enum):
    UNCONFIRMED = 1
    CONFIRMED = 2
    CANCELLED = 3
    EXPIRED = 4


@dataclass
class AuthCode:
    code: str


@dataclass
class BlikCode:
    code: str
    status: BlikStatus
    created_at: datetime
    valid_thru: datetime
    updated_at: datetime
    owner_account_id: str


@dataclass
class BlikClientVersion:
    code: str
    valid_thru: datetime


@dataclass
class Payment:
    payment_id: str
    receipent_account_id: str
    source_account_id: str
    amount: float
    status: PaymentStatus
    created_at: datetime
    finalized_at: datetime
    title: str


@dataclass
class Account:
    account_id: str
    password_hash: str
    funds: float


if __name__ == '__main__':
    # st = BlikStatus.USED
    st = BlikStatus.EXPIRED
    print(st)
    if st == BlikStatus.EXPIRED:
        print('This token has expired')
