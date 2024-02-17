# Charging station backend server


```
Model:

ClientAccount
- id
- name
- funds

Car
- vin
- total_charged_kwh
- max_current_kw

ChargingSession
- csid
- status
- current_kw
- total_kwh

ChargingStatus
- OPEN
- ERROR
- FINISHED

ChargingService
 - chargers: list[Charger]
 - time_modifier: float (for testing)

 - start_charging(client_id, vin, kwh, desired_current_kw, charger_position: int)
   # check if charger available and supports such desired_current

 - stop_charging(client_id, vin)   
 - attach_charger(charger)
 - disable_charger(charger_position:int)
 - engable_charger(charger_position:int)
 - remove_charger(charger)

Charger
 - max_current_kw
 - total_charged_kw
 - attached_car_vin 
 - status

ChargerStatus
- FREE
- CHARGING
- ERROR

... error codes...

```