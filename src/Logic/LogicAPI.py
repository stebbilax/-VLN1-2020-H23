from Data.DataAPI import DataAPI
from Presentation.input_verifiers import Input_Verifiers
from Logic.Search_API import Search_API
from Models.Employee import Employee
from Models.Contract import Contract
from Models.Vehicle import Vehicle
from Models.Customer import Customer
from Models.Vehicle_Type import Vehicle_Type
from Models.Destination import Destination
from Logic.form_fillers import *
from Logic.form_editors import *
from Logic.Report_Generator import Report_Generator
from Logic.Invoice_Manager import Invoice_Manager
from Logic.Enums import EnumManager


class LogicAPI:
    def __init__(self):
        self.dataAPI = DataAPI()
        self.searchAPI = Search_API()
        self.enums = EnumManager(self.dataAPI)
        self.vehicle = ManageVehicles(self, self.dataAPI, self.searchAPI)
        self.employee = ManageEmployees(self, self.dataAPI, self.searchAPI)
        self.contract = ManageContracts(self, self.dataAPI, self.searchAPI)
        self.customer = ManageCustomers(self, self.dataAPI, self.searchAPI)
        self.vehicle_type = ManageVehicleTypes(self, self.dataAPI, self.searchAPI)
        self.destination = ManageDestinations(self, self.dataAPI, self.searchAPI)
        self.report = ManageReports(self, self.dataAPI, self.searchAPI)
        self.invoice = ManageInvoices(self, self.dataAPI, self.searchAPI, self.contract)

class ManageVehicles:
    def __init__(self, lapi, dapi, sapi):
        self.logicAPI = lapi
        self.dataAPI = dapi
        self.searchAPI = sapi

    def register(self,form):
        new_form = vehicle_filler(form)
        new_vehicle = Vehicle(**new_form)
        self.dataAPI.append_vehicle(new_vehicle)

    def edit(self,form,id):
        new_form =  vehicle_editor(form)
        new_vehicle = Vehicle(**new_form)
        self.dataAPI.edit_vehicle(new_vehicle, id)

    def get(self):
        return self.searchAPI.search_vehicle() # Search

    def get_all(self):
        return self.dataAPI.read_all_vehicles()
    
    def get_all_after_choice(self):
        return self.dataAPI.read_all_vehicles()

    def get_search_options(self):
        return [getattr(self.searchAPI.search_vehicle(), func) 
            for func in dir(self.searchAPI.search_vehicle())
            if callable(getattr(self.searchAPI.search_vehicle(), func)) and not func.startswith('__')]

class ManageEmployees:
    def __init__(self, lapi, dapi, sapi):
        self.logicAPI = lapi
        self.dataAPI = dapi
        self.searchAPI = sapi
    
    def register(self, form):
        new_form = employee_filler(form)
        new_employee = Employee(**new_form)
        self.dataAPI.append_employee(new_employee)
    
    def edit(self, form, id):
        new_form =  employee_editor(form)
        new_employee = Employee(**new_form)
        self.dataAPI.edit_employee(new_employee, id)
    
    def get(self):
        return self.searchAPI.search_employee() # Search
    
    def get_all(self):
        return self.dataAPI.read_all_employees()

    def get_all_after_choice(self):
        return self.dataAPI.read_all_employees()

    def get_search_options(self):
        return [getattr(self.searchAPI.search_employee(), func) 
            for func in dir(self.searchAPI.search_employee())
            if callable(getattr(self.searchAPI.search_employee(), func)) and not func.startswith('__')]

class ManageContracts:
    def __init__(self, lapi, dapi, sapi):
        self.logicAPI = lapi
        self.dataAPI = dapi
        self.searchAPI = sapi

    def register(self, form):
        new_form = contract_filler(form)
        new_contract = Contract(**new_form)
        self.dataAPI.append_contract(new_contract)
    
    def edit(self, form, id):
        new_form = contract_editor(form)
        new_contract = Contract(**form)
        self.dataAPI.edit_contract(new_contract, id)
    
    def get(self):
        return self.searchAPI.search_contract() # Search
    
    def get_all(self):
        return self.dataAPI.read_all_contracts()

    def get_search_options(self):
        return [getattr(self.searchAPI.search_contract(), func) 
            for func in dir(self.searchAPI.search_contract())
            if callable(getattr(self.searchAPI.search_contract(), func)) and not func.startswith('__')]

class ManageCustomers:
    def __init__(self, lapi, dapi, sapi):
        self.logicAPI = lapi
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

    def get_all(self):
        return self.dataAPI.read_all_customers()

    def get_search_options(self):
        return [getattr(self.searchAPI.search_customer(), func) 
            for func in dir(self.searchAPI.search_customer())
            if callable(getattr(self.searchAPI.search_customer(), func)) and not func.startswith('__')]


class ManageVehicleTypes:
    def __init__(self, lapi, dapi, sapi):
        self.logicAPI = lapi
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

    def get_search_options(self):
        return [getattr(self.searchAPI.search_vehicle_type(), func) 
            for func in dir(self.searchAPI.search_vehicle_type())
            if callable(getattr(self.searchAPI.search_vehicle_type(), func)) and not func.startswith('__')]


class ManageDestinations:
    def __init__(self, lapi, dapi, sapi):
        self.logicAPI = lapi
        self.dataAPI = dapi
        self.searchAPI = sapi
    
    def register(self, form):
        new_destination = Destination(*form)
        self.dataAPI.append_destination(new_destination)
        self.logicAPI.enums.generate_enums()
    
    def edit(self, form, id):
        new_destination = Destination(**form)
        self.dataAPI.edit_destination(new_destination, id)
        self.logicAPI.enums.generate_enums()
    
    def get(self):
        return self.searchAPI.search_destination()

    def get_all(self):
        return self.dataAPI.read_all_destinations()
    
    def get_all_location(self):
        return self.dataAPI.read_all_destinations()

    def get_search_options(self):
        return [getattr(self.searchAPI.search_destination(), func) 
            for func in dir(self.searchAPI.search_destination())
            if callable(getattr(self.searchAPI.search_destination(), func)) and not func.startswith('__')]


class ManageReports:
    def __init__(self, lapi, dapi, sapi):
        self.RG = Report_Generator(dapi, sapi)
        
    def financial_report(self):
        return self.RG.financial_report(time_from=None, time_to=None)

    def invoice_report_by_state(self):
        return self.RG.invoice_report_by_state(time_from=None, time_to=None)

    def invoice_report_by_customer(self):
        return self.RG.invoice_report_by_customer(time_from=None, time_to=None)

    def vehicle_report(self):
        return self.RG.vehicle_report()

    
    def get_search_options(self):
        return [getattr(self.searchAPI.search_report(), func) 
            for func in dir(self.searchAPI.search_report())
            if callable(getattr(self.searchAPI.search_report(), func)) and not func.startswith('__')]



class ManageInvoices:
    def __init__(self, lapi, dapi, sapi, contract):
        self.IM = Invoice_Manager(dapi, sapi, self)
        self.contract = contract

    def generate_invoice(self, id):
        return self.IM.generate_invoice(id)

    def pay_invoice(self, id):
        return self.IM.pay_invoice(id)


    def get_search_options(self):
        return [getattr(self.searchAPI.search_invoice(), func) 
            for func in dir(self.searchAPI.search_invoice())
            if callable(getattr(self.searchAPI.search_invoice(), func)) and not func.startswith('__')]