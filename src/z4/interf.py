# Interfaces

class UsbChargeProvider:
    def charge(self, mAh: float):
        raise NotImplementedError()


class LightningChargeProvider:
    def charge(self, mAh: float):
        raise NotImplementedError()


class UsbChargeableDevice:
    def acceptCharge(self, mAh: float):
        raise NotImplementedError()


class LightningChargeableDevice:
    def acceptCharge(self, mAh: float):
        raise NotImplementedError()


class UsbToLightningAdapter(UsbChargeableDevice, LightningChargeProvider):
    """
    An adapter which accepts Usb-C, and provides lightning output.
    """
    pass


# ----------------- True objects/classes

class Phone(UsbChargeableDevice):
    def __init__(self):
        self.battery_charge = 100

    def acceptCharge(self, mAh: float):
        self.battery_charge += mAh


class IPhone14(LightningChargeableDevice):

    def acceptCharge(self, mAh: float):
        pass


class StandardCharger(UsbChargeProvider):
    def charge(self, mAh: float):
        print(f'charging with {mAh=}')


class StandardAdaptor(UsbToLightningAdapter):

    def acceptCharge(self, mAh: float):
        print('connected to USB charger')

    def charge(self, mAh: float):
        print('charging Lightning device')


if __name__ == '__main__':
    charger = StandardCharger()
    adaptor = StandardAdaptor()
    phone = IPhone14()

    # teraz spróbujemy ładowania....
    charger.charge(10)
    adaptor.acceptCharge(10)
    adaptor.charge(10)
    phone.acceptCharge(10)



