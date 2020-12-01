from enum import Enum

class Airport(Enum):
    reykjavik = 1
    nuuk = 2
    kulusk = 3
    tingwall = 4
    longyearbyen = 5
    torshavn = 6


class Title(Enum):
    office = 1
    airport = 2


class Country(Enum):
    iceland = 1
    greenland = 2
    shetland = 3
    svalbard = 4
    faroe_islands = 5

class Employee:
    '''
    Class Employee

    Attributes:
    -   name            (string)
    -   address         (string)
    -   postal_code     (int)
    -   ssn             (string)
    -   phone           (string)
    -   mobile_phone    (string)
    -   email           (string)
    -   title           (enum)
    -   location        (enum)
    -   country         (enum)

    Methods:
    -   set_name(name)
    -   set_address(address)
    -   set_postal_code(postal_code)
    -   set_phone(phone)
    -   set_mobile_phone(mobile_phone)
    -   set_email(email)
    -   set_location(location)
    -   set_title(title)
    -   set_country(country)

    Enums:
    -   Location
        *   Reykjavik       - 1
        *   Nuuk            - 2
        *   Kulusk          - 3
        *   Tingwall        - 4
        *   Longyearbyen    - 5
        *   Torshavn        - 6

    -   Title
        *   Office          - 1
        *   Airport         - 2

    -   Country
        *   Iceland         - 1
        *   Greenland       - 2
        *   Shetland        - 3
        *   Svalbard        - 4
        *   Faroe Islands   - 5
    '''

    def __init__(self, name, address, postal_code, ssn, phone, mobile_phone, email, title, airport, country):
        self.name = name
        self.address = address
        self.postal_code = postal_code
        self.ssn = ssn
        self.phone = phone
        self.mobile_phone = mobile_phone
        self.email = email
        self.title = Title(int(title)).name
        self.airport = Airport(int(airport)).name
        self.country = Country(int(country)).name

    def __str__(self):
        return f'{self.name}, {self.address}, {self.postal_code}, {self.ssn}, {self.phone}, {self.mobile_phone}, {self.email}, {self.title}, {self.airport}, {self.country}'

    def __dict__(self):
        return {
            'name' : self.name,
            'address' : self.address,
            'postal_code' : self.postal_code,
            'ssn' : self.ssn,
            'phone' : self.phone,
            'mobile_phone' : self.mobile_phone,
            'email' : self.email,
            'title' : self.title,
            'airport' : self.airport,
            'country' : self.country
        }
           
    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_postal_code(self, postal_code):
        self.postal_code = postal_code

    def set_phone(self, phone):
        self.phone = phone

    def set_mobile_phone(self, mobile_phone):
        self.mobile_phone = mobile_phone

    def set_email(self, email):
        self.email = email

    def set_airport(self, airport):
        self.airport = Airport(int(airport)).name
        
    def set_title(self, title):
        self.title = Title(int(title)).name

    def set_country(self, country):
        self.country = Country(int(country)).name


    
# e = Employee('Chuck Norris', 'Svarthöfða 1', '110', '250645-9999', '+354 5555555', '+354 6890001', 'bigc@nan.is', 1, 2, 5)


