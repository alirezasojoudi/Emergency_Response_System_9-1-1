class EmergencyRequest:
    def __init__(self,caller,location,description,service_type):
        self.caller = caller
        self.location = location
        self.description = description
        self.service_type = service_type

    def get_request_info(self):
        return (
            f"New Request |"
            f"Service: {self.service_type} | "
            f"Name: {self.caller.name} | "
            f"Phone: {self.caller.phone} | "
            f"Location: {self.location} | "
            f"Description: {self.description}"
        )