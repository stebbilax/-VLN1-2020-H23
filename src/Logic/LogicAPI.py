from Data.DataAPI import DataAPI

class LogicAPI:
    def __init__(self):
        self.dataAPI = DataAPI()
        self.vehicles = ManageVehicles(self.dataAPI)
        self.employee = ManageEmployees(self.dataAPI)
        self.contract = ManageContracts(self.dataAPI)

class ManageVehicles:
    def __init__(self, api):
        self.dataAPI = api

    def register_vehicle(self):
        pass

    def edit_vehicle(self):
        pass

    def get_vehicle(self):
        pass # Search

    def get_all_vehicles(self):
        return self.dataAPI.read_all_vehicles()

class ManageEmployees:
    def __init__(self, api):
        self.dataAPI = api
    
    def register_employee():
        pass
    
    def edit_employee():
        pass
    
    def get_employee():
        pass # Search
    
    def get_all_employees():
        return self.dataAPI.read_all_employees()
    

class ManageContracts:
    def __init__(self, api):
        self.dataAPI = api
    
    def register_contract():
        pass
    
    def edit_contract():
        pass
    
    def get_contract():
        pass # Search
    
    def get_all_contracts():
        return self.dataAPI.read_all_contracts()