class BlikError(RuntimeError):
    pass


class BlikUnauthorized(BlikError):
    pass


class BlikInvalid(BlikError):
    pass


class PaymentRejected(BlikError):
    pass
