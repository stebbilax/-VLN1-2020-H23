from random import randint, choice
import datetime
from string import ascii_uppercase as AU

class Dummy:
    def make_name(self):
        names = ['Liam','Olivia','Noah','Emma','Oliver','Ava','William','Sophia','Elijah','Isabella',
        'James','Charlotte','Benjamin','Amelia','Lucas','Mia','Mason','Harper','Ethan','Evelyn']
        return choice(names)


    def make_phone(self):
        return f'{randint(6,9)}{randint(6,9)}{randint(0,9)}-{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}'

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
        return choice(['Iceland', 'Greenland', 'Svalbard', 'Farao Islands', 'Shetland'])

    def make_vehicle_state(self):
        return choice(['OK', 'DEFECTIVE'])

    def make_vehicle_status(self):
        return choice(['Unavailable', 'Available'])

    def make_contract_state(self):
        return choice(['Valid', 'Invalid', 'Completed'])

    def make_employee_id(self):
        return f'{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}'

    def make_total(self):
        return randint(200, 4000)

    def make_loan_status(self):
        return choice(['LATE', 'OK', 'RETURNED'])

    def make_ssn(self):
        return f'{randint(10, 12)}{randint(10, 12)}{randint(50, 90)}-{randint(10, 90)}{randint(10, 90)}'

    def make_postal_code(self):
        return f'{randint(1,9)}{randint(1,9)}{randint(1,9)}'

    def make_airport(self):
        return choice(['reykjavik', 'nuuk', 'kulusk', 'tingwall', 'tingwall', 'longyearbyen', 'torshavn'])

    def make_opening_hours(self):
        return '10:00-15:30'

    def make_title(self):
        return choice(['airport', 'office'])

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
        return choice(['None', 'Drivers licence', 'Im amazing licence'])

    def make_model(self):
        return choice(['Free Fly II', 'Crazy', 'Fat Max'])
