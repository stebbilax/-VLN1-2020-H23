class Customer:
    """
    Model class for customer
    """
    def __init__(self,name,ssn,address,postnumber,phone,email,country):
        self.name = name 
        self.ssn = ssn
        self.address = address
        self.postnumber = postnumber
        self.phone = phone
        self.email = email
        self.country  = country
        #self.people = [].append([self.name,self.ssn,self.address,self.postnumber,self.phone,self.email,self.country])

    def __str__(self):
        return f'{self.name},{self.ssn},{self.address},{self.postnumber},{self.phone},{self.email},{self.country}'  

    def set_name (self,name):
        self.name = name
    
    def set_ssn (self,ssn):
        self.ssn = ssn

    def set_address(self, address):
        self.address = address
    
    def set_postnumer(self,postnumber):
        self.postnumber = postnumber

    def set_phone(self,phone):
        self.phone = phone

    def set_email(self,email):
        self.email = email

    def set_country(self,country):
        self.country = country


            


        
        



