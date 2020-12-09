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

    def set_type(self,Type):
        self.type = Type

    def set_manufacturer(self, Manufacturer):
        self.manufacturer = Manufacturer

    def set_yom(self, YOM):
        self.yom = YOM

    def set_color(self, Color):
        self.color = Color

    def set_licence(self, licence):
        self.licence = licence

    def set_airport(self, Airport):
        self.airport = Airport

    def set_condition(self, Condition):
        self.condition = Condition

    def set_model(self, Model):
        self.model = Model

    def set_vehicle_id(self, vehicle_authentication):
        self.vehicle_id = vehicle_authentication

        