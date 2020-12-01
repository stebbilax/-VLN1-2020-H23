class Vehicle:
    def __init__(self,Type, Manufacturer, YOM, Color, licence, Airport, Condition, Model):
        self.id = None
        self.type = Type
        self.manufacturer = Manufacturer
        self.yom = YOM
        self.color = Color
        self.licence = licence
        self.airport = Airport
        self.condition = Condition
        self.model = Model

    def __str__(self):
        return f'{self.type}, {self.manufacturer}, {self.yom}, {self.color}, {self.licence}, {self.airport}, {self.condition}, {self.model}'

    def __dict__(self):
        return {
            'type' : self.type,  
            'manufacturer' : self.manufacturer, 
            'yom' : self.yom, 
            'color' : self.color, 
            'licence' : self.licence, 
            'airport' : self.airport, 
            'condition' : self.condition,
            'model' : self.model 
        }
    

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
        self.airport = airport

    def set_condition(self, Condition):
        self.condition = Condition

    def set_model(self, Model):
        self.model = Model