import os
from Data.csv_manager import Csv_Manager

class DataAPI:
    """
    Methods:
    -   write_all_[contracts, customers, destinations, employees, vehicles, vehicle_types]
    -   read_all_[contracts, customers, destinations, employees, vehicles, vehicle_types]

    All data should be a list of objects
    """
    def __init__(self):
        self.data_dir = os.getcwd() + '\data/'
        self.manager = Csv_Manager(self.data_dir)


    def write_all_contracts(self, data):
        self.manager.write_all(data, 'contract')
    def read_all_contracts(self):
        return self.manager.read_all('contract')
    

    def write_all_customers(self, data):
        self.manager.write_all(data, 'customer')
    def read_all_customers(self):
        return self.manager.read_all('customer')


    def write_all_destinations(self, data):
        self.manager.write_all(data, 'destination')
    def read_all_destinations(self):
        return self.manager.read_all('destination')


    def write_all_employees(self, data):
        self.manager.write_all(data, 'employee')
    def read_all_employees(self):
        return self.manager.read_all('employee')
    def append_employee(self, data):
        self.manager.append(data, 'employee')


    def write_all_vehicles(self, data):
        self.manager.write_all(data, 'vehicle')
    def read_all_vehicles(self):
        return self.manager.read_all('vehicle')


    def write_all_vehicle_types(self, data):
        self.manager.write_all(data, 'vehicle_type')
    def read_all_vehicle_types(self):
        return self.manager.read_all('vehicle_type')

        
    

    





