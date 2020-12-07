class Destination:
    def __init__(self, country, airport, phone, opening_hours, id=None):
        self.country = country
        self.airport = airport
        self.phone = phone
        self.opening_hours = opening_hours
        self.id = id
    
    def __str__(self):
        return "{:10} {:12} {:15} {:10}".format(self.country, self.airport, self.phone, self.opening_hours)
    
    @staticmethod
    def fields(self):
        return [property for property, value, in vars(self).items()]

    def set_country(self, country):
        # self.country = Country(int(country)).name
        self.country = country
    
    def set_airport(self, airport):
        # self.airport = Airport(int(airport)).name
        self.airport = airport
        
    def set_phone(self, phone):
        self.phone = phone
        
    def set_opening_hours(self, opening_hours):
        self.opening_hours = opening_hours