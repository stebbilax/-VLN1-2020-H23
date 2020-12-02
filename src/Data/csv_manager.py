import csv
from configparser import ConfigParser
from Models.Contract import Contract
from Models.Customer import Customer
from Models.Destination import Destination
from Models.Employee import Employee
from Models.Vehicle import Vehicle
from Models.Vehicle_Type import Vehicle_Type
from Data.id_manager import id_manager


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


    def get_model(self, name):
        if name == 'contract': return Contract
        if name == 'customer': return Customer
        if name == 'destination': return Destination
        if name == 'employee': return Employee
        if name == 'vehicle': return Vehicle
        if name == 'vehicle_type': return Vehicle_Type


    # Return filename and appropriate fields based on a name
    def get_name_and_fields(self, name):
        if name == 'contract': return ('contracts.csv', self.contract_fields)
        if name == 'customer': return ('customers.csv', self.customer_fields)
        if name == 'destination': return ('destinations.csv', self.destination_fields)
        if name == 'employee': return ('employees.csv', self.employee_fields)
        if name == 'vehicle': return ('vehicles.csv', self.vehicle_fields)
        if name == 'vehicle_type': return ('vehicle_types.csv', self.vehicle_type_fields)

    def get_new_id(self, type):
        idMan = id_manager()
        return idMan.make_new_id(type)


    # Possible names are in get_name_and_fields function
    def write_all(self, data, name):
        catagory_name = name
        
        name, fields = self.get_name_and_fields(name)

        with open(f'{self.directory}/data/{name}', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for obj in data:
                id = self.get_new_id(catagory_name)
                print(id)
                line_obj = obj.__dict__()
                line_obj['id'] = id
                writer.writerow(line_obj)


    def read_all(self, name):
        model = self.get_model(name)
        name, fields = self.get_name_and_fields(name)
        retList = []

        with open(f'{self.directory}/data/{name}', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                line = [row[field] for field in fields]
                obj = model(*line)
                retList.append(obj)
        return retList 
