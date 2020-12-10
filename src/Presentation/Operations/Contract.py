''' Operations calling the vehicle logic API '''

from Presentation.Operations.Generic import *

def register_contract(logicAPI, ui):
    ignore_fields = ['vehicle_state', 'vehicle_status', 'vehicle_licence', 'vehicle_type', 'rate', 'late_fee', 'total_price',
                    'customer_name', 'phone', 'email', 'address', 'customer_licence', 'date_handover', 'date_return', 'time_handover',
                    'time_return', 'state']
    o = Operations(logicAPI, ui)
    o.register(o.contract, ignore_fields)

def edit_contract(logicAPI, ui):   
    ignore_fields = [] 
    o = Operations(logicAPI, ui)
    o.edit(o.contract, ignore_fields)
      
def get_contract(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get(o.contract)

def get_all_contracts(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get_all(o.contract)

def get_printable_contract(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.printable_version(o.contract)

'''This is for chuck to be able to get overview of his company'''
def get_printable_overview_of_business(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.get_overview(o.contract)
