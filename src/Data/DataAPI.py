import os
from Data.csv_manager import Csv_Manager

class DataAPI:
    """
    Methods:
    -   write_all_[contracts, customers, destinations, employees, vehicles, vehicle_types]
    -   read_all_[contracts, customers, destinations, employees, vehicles, vehicle_types]
    -   append_[contracts, customers, destinations, employees, vehicles, vehicle_types]
    -   edit_[contracts, customers, destinations, employees, vehicles, vehicle_types]

    Data should be a list of objects for write_all
    Data should be a single object for append
    Data should be a single modified object for edit_single
    """

    def __init__(self):
        self.data_dir = os.getcwd() + '\Data\\'
        self.manager = Csv_Manager(self.data_dir)


    # Contract menu
    def write_all_contracts(self, data):
        self.manager.write_all(data, 'contract')
    def read_all_contracts(self):
        return self.manager.read_all('contract')
    def append_contract(self, data):
        self.manager.append(data, 'contract')
    def edit_contract(self, data, id):
        self.manager.edit_single(data, 'contract', id)
    
    # Customer menu
    def write_all_customers(self, data):
        self.manager.write_all(data, 'customer')
    def read_all_customers(self):
        return self.manager.read_all('customer')
    def append_customer(self, data):
        self.manager.append(data, 'customer')
    def edit_customer(self, data, id):
        self.manager.edit_single(data, 'customer', id)

    # Destination methods
    def write_all_destinations(self, data):
        self.manager.write_all(data, 'destination')
    def read_all_destinations(self):
        return self.manager.read_all('destination')
    def append_destination(self, data):
        self.manager.append(data, 'destination')
    def edit_destination(self, data, id):
        self.manager.edit_single(data, 'destination', id)

    # Employee methods
    def write_all_employees(self, data):
        self.manager.write_all(data, 'employee')
    def read_all_employees(self):
        return self.manager.read_all('employee')
    def append_employee(self, data):
        self.manager.append(data, 'employee')
    def edit_employee(self, data, id):
        self.manager.edit_single(data, 'employee', id)

    # Vehicle methods
    def write_all_vehicles(self, data):
        self.manager.write_all(data, 'vehicle')
    def read_all_vehicles(self):
        return self.manager.read_all('vehicle')
    def append_vehicle(self, data):
        self.manager.append(data, 'vehicle')
    def edit_vehicle(self, data, id):
        self.manager.edit_single(data, 'vehicle', id)

    # Vehicle type methods
    def write_all_vehicle_types(self, data):
        self.manager.write_all(data, 'vehicle_type')
    def read_all_vehicle_types(self):
        return self.manager.read_all('vehicle_type')
    def append_vehicle_type(self, data):
        self.manager.append(data, 'vehicle_type')
    def edit_vehicle_type(self, data, id):
        self.manager.edit_single(data, 'vehicle_type', id)
        
    

    





