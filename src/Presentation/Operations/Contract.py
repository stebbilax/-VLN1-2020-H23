''' Operations calling the vehicle logic API '''

from Presentation.Operations.Generic import *

def register_contract(logicAPI, ui):
    '''Register new contract. Ignore fields do not get prompted in the registration process'''
    ignore_fields = ['vehicle_state', 'vehicle_status', 'vehicle_licence', 'vehicle_type', 'rate', 'late_fee', 'total_price',
                    'customer_name', 'phone', 'email', 'address', 'customer_licence', 'date_handover', 'date_return', 'time_handover',
                    'time_return', 'state', 'date_of_creation']
    o = Operations(logicAPI, ui)
    o.register(o.contract, ignore_fields)

def edit_contract(logicAPI, ui):
    '''Edit contract. Ignore fields do not get prompted in the Editing process'''  
    ignore_fields = [] 
    o = Operations(logicAPI, ui)
    o.edit(o.contract, ignore_fields)
      
def get_contract(logicAPI, ui):
    '''Search for contract'''
    o = Operations(logicAPI, ui)
    o.get(o.contract)

def get_all_contracts(logicAPI, ui): 
    '''Get/display all contracts. ignore fields do not get displayed on screen''' 
    ignore_fields = ['vehicle_state','vehicle_status','address','customer_id','employee_id','time_handover','time_return',
                    ' total_price', 'late_fee', 'rate', 'date_handover', 'date_return', 'vehicle_licence', 'customer_licence']
    o = Operations(logicAPI, ui)
    o.get_all(o.contract, ignore_fields)

def get_printable_contract(logicAPI,ui):
    '''Displays contract in a printable format'''
    o = Operations(logicAPI, ui)
    o.printable_version(o.contract)


