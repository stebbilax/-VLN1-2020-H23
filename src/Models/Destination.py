from enum import Enum

class Airport(Enum):
    reykjavik = 1
    nuuk = 2
    kulusk = 3
    tingwall = 4
    longyearbyen = 5
    torshavn = 6

class Country(Enum):
    iceland = 1
    greenland = 2
    shetland = 3
    svalbard = 4
    faroe_islands = 5


class Destinations:
    def __init__(self, country, airport, phone, opening_hours):
        self.country = Country(country).name
        self.airport = Airport(airport).name
        self.phone = phone
        self.opening_hours = opening_hours
    
    def __str__(self):
        return "{:10} {:12} {:15} {:10}".format(self.country, self.airport, self.phone, self.opening_hours)
    
    
    def __dir__(self):
        return {
            'country' : self.country,
            'airport' : self.airport,
            'phone' : self.phone,
            'opening_hours' : self.opening_hours
        }


    def set_country(self, country):
        self.country = country
    
    def set_airport(self, airport):
        self.airport = airport
        
    def set_phone(self, phone):
        self.phone = phone
        
    def set_opening_hours(self, opening_hours):
        self.opening_hours = opening_hours