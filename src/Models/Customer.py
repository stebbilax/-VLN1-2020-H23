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

    def fields(self):
        return [property for property, value, in vars(self).items()]



            


        
        



