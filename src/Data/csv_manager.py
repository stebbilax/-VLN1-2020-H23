import csv
from configparser import ConfigParser

file = 'Data/config.ini'
config = ConfigParser()
config.read(file)

contract_fields = config['fields']['contract_fields'].split(',')
customer_fields = config['fields']['customer_fields'].split(',')
destination_fields = config['fields']['destination_fields'].split(',')
employee_fields = config['fields']['employee_fields'].split(',')
vehicle_fields = config['fields']['vehicle_fields'].split(',')
vehicle_type_fields = config['fields']['vehicle_type_fields'].split(',')



class Csv_Manager:
    def __init__(self, directory):
        self.directory = directory
        self.contract_fields = None
        self.customer_fields = None
        self.destination_fields = None
        self.employee_fields = None
        self.vehicle_fields = None
        self.vehicle_type_fields = None
        
        self.setup_config()


    # Get csv fields from config file
    def setup_config(self):
        file = 'Data/config.ini'
        config = ConfigParser()
        config.read(file)

        self.contract_fields = config['fields']['contract_fields'].split(',')
        self.customer_fields = config['fields']['customer_fields'].split(',')
        self.destination_fields = config['fields']['destination_fields'].split(',')
        self.employee_fields = config['fields']['employee_fields'].split(',')
        self.vehicle_fields = config['fields']['vehicle_fields'].split(',')
        self.vehicle_type_fields = config['fields']['vehicle_type_fields'].split(',')


    # Return filename and appropriate fields based on a name
    def get_name_and_fields(self, name):
        if name == 'contract': return ('contracts.csv', self.contract_fields)
        if name == 'customer': return ('customers.csv', self.customer_fields)
        if name == 'destination': return ('destinations.csv', self.destination_fields)
        if name == 'employee': return ('employees.csv', self.employee_fields)
        if name == 'vehicle': return ('vehicles.csv', self.vehicle_fields)
        if name == 'vehicle_type': return ('vehicle_types.csv', self.vehicle_type_fields)


    # Possible names are in function above
    def write_all(self, data, name):
        name, fields = self.get_name_and_fields(name)
        with open(f'{self.directory}/data/{name}', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for obj in data:
                line_obj = obj.__dict__()
                writer.writerow(line_obj)



    # def read_all(self):
    #     print('read all')

