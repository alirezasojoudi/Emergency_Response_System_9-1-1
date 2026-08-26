from project.models.emergency_service import EmergencyService
from project.tools.logger import Logger


class AmbulanceService(EmergencyService):
    def dispatch(self, request):
        logger = Logger()

        print("Dispatching Ambulance Service")


