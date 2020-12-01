class Vehicle_Type:
    def __init__(self, name, regions, rate):
        self.name = name
        self.regions = regions
        self.rate = rate

    def __str__(self):
        return f'{self.name}, {self.regions}, {self.rate}'


    def __dict__(self):
        return {
            'name' : self.name,
            'regions' : self.regions,
            'rate' : self.rate
        }

    def set_name(self, name):
        self.name = name

    def set_regions(self, regions):
        self.regions = regions

    def set_rate(self, rate):
        self.rate = rate