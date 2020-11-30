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
    def __init__(self, country, airport, phonenumber, opening_hours):
        self.country = Country(country).name
        self.airport = Airport(airport).name
        self.phonenumber = phonenumber
        self.opening_hours = opening_hours
    
    def __str__(self):
        return "{:10} {:12} {:15} {:10}".format(self.country, self.airport, self.phonenumber, self.opening_hours)
    
    
    def set_country(self, country):
        self.country = country
    
    def set_airport(self, airport):
        self.airport = airport
        
    def set_phonenumber(self, phonenumber):
        self.phonenumber = phonenumber
        
    def set_opening_hours(self, opening_hours):
        self.opening_hours = opening_hours