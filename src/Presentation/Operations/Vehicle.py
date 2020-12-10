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
    res = logicAPI.vehicle.get().by_id(id)
    # Check if vehicle exists
    if res == []: 
        print('Vehicle not found')
        return

    # Check if vehicle is available
    vehicle = vars(res[0])
    if vehicle['vehicle_status'] == 'Unavailable': 
        print('This vehicle is Unavailable')
        return

    # Check if vehicle has a contract assigned to it
    con_res = logicAPI.contract.get().by_vehicle_id(vehicle['id'])
    if con_res == []: 
        print('Vehicle does not belong to any contract. Please create a contract first')
        return

    contract = vars(con_res[0])

    #Check if contract has a rate
    if contract['rate'] == 'N/A':
        print('Contract does not yet have a rate. Please add a rate before handing over vehicle')
        return

    # Add handover time and date to contract
    date, time = datetime.now().replace(microsecond=0, second=0).isoformat().split('T')
    vehicle['vehicle_status'] = 'Unavailable'
    contract['vehicle_status'] = 'Unavailable'
    contract['date_handover'] = date
    contract['time_handover'] = time[0:5]



    logicAPI.vehicle.edit(vehicle, vehicle['id'])
    logicAPI.contract.edit(contract, contract['id'])

    return 'Success'
