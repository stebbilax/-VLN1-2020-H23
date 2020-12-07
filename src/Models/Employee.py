class Employee:
    def __init__(self, name, address, postal_code, ssn, phone, mobile_phone, email, title, airport, country, id=None):
        self.name = name
        self.address = address
        self.postal_code = postal_code
        self.ssn = ssn
        self.phone = phone
        self.mobile_phone = mobile_phone
        self.email = email
        self.title = title
        self.airport = airport
        self.country = country
        self.id = id

    def __str__(self):
        return f'{self.name}, {self.address}, {self.postal_code}, {self.ssn}, {self.phone}, {self.mobile_phone}, {self.email}, {self.title}, {self.airport}, {self.country}'

    def fields(self):
        return [property for property, value, in vars(self).items()]
           
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
        self.airport = airport
        
    def set_title(self, title):
        self.title = title

    def set_country(self, country):
        self.country = country


    


