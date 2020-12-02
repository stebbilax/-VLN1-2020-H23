class Contract:
    def __init__(self, name, phone, address, email, date_from, date_to, vehicle_id, country, vehicle_status, employee_id, loan_date, return_date, total, loan_status, id=None):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email
        self.date_from = date_from
        self.date_to = date_to
        self.vehicle_id = vehicle_id
        self.country = country
        self.vehicle_status = vehicle_status
        self.employee_id = employee_id
        self.loan_date = loan_date
        self.return_date = return_date
        self.total = total
        self.loan_status = loan_status
        self.id = id

    
    def __str__(self):
        return f'{self.name}, {self.phone}, {self.address}, {self.email}, {self.date_from}, {self.date_to}, {self.vehicle_id}, {self.country}, {self.vehicle_status}, {self.employee_id}, {self.loan_date}, {self.return_date}, {self.total}, {self.loan_status}'
    

    def __dict__(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'address': self.address,
            'email': self.email,
            'date_from': self.date_from, 
            'date_to': self.date_to,
            'vehicle_id': self.vehicle_id,
            'country': self.country,
            'vehicle_status': self.vehicle_status,
            'employee_id': self.employee_id,
            'loan_date': self.loan_date,
            'return_date': self.return_date,
            'total': self.total,
            'loan_status': self.loan_status,
            'id': self.id
        }


    def set_name(self, name):
        self.name = name
    
    def set_phone(self, phone):
        self.phone = phone
    
    def set_address(self, address):
        self.address = address
    
    def set_email(self, email):
        self.email = email
    
    def set_date_from(self, date_from):
        self.date_from = date_from

    def set_date_to(self, date_to):
        self.date_to = date_to

    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id
    
    def set_country(self, country):
        self.country = country
    
    def set_vehicle_status(self, vehicle_status):
        self.vehicle_status = vehicle_status
    
    def set_employee_id(self, employee_id):
        self.employee_id = employee_id
    
    def set_loan_date(self, loan_date):
        self.loan_date = loan_date
    
    def set_return_date(self, return_date):
        self.return_date = return_date
    
    def set_total(self, total):
        self.total = total
    
    def set_loan_status(self, loan_status):
        self.loan_status = loan_status
