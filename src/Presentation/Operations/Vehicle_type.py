''' Operations calling the vehicle_type logic API '''

from Presentation.Operations.Generic import *

def register_vehicle_type(logicAPI,ui):
    '''Register new vehicle type. Ignore fields do not get prompted in the registration process'''
    ignore_fields = []
    o = Operations(logicAPI, ui)
    o.register(o.vehicle_type, ignore_fields)

def edit_vehicle_type(logicAPI,ui):
    '''Edit vehicle_type. Ignore fields do not get prompted in the Editing process'''
    ignore_fields = []
    o = Operations(logicAPI, ui)
    o.edit(o.vehicle_type, ignore_fields)
    
def get_vehicle_type(logicAPI,ui):
    '''Search for vehicle type'''
    o = Operations(logicAPI, ui)
    o.get(o.vehicle_type)

def get_all_vehicle_types(logicAPI, ui):
    '''Get/display all vehicle types''' 
    o = Operations(logicAPI, ui)
    o.get_all(o.vehicle_type)

def get_vehicle_type_rates(logicAPI,ui):
    '''Get/display all vehicle type rates''' 
    o = Operations(logicAPI,ui)
    o.get_all(o.vehicle_type)
