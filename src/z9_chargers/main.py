class ChargingStatus:
    OPEN = "OPEN"
    ERROR = "ERROR"
    FINISHED = "FINISHED"


class ChargerStatus:
    FREE = "FREE"
    CHARGING = "CHARGING"
    ERROR = "ERROR"


class ClientAccount:
    def __init__(self, id, name, funds):
        self.id = id
        self.name = name
        self.funds = funds


class Car:
    def __init__(self, vin, total_charged_kwh, max_current_kw):
        self.vin = vin
        self.total_charged_kwh = total_charged_kwh
        self.max_current_kw = max_current_kw


class ChargingSession:
    def __init__(self, csid, status, current_kw, total_kwh):
        self.csid = csid
        self.status = status
        self.current_kw = current_kw
        self.total_kwh = total_kwh


class Charger:
    def __init__(self, max_current_kw):
        self.max_current_kw = max_current_kw
        self.total_charged_kw = 0
        self.attached_car_vin = None
        self.status = ChargerStatus.FREE
