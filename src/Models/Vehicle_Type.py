class Vehicle_Type:
    def __init__(self, type, airport, rate, id=None):
        self.type = type
        self.airport = airport
        self.rate = rate
        self.id = id

    def __str__(self):
        return f'{self.name}, {self.airport}, {self.rate}'

    def fields(self):
        return [property for property, value, in vars(self).items()]

    def set_name(self, name):
        self.name = name

    def set_regions(self, regions):
        self.regions = regions

    def set_rate(self, rate):
        self.rate = rate