class Vehicle:
    def __init__(self,Type, Manufacturer, YOM, Color, Req_Rights, Location, Condition, Model):
        self.type = Type
        self.manufacturer = Manufacturer
        self.yom = YOM
        self.color = Color
        self.req_rights = Req_Rights
        self.location = Location
        self.condition = Condition
        self.model = Model

    def set_type(self,Type):
        self.type = Type

    def set_manufacturer(self, Manufacturer):
        self.manufacturer = Manufacturer

    def set_yom(self, YOM):
        self.yom = YOM

    def set_color(self, Color):
        self.color = Color

    def set_req_rights(self, Req_Rights):
        self.req_rights = Req_Rights

    def set_location(self, Location):
        self.location = Location

    def set_condition(self, Condition):
        self.condition = Condition

    def set_model(self, Model):
        self.model = Model