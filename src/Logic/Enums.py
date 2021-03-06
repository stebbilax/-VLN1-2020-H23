from enum import Enum

class EnumManager:
    def __init__(self, dapi):
        self.dataAPI = dapi 
        self.generate_enums()

    def generate_enums(self):
        '''Keeps track of all registered countries and airports, providing
        enums with dynamically updated values'''
        
        #list containing all destinations
        destinations_list = self.dataAPI.read_all_destinations()

        # Initialize with basic locations and countries
        countries = set(['Svalbard', 'Shetland', 'Farao Islands', 'Iceland', 'Greenland'])
        airports = set(['nuuk', 'tingwall', 'kulusuk', 'longyearbyen', 'reykjavik', 'torshavn'])

        # Add any additional destinations
        for dest in destinations_list:
            v = vars(dest)
            countries.add(v['destination_name'])
            airports.add(v['destination_airport'])

        self.airport_enum = Enum('Airport', {key:i for (i, key) in enumerate(airports)})
        self.country_enum = Enum('Countries', {key:i for (i, key) in enumerate(countries)})
        self.title_enum = Enum('Titles', {'office' : 1, 'airport' : 2})

    def enum_to_regex(self, enum):
        ''' Converts an enum to a OR regex string '''


        s = '('
        for var in enum:
            s += var.name + '|'

        # Remove trailing OR
        s = s[:-1]

        s += ')'

        return s

    def enum_to_instructions(self, enum):
        ''' Converts an enum to instructions for forms '''

        s = "Must be one of the following: "

        for var in enum:
            s += var.name + ', '

        # Remove trailing whitespace and comma
        s = s[:-2]

        s += '.'

        return s