import csv

class id_manager:
    def __init__(self):
        self.contract_ids = [1, 2, 3]
        self.customer_ids = [1, 2, 3]
        self.destination_ids = [1, 2, 3]
        self.employee_ids = [1, 2, 3]
        self.vehicle_ids = [1, 2, 3]
        self.vehicle_type_ids = [1, 2, 3]
        self.fields = [
            (self.contract_ids,'contract'), 
            (self.customer_ids,'customer'), 
            (self.destination_ids,'destination'), 
            (self.employee_ids,'employee'), 
            (self.vehicle_ids,'vehicle'), 
            (self.vehicle_type_ids,'vehicle_type')
            ]
        self.field_names = ['contract','customer','destination','employee','vehicle','vehicle_type']
        


    # Need to change os to be modular
    def write(self):
        import os
        curDir = os.getcwd()
        #################
        with open(f'{curDir}/Data/data/ids.txt', 'w', newline='', encoding='utf-8') as f:
            for field in self.fields:
                for id in field[0]:
                    f.write(str(id))
                f.write('\n')
   


i = id_manager()
i.write()

# contract,customer,destination,employee,vehicle,vehicle_type