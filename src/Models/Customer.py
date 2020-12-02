class Customer:
    """
    Model class for customer
    """
    def __init__(self,name,ssn,address,postal_code,phone,email,country,licence,id=None):
        self.name = name 
        self.ssn = ssn
        self.address = address
        self.postal_code = postal_code
        self.phone = phone
        self.email = email
        self.country = country
        self.licence = licence #this is drivers licence 
        self.id = id
        #self.people = [].append([self.name,self.ssn,self.address,self.postal_code,self.phone,self.email,self.country])

    def __str__(self):
        return f'{self.name}, {self.ssn}, {self.address}, {self.postal_code}, {self.phone}, {self.email}, {self.country}'  

    def __dict__(self):
        return {
            'name' : self.name, 
            'ssn' : self.ssn,
            'address' : self.address,
            'postal_code' : self.postal_code,
            'phone' : self.phone,
            'email' : self.email,
            'country'  : self.country,
            'licence' : self.licence,
            'id': self.id
        }


    def set_name (self,name):
        self.name = name
    
    def set_ssn (self,ssn):
        self.ssn = ssn

    def set_address(self, address):
        self.address = address
    
    def set_postal_code(self,postal_code):
        self.postal_code = postal_code

    def set_phone(self,phone):
        self.phone = phone

    def set_email(self,email):
        self.email = email

    def set_country(self,country):
        self.country = country


            


        
        



