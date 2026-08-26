from project.models.emergency_service import EmergencyService
from project.tools.logger import Logger


class PoliceService(EmergencyService):
    def dispatch(self, request):
        logger = Logger()

        print("Dispatching Police Service")


