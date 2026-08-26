from project.models.person import Person

class Caller(Person):
    def __init__(self,name,phone):
        super().__init__(name,phone)