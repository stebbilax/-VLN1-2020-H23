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
           
 


    


