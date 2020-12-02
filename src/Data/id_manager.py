import csv

class id_manager:
    def __init__(self):
        self.contract_ids = [0]
        self.customer_ids = [0]
        self.destination_ids = [0]
        self.employee_ids = [0]
        self.vehicle_ids = [0]
        self.vehicle_type_ids = [0]
        self.fields = [
            (self.contract_ids,'contract'), 
            (self.customer_ids,'customer'), 
            (self.destination_ids,'destination'), 
            (self.employee_ids,'employee'), 
            (self.vehicle_ids,'vehicle'), 
            (self.vehicle_type_ids,'vehicle_type')
            ]
        self.field_names = ['contract','customer','destination','employee','vehicle','vehicle_type']
        self.field_values = [self.contract_ids, self.customer_ids, self.destination_ids, 
                            self.employee_ids, self.vehicle_ids, self.vehicle_type_ids]
        


    # Need to change os to be modular
    # def write(self):
    #     import os
    #     curDir = os.getcwd()
    #     #################
    #     with open(f'{curDir}/Data/data/ids.txt', 'w', newline='', encoding='utf-8') as f:
    #         for field in self.fields:
    #             for id in field[0]:
    #                 f.write(str(id))
    #                 f.write(',')
    #             f.write('\n')

    def write(self):
        import os
        curDir = os.getcwd()
        #################
        with open(f'{curDir}/Data/data/ids.txt', 'w', newline='', encoding='utf-8') as f:
            for i in self.contract_ids:
                f.write(str(i))
                f.write(',')
            f.write('\n')
            for i in self.customer_ids:
                f.write(str(i))
                f.write(',')
            f.write('\n')
            for i in self.destination_ids:
                f.write(str(i))
                f.write(',')
            f.write('\n')
            for i in self.employee_ids:
                f.write(str(i))
                f.write(',')
            f.write('\n')
            for i in self.vehicle_ids:
                f.write(str(i))
                f.write(',')
            f.write('\n')
            for i in self.vehicle_type_ids:
                f.write(str(i))
                f.write(',')
            f.write('\n')



            # print(self.contract_ids)  
            # print(self.customer_ids)
            # print(self.destination_ids) 
            # print(self.employee_ids) 
            # print(self.vehicle_ids) 
            # print(self.vehicle_type_ids)


    def read(self):
        import os
        curDir = os.getcwd()
        file = None
        #################
        f = open(f'{curDir}/Data/data/ids.txt', 'r', newline='', encoding='utf-8')
        file = f.readlines()
        file = [x.strip() for x in file]
        self.contract_ids = [int(x) for x in file[0].replace(',', '')]
        self.customer_ids = [int(x) for x in file[1].replace(',', '')]
        self.destination_ids = [int(x) for x in file[2].replace(',', '')]
        self.employee_ids = [int(x) for x in file[3].replace(',', '')]
        self.vehicle_ids = [int(x) for x in file[4].replace(',', '')]
        self.vehicle_type_ids = [int(x) for x in file[5].replace(',', '')]
        
        f.close()
                

    def make_new_id(self, type):
        self.read()
        id_catagory = self.get_type(type)
        new_id = id_catagory[-1]+1
        id_catagory.append(new_id)
        self.set_type(type, id_catagory)

        self.write()
        return new_id


    def get_type(self, type):
        if type == 'contract': return self.contract_ids
        if type == 'customer': return self.customer_ids
        if type == 'destination': return self.destination_ids
        if type == 'employee': return self.employee_ids
        if type == 'vehicle': return self.vehicle_ids
        if type == 'vehicle_type': return self.vehicle_type_ids

    
    
    def set_type(self, type, arr):
        
        if type == 'contract': self.contract_ids = arr
        if type == 'customer': self.customer_ids = arr
        if type == 'destination': self.destination_ids = arr
        if type == 'employee': self.employee_ids = arr
        if type == 'vehicle': self.vehicle_ids = arr
        if type == 'vehicle_type': self.vehicle_type_ids = arr






# contract,customer,destination,employee,vehicle,vehicle_type