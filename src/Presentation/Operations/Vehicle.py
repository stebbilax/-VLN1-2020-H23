from datetime import datetime

''' Operations calling the vehicle logic API '''

from Presentation.Operations.Generic import *

def register_vehicle(logicAPI,ui):
    ignore_fields = ['rate', 'vehicle_status', 'vehicle_state']
    o = Operations(logicAPI, ui)
    o.register(o.vehicle, ignore_fields)

def edit_vehicle(logicAPI,ui):
    ignore_fields = []
    o = Operations(logicAPI, ui)
    o.edit(o.vehicle, ignore_fields)
    
def get_vehicle(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.get(o.vehicle)


def get_all_vehicles(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get_all(o.vehicle)


def get_vehicle_after_location(logicAPI,ui):
    key_type = ['airport']
    o = Operations(logicAPI, ui)
    o.get_all_after_choice(o.vehicle,key_type[0])

def get_vehicle_after_condition(logicAPI,ui):
    key_type = ui.get_user_form(
        {
            'Pick one: vehicle_state or vehicle_status': ['(?:vehicle_state|vehicle_status)$','Enter valid word!']
        }  
    )
    if key_type == False: return

    o = Operations(logicAPI, ui)
    o.get_all_after_choice(o.vehicle,key_type[0])

def get_vehicle_fit_for_rental(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.get_all_fit_for_rental(o.vehicle)

def get_vehicle_report(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get_report('vehicle')



def handover_vehicle(logicAPI, ui):
    id = input('Enter Id of vehicle: ')
    print(logicAPI.vehicle.handover_vehicle(id))


def handin_vehicle(logicAPI, ui):
    id = input('Enter Id of vehicle: ')
    print(logicAPI.vehicle.handin_vehicle(id))