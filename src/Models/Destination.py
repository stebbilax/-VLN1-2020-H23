class Destination:
    def __init__(self, destination_name, destination_airport, phone, opening_hours, id=None):
        self.destination_name = destination_name
        self.destination_airport = destination_airport
        self.phone = phone
        self.opening_hours = opening_hours
        self.id = id
    
    def __str__(self):
        return "{:10} {:12} {:15} {:10}".format(self.destination_name, self.destination_airport, self.phone, self.opening_hours)
    
    def fields(self):
        return [property for property, value, in vars(self).items()]
