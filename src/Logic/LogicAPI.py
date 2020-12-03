from Data.DataAPI import DataAPI
from Logic.Search_API import Search_API

class LogicAPI:
    def __init__(self):
        self.dataAPI = DataAPI()
        self.searchAPI = Search_API()
        self.vehicles = ManageVehicles(self.dataAPI, self.searchAPI)
        self.employee = ManageEmployees(self.dataAPI, self.searchAPI)
        self.contract = ManageContracts(self.dataAPI, self.searchAPI)

class ManageVehicles:
    def __init__(self, dapi, sapi):
        self.dataAPI = dapi
        self.searchAPI = sapi

    def register_vehicle(self):
        pass

    def edit_vehicle(self):
        pass

    def get_vehicle(self, field, value):
        pass # Search

    def get_all_vehicles(self):
        return self.dataAPI.read_all_vehicles()

class ManageEmployees:
    def __init__(self, dapi, sapi):
        self.dataAPI = dapi
        self.searchAPI = sapi
    
    def register_employee(self):
        pass
    
    def edit_employee(self):
        pass
    
    def get_employee(self):
        pass # Search
    
    def get_all_employees(self):
        return self.dataAPI.read_all_employees()
    

class ManageContracts:
    def __init__(self, dapi, sapi):
        self.dataAPI = dapi
        self.searchAPI = sapi
    
    def register_contract(self):
        pass
    
    def edit_contract(self):
        pass
    
    def get_contract(self):
        pass # Search
    
    def get_all_contracts(self):
        return self.dataAPI.read_all_contracts()