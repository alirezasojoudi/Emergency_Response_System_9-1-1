from project.models.person import Person
from project.models.caller import Caller
from project.models.emergency_request import EmergencyRequest

from project.models.police_service import PoliceService
from project.models.ambulance_service import AmbulanceService
from project.models.fire_service import FireService


print("===== EMERGENCY RESPONSE SYSTEM TEST =====")


print("\n1. Testing Person")

person = Person("Ali", "09123456789")

print("Name:", person.name)
print("Phone:", person.phone)


print("\n2. Testing Caller")

caller = Caller("Ali", "09123456789")

print("Name:", caller.name)
print("Phone:", caller.phone)


print("\n3. Testing EmergencyRequest")

request = EmergencyRequest(
    caller,
    "Tehran",
    "Emergency situation",
    "Police"
)

print(request.get_request_info())


print("\n4. Testing PoliceService")

police = PoliceService()
police.dispatch(request)


print("\n5. Testing AmbulanceService")

ambulance = AmbulanceService()

ambulance_request = EmergencyRequest(
    caller,
    "Tehran",
    "Car accident",
    "Ambulance"
)

ambulance.dispatch(ambulance_request)


print("\n6. Testing FireService")

fire = FireService()

fire_request = EmergencyRequest(
    caller,
    "Tehran",
    "Building fire",
    "Fire Station"
)

fire.dispatch(fire_request)


print("\n===== ALL TESTS COMPLETED =====")