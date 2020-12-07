from Data.DataAPI import DataAPI
from Logic.Search_API import Search_API
from Models.Employee import Employee
from Models.Contract import Contract
from Models.Vehicle import Vehicle
from Logic.form_fillers import contract_filler



class LogicAPI:
    def __init__(self):
        self.dataAPI = DataAPI()
        self.searchAPI = Search_API()
        self.vehicle = ManageVehicles(self.dataAPI, self.searchAPI)
        self.employee = ManageEmployees(self.dataAPI, self.searchAPI)
        self.contract = ManageContracts(self.dataAPI, self.searchAPI)

class ManageVehicles:
    def __init__(self, dapi, sapi):
        self.dataAPI = dapi
        self.searchAPI = sapi

    def register(self,form):
        new_vehicle = Vehicle(*form)
        self.dataAPI.append_vehicle(new_vehicle)

    def edit(self,form,id):
        new_vehicle = Vehicle(**form)
        self.dataAPI.edit_vehicle(new_vehicle, id)

    def get(self):
        return self.searchAPI.search_vehicle() # Search

    def get_all_vehicles(self):
        return self.dataAPI.read_all_vehicles()

    def get_all_vehicle_types(self):
        return self.dataAPI.read_all_vehicle_types()

    def get_vehicle_search_options(self):
        return [getattr(self.searchAPI.search_vehicle(), func) 
            for func in dir(self.searchAPI.search_vehicle())
            if callable(getattr(self.searchAPI.search_vehicle(), func)) and not func.startswith('__')]

class ManageEmployees:
    def __init__(self, dapi, sapi):
        self.dataAPI = dapi
        self.searchAPI = sapi
    
    def register(self, form):
        new_employee = Employee(*form)
        self.dataAPI.append_employee(new_employee)
    
    def edit(self, form, id):
        new_employee = Employee(**form)
        self.dataAPI.edit_employee(new_employee, id)
    
    def get(self):
        return self.searchAPI.search_employee() # Search
    
    def get_all_employees(self):
        return self.dataAPI.read_all_employees()

    def get_employee_search_options(self):
        return [getattr(self.searchAPI.search_employee(), func) 
            for func in dir(self.searchAPI.search_employee())
            if callable(getattr(self.searchAPI.search_employee(), func)) and not func.startswith('__')]

class ManageContracts:
    def __init__(self, dapi, sapi):
        self.dataAPI = dapi
        self.searchAPI = sapi
    
    def register(self, form):
        new_form = contract_filler(form)
        new_contract = Contract(*new_form)
        self.dataAPI.append_contract(new_contract)
    
    def edit(self, form, id):
        new_contract = Contract(**form)
        self.dataAPI.edit_contract(new_contract, id)
    
    def get(self):
        return self.searchAPI.search_contract() # Search
    
    def get_all_contracts(self):
        return self.dataAPI.read_all_contracts()

    def get_contract_search_options(self):
        return [getattr(self.searchAPI.search_contract(), func) 
            for func in dir(self.searchAPI.search_contract())
            if callable(getattr(self.searchAPI.search_contract(), func)) and not func.startswith('__')]

class ManageCustomers:
    def __init__(self, dapi, sapi):
        self.dataAPI = dapi
        self.searchAPI = sapi
    
    def register(self, form):
        pass
    
    def edit(self, form, id):
        pass
    
    def get(self):
        pass

class VehicleTypes:
    def __init__(self, dapi, sapi):
        self.dataAPI = dapi
        self.searchAPI = sapi
    
    def register(self, form):
        pass
    
    def edit(self, form, id):
        pass
    
    def get(self):
        pass

class Destinations:
    def __init__(self, dapi, sapi):
        self.dataAPI = dapi
        self.searchAPI = sapi
    
    def register(self, form):
        pass
    
    def edit(self, form, id):
        pass
    
    def get(self):
        pass


