class Vehicle:
    def __init__(self,type, manufacturer, yom, color, licence, airport, vehicle_state, vehicle_status, rate, model, vehicle_authentication, id=None):
        self.type = type
        self.manufacturer = manufacturer
        self.yom = yom
        self.color = color
        self.licence = licence
        self.airport = airport
        self.vehicle_state = vehicle_state
        self.vehicle_status = vehicle_status
        self.rate = rate
        self.model = model
        self.vehicle_authentication = vehicle_authentication
        self.id = id

    def __str__(self):
        return f'{self.type}, {self.manufacturer}, {self.yom}, {self.color}, {self.licence}, {self.airport}, {self.vehicle_state}, {self.model}'

    def fields(self):
        return [property for property, value, in vars(self).items()]
