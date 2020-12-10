''' Operations calling the vehicle_type logic API '''

from Presentation.Operations.Generic import *

def register_vehicle_type(logicAPI,ui):
    ignore_fields = []
    o = Operations(logicAPI, ui)
    o.register(o.vehicle_type, ignore_fields)

def edit_vehicle_type(logicAPI,ui):
    ignore_fields = []
    o = Operations(logicAPI, ui)
    o.edit(o.vehicle_type, ignore_fields)
    
def get_vehicle_type(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.get(o.vehicle_type)

def get_all_vehicle_types(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get_all(o.vehicle_type)

def get_vehicle_type_rates(logicAPI,ui):
    o = Operations(logicAPI,ui)
    o.get_all(o.vehicle_type)
