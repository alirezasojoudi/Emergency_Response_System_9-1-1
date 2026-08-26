import re

class Validator:

    @staticmethod
    def location_validator(location, fail_message):
        if re.match(r"^[\sa-zA-Z]{3,50}$", location):
            return location
        else:
            raise ValueError(fail_message)

    @staticmethod
    def en_name_validator(name, fail_message):
        if re.match(r"^[\sa-zA-Z]{3,30}$", name):
            return name
        else:
            raise ValueError(fail_message)

    @staticmethod
    def phone_validator(phone, message):
        if re.match(r"^(\+989|09)\d{9}$", phone):
            return phone
        else:
            raise ValueError(message)