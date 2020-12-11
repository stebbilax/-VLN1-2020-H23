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
        self.id_manager = id_manager()
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
        return self.id_manager.make_new_id(type)


    def clear_id_line(self, type):
        self.id_manager.clear_line(type)


    # Possible names are in get_name_and_fields function
    def write_all(self, data, name, clear_fields=True):
        category_name = name
        name, fields = self.get_name_and_fields(name)
        
        if clear_fields: self.clear_id_line(category_name)
        with open(f'{self.directory}/data/{name}', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for obj in data:
                line_obj = vars(obj)
                if obj.id == None:
                    id = self.get_new_id(category_name)
                    line_obj['id'] = id
                writer.writerow(line_obj)


    def read_all(self, name):
        """Reads all from a model in csv document"""
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


    def append(self, data, name):
        ''' Appends a new model to its respective csv document '''
        category_name = name
        name, fields = self.get_name_and_fields(name)

        with open(f'{self.directory}/data/{name}', 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fields)

            obj = vars(data)

            id = self.get_new_id(category_name)
            obj['id'] = id

            writer.writerow(obj)

    def edit_single(self, data, name, id):
        # print('from csv_manager : ', data)
        ''' Edits a single model by rewriting the file with the modified value
            Expects a ID to find the modified model and replace it           '''

        category_name = name
        name, fields = self.get_name_and_fields(name)

        lines = self.read_all(category_name)
        new_lines = []

        for line in range(len(lines)):
            if lines[line].id == id:
                new_lines.append(data)
            else:
                new_lines.append(lines[line])
        
        self.write_all(new_lines, category_name, False)