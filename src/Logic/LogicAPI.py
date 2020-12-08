from Data.DataAPI import DataAPI
from Logic.Search_API import Search_API
from Models.Employee import Employee
from Models.Contract import Contract
from Models.Vehicle import Vehicle
from Models.Customer import Customer
from Models.Vehicle_Type import Vehicle_Type
from Models.Destination import Destination
from Logic.form_fillers import contract_filler



class LogicAPI:
    def __init__(self):
        self.dataAPI = DataAPI()
        self.searchAPI = Search_API()
        self.vehicle = ManageVehicles(self.dataAPI, self.searchAPI)
        self.employee = ManageEmployees(self.dataAPI, self.searchAPI)
        self.contract = ManageContracts(self.dataAPI, self.searchAPI)
        self.customer = ManageCustomers(self.dataAPI, self.searchAPI)
        self.vehicle_type = ManageVehicleTypes(self.dataAPI, self.searchAPI)
        self.destination = ManageDestinations(self.dataAPI, self.searchAPI)

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

    def get_all(self):
        return self.dataAPI.read_all_vehicles()
    
    def get_all_location(self):
        return self.dataAPI.read_all_vehicles()

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
    
    def get_all(self):
        return self.dataAPI.read_all_employees()

    def get_all_location(self):
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
    
    def get_all(self):
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
        new_customer = Customer(*form)
        self.dataAPI.append_customer(new_customer)
    
    def edit(self, form, id):
        new_customer = Customer(**form)
        self.dataAPI.edit_customer(new_customer, id)
    
    def get(self):
        return self.searchAPI.search_customer()

class ManageVehicleTypes:
    def __init__(self, dapi, sapi):
        self.dataAPI = dapi
        self.searchAPI = sapi
    
    def register(self, form):
        new_vehicle_type = Vehicle_Type(*form)
        self.dataAPI.append_vehicle_type(new_vehicle_type)
    
    def edit(self, form, id):
        new_vehicle_type = Vehicle_Type(**form)
        self.dataAPI.edit_vehicle_type(new_vehicle_type, id)
    
    def get(self):
        return self.searchAPI.search_vehicle_type()

    def get_all(self):
        return self.dataAPI.read_all_vehicle_types()


class ManageDestinations:
    def __init__(self, dapi, sapi):
        self.dataAPI = dapi
        self.searchAPI = sapi
    
    def register(self, form):
        new_destination = Destination(*form)
        self.dataAPI.append_destination(new_destination)
    
    def edit(self, form, id):
        new_destination = Destination(**form)
        self.dataAPI.edit_destination(new_destination, id)
    
    def get(self):
        return self.searchAPI.search_destination()
    
    def get_all(self):
        return self.dataAPI.read_all_destinations()


