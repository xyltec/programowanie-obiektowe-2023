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

class ChargingService:
    def __init__(self, time_modifier):
        self.chargers = []
        self.time_modifier = time_modifier

    def start_charging(self, client_id, vin, kwh, desired_current_kw, charger_position):
        charger = self.chargers[charger_position]
        if charger.status == ChargerStatus.FREE and charger.max_current_kw >= desired_current_kw:
            charger.attached_car_vin = vin
            charger.status = ChargerStatus.CHARGING
            charging_time_seconds = kwh / desired_current_kw * self.time_modifier
            return ChargingSession(csid=client_id, status=ChargingStatus.OPEN, current_kw=desired_current_kw,
                                   total_kwh=kwh), charging_time_seconds
        else:
            return None, None

    def stop_charging(self, client_id, vin):
        for charger in self.chargers:
            if charger.attached_car_vin == vin:
                charger.status = ChargerStatus.FREE
                charger.attached_car_vin = None
                return True
        return False

    def attach_charger(self, charger):
        self.chargers.append(charger)

    def disable_charger(self, charger_position):
        self.chargers[charger_position].status = ChargerStatus.ERROR

    def enable_charger(self, charger_position):
        self.chargers[charger_position].status = ChargerStatus.FREE

    def remove_charger(self, charger):
        self.chargers.remove(charger)


if __name__ == "__main__":

    charger1 = Charger(max_current_kw=50)
    charger2 = Charger(max_current_kw=100)

    charging_service = ChargingService(time_modifier=3600)  # godziny

    charging_service.attach_charger(charger1)
    charging_service.attach_charger(charger2)

    # rozpoczęcie ładowania
    session, charging_time_seconds = charging_service.start_charging(client_id="client1", vin="car1", kwh=30,
                                                                 desired_current_kw=40, charger_position=0)
    if session:
        print("Sesja ładowania rozpoczęta. Szacowany czas ładowania:", charging_time_seconds, "sekund")


    stop_charging = charging_service.stop_charging(client_id="client1", vin="car1")
    if stop_charging:
        print("Ładowanie zostało zatrzymane.")
