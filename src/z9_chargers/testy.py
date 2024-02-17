import unittest
from main import Charger, ChargingService, ChargerStatus, ChargingStatus, ClientAccount, Car, ChargingSession

class TestChargingService(unittest.TestCase):

    def setUp(self):
        self.charger1 = Charger(max_current_kw=50)
        self.charger2 = Charger(max_current_kw=100)

        self.charging_service = ChargingService(time_modifier=3600)  # in hours
        self.charging_service.attach_charger(self.charger1)
        self.charging_service.attach_charger(self.charger2)

    def test_start_charging_successful(self):
        session, charging_time_seconds = self.charging_service.start_charging(
            client_id="client1", vin="car1", kwh=30, desired_current_kw=40, charger_position=0
        )
        self.assertIsNotNone(session)
        self.assertIsNotNone(charging_time_seconds)
        self.assertEqual(self.charger1.status, ChargerStatus.CHARGING)

    def test_start_charging_unsuccessful_due_to_busy_charger(self):
        self.charger1.status = ChargerStatus.CHARGING

        session, charging_time_seconds = self.charging_service.start_charging(
            client_id="client1", vin="car1", kwh=30, desired_current_kw=40, charger_position=0
        )
        self.assertIsNone(session)
        self.assertIsNone(charging_time_seconds)

    def test_start_charging_unsuccessful_due_to_insufficient_current(self):
        session, charging_time_seconds = self.charging_service.start_charging(
            client_id="client1", vin="car1", kwh=30, desired_current_kw=120, charger_position=0
        )
        self.assertIsNone(session)
        self.assertIsNone(charging_time_seconds)
     def test_stop_charging_successful(self):
        session, charging_time_seconds = self.charging_service.start_charging(
            client_id="client1", vin="car1", kwh=30, desired_current_kw=40, charger_position=0
        )

        success = self.charging_service.stop_charging(client_id="client1", vin="car1")
        self.assertTrue(success)
        self.assertEqual(self.charger1.status, ChargerStatus.FREE)
        self.assertIsNone(self.charger1.attached_car_vin)

    def test_stop_charging_unsuccessful_due_to_nonexistent_vin(self):
        success = self.charging_service.stop_charging(client_id="client1", vin="nonexistent_car")
        self.assertFalse(success)

    def test_disable_charger(self):
        self.charging_service.disable_charger(charger_position=0)
        self.assertEqual(self.charger1.status, ChargerStatus.ERROR)

    def test_enable_charger(self):
        self.charging_service.disable_charger(charger_position=0)

        self.charging_service.enable_charger(charger_position=0)
        self.assertEqual(self.charger1.status, ChargerStatus.FREE)

    def test_remove_charger(self):
        self.charging_service.remove_charger(self.charger1)
        self.assertNotIn(self.charger1, self.charging_service.chargers)

if __name__ == '__main__':
    unittest.main()
