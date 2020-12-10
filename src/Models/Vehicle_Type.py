class Vehicle_Type:
    def __init__(self, type_name, airport, rate, id=None):
        self.type_name = type_name
        self.airport = airport
        self.rate = rate
        self.id = id

    def __str__(self):
        return f'{self.type_name}, {self.airport}, {self.rate}'

    def fields(self):
        return [property for property, value, in vars(self).items()]

