from random import randint, choice
import datetime
from string import ascii_uppercase as AU

class Dummy:
    """Makes dummy data for csv documents"""
    def __init__(self):
        self.job = ''
        self.airport = ''
        self.country = ''
        self.state = ''

    def make_name(self):
        names = ['Liam','Olivia','Noah','Emma','Oliver','Ava','William','Sophia','Elijah','Isabella',
        'James','Charlotte','Benjamin','Amelia','Lucas','Mia','Mason','Harper','Ethan','Evelyn']
        return choice(names)


    def make_phone(self):
        return f'{randint(6,9)}{randint(6,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}'

    def make_address(self):
        l = ['Street','Town','Road', 'Square']
        return f'{self.make_name()}{choice(l)} {randint(0, 30)}'

    def make_email(self):
        return f'{self.make_name()}@nan.is'

    def make_early_date(self):
        return datetime.date(2020, randint(1,2), randint(1,5))

    def make_later_date(self):
        return datetime.date(2020, 2, randint(5,10))

    def make_vehicle_id(self):
        return f'{choice(AU)}{choice(AU)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'

    def make_country(self):
        self.country =choice(['Iceland', 'Greenland', 'Svalbard', 'Farao Islands', 'Shetland'])
        return self.country


    def make_country_after_airport(self):
        if self.airport == 'reykjavik':
            return 'Iceland'
        if self.airport == 'nuuk' or self.airport =='kulusuk':
            return 'Greenland'
        if self.airport == 'longyearbyen':
            return 'Svalbard'
        if self.airport == 'torshavn':
            return 'Farao Islands'
        if self.airport ==  'tingwall':
            return 'Shetland'

    def make_vehicle_state(self):
        self.state = choice(['OK'])
        return self.state

    def make_vehicle_status(self):
        if self.state == 'OK':
            return choice(['Available'])
        else:
            return 'Unavailable'

    def make_contract_state(self):
        return choice(['Valid'])

    def make_employee_id(self):
        return f'{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}'

    def make_total(self):
        return randint(200, 4000)

    def make_loan_status(self):
        return choice(['OK'])

    def make_ssn(self):
        return f'{randint(10, 12)}{randint(10, 12)}{randint(50, 90)}-{randint(10, 90)}{randint(10, 90)}'

    def make_postal_code(self):
        return f'{randint(1,9)}{randint(1,9)}{randint(1,9)}'

    def make_airport(self):
        return choice(['reykjavik', 'nuuk', 'kulusuk', 'tingwall', 'longyearbyen', 'torshavn'])
    
    def make_airport_after_title(self):
        if self.job == 'office':
            self.airport = 'reykjavik'
            return self.airport
        elif self.job == 'airport':
            self.airport = choice(['reykjavik', 'nuuk', 'kulusuk', 'tingwall', 'longyearbyen', 'torshavn'])
            return self.airport

    
    def make_airport_after_country(self):
        if self.country =='Iceland' :
            return 'reykjavik'
        if self.country == 'Greenland' :
            self.airport = choice(['nuuk','kulusuk'])
            return self.airport
        if self.country == 'Svalbard':
            return 'longyearbyen'
        if self.country == 'Farao Islands':
            return 'torshavn'
        if self.country == 'Shetland':
            return 'tingwall'


    def make_opening_hours(self):
        return '10:00-15:30'

    def make_title(self):
        self.job = choice(['airport', 'office'])
        return self.job

    def make_id(self):
        return randint(1, 999)




    # VEHICLES
    def make_type(self):
        return choice(['Light road', 'Light off-road', 'Light water', 'Medium off-road', 'Medium water'])

    def make_manufacturer(self):
        return choice(['TAILG', 'Kayman Kayaks', 'Cani-Fit', 'Yedoo', 'WildChild'])

    def make_yom(self):
        return randint(1991, 2020)

    def make_color(self):
        return choice(['red', 'blue', 'green', 'grey', 'black'])

    def make_licence(self):
        return choice(['None', 'Drivers licence'])

    def make_model(self):
        return choice(['Free Fly II', 'Crazy', 'Fat Max'])
