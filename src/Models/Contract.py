class Contract:
    def __init__(self, 
        vehicle_id,vehicle_state,vehicle_status,vehicle_licence,vehicle_type,
        country,customer_id,customer_name,phone,email,address,customer_licence,
        employee_id,location_handover,location_return,date_handover,
        date_return,time_handover,time_return,contract_start,contract_end,
        state,rate,late_fee,total_price,
        id=None):

        self.vehicle_id = vehicle_id
        self.vehicle_state = vehicle_state      # OK / DEFECTIVE
        self.vehicle_status = vehicle_status    # On Loan / Available
        self.vehicle_licence = vehicle_licence
        self.vehicle_type = vehicle_type
        self.country = country

        self.customer_id = customer_id
        self.customer_name = customer_name
        self.phone = phone
        self.email = email
        self.address = address
        self.customer_licence = customer_licence

        self.employee_id = employee_id
        self.location_handover = location_handover
        self.location_return = location_return
        self.date_handover = date_handover
        self.date_return = date_return        # Day of return, registered on return
        self.time_handover = time_handover
        self.time_return = time_return
        self.contract_start = contract_start        # Day of contract creation
        self.contract_end = contract_end            # Expiration date for return
        self.state = state                          # Valid / Invalid / Completed
        self.rate = rate
        self.late_fee = late_fee
        self.total_price = total_price
        self.id = id


    def __str__(self):
        return f'Contract Nr.{self.id}'

    def fields(self):
        return [property for property, value, in vars(self).items()]

