from project.models.emergency_service import EmergencyService
from project.tools.logger import Logger


class FireService(EmergencyService):
    def dispatch(self, request):
        logger = Logger()

        print("Dispatching Fire Service")

