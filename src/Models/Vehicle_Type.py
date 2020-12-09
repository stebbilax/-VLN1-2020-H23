class Vehicle_Type:
    def __init__(self, type, airport, rate, id=None):
        self.type = type
        self.airport = airport
        self.rate = rate
        self.id = id

    def __str__(self):
        return f'{self.type}, {self.airport}, {self.rate}'

    def fields(self):
        return [property for property, value, in vars(self).items()]

