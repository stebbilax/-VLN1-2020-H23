class Contract:
    def __init__(self, 
        vehicle_id,vehicle_state,vehicle_status,vehicle_licence,country,
        customer_id,customer_name,phone,email,address,customer_licence,
        employee_id,date_of_handover,date_of_return,contract_start,
        contract_end,state,rate,late_fee,total_price,
        id=None):

        self.vehicle_id = vehicle_id
        self.vehicle_state = vehicle_state      # OK / DEFECTIVE
        self.vehicle_status = vehicle_status    # On Loan / Available
        self.vehicle_licence = vehicle_licence
        self.country = country

        self.customer_id = customer_id
        self.customer_name = customer_name
        self.phone = phone
        self.email = email
        self.address = address
        self.customer_licence = customer_licence

        self.employee_id = employee_id
        self.date_of_handover = date_of_handover
        self.date_of_return = date_of_return        # Day of return, registered on return
        self.contract_start = contract_start        # Day of contract creation
        self.contract_end = contract_end            # Expiration date for return
        self.state = state                          # Valid / Invalid / Completed
        self.rate = rate
        self.late_fee = late_fee
        self.total_price = total_price
        self.id = id


    def __str__(self):
        return f'Contract Nr.{self.id}'
    
    def __dict__(self):
        return {
           'vehicle_id' : self.vehicle_id,  
           'vehicle_state' : self.vehicle_state,  
           'vehicle_status' : self.vehicle_status,  
           'vehicle_licence' : self.vehicle_licence,  
           'country' : self.country, 

           'customer_id' : self.customer_id,
           'customer_name' : self.customer_name,  
           'phone' : self.phone,  
           'email' : self.email,  
           'address' : self.address, 
           'customer_licence' : self.customer_licence,  

           'employee_id' : self.employee_id,  
           'date_of_handover' : self.date_of_handover,  
           'date_of_return' : self.date_of_return,   
           'contract_start' : self.contract_start,   
           'contract_end' : self.contract_end,       
           'state' : self.state,                     
           'rate' : self.rate,  
           'late_fee' : self.late_fee,  
           'total_price' : self.total_price,  
           'id' : self.id  
        }

    

