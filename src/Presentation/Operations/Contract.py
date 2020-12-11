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
    #search for customer
    o = Operations(logicAPI, ui)
    o.get(o.contract)

def get_all_contracts(logicAPI, ui): 
    #get/display all contracts 
    ignore_fields = ['vehicle_state','vehicle_status','address','customer_id','employee_id','time_handover','time_return',
                    ' total_price', 'late_fee', 'rate', 'date_handover', 'date_return', 'vehicle_licence', 'customer_licence']
    o = Operations(logicAPI, ui)
    o.get_all(o.contract, ignore_fields)

def get_printable_contract(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.printable_version(o.contract)


