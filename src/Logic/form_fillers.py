from Logic.Search_API import Search_API
from datetime import datetime

# Recives two dates and calculates the difference, returning in days
def calculate_date_difference(d1, d2):
    d1 = datetime.fromisoformat(d1)
    d2 = datetime.fromisoformat(d2)

    delta = d2 - d1
    return delta.days


# Finds vehicle with matching id and inserts relevant information about it
def contract_filler(form):
    Search = Search_API()

    vehicle_id_idx = 0
    vehicle_state_idx = 1
    vehicle_status_idx = 2
    vehicle_licence_idx = 3
    date_from_idx = 12
    date_too_idx = 13
    contract_state_idx = 16
    vehicle_rate_idx = 17
    vehicle_late_fee_idx = 18
    vehicle_total_price_idx = 19

    vehicle_id = form[vehicle_id_idx]

    vehicle = vars(Search.search_vehicle().by_id(vehicle_id)[0])
    
    
    form.insert(vehicle_state_idx, vehicle['vehicle_state'])
    form.insert(vehicle_status_idx, vehicle['vehicle_status'])    
    form.insert(vehicle_licence_idx, vehicle['licence'])
    form.insert(contract_state_idx, 'VALID')
    form.insert(vehicle_rate_idx, vehicle['rate'])       
    form.insert(vehicle_late_fee_idx, 'N/A')
    form.insert(vehicle_total_price_idx, 'N/A')

    return form


def vehicle_filler(form):
    Search = Search_API()

    type_idx = 0
    airport_idx = 5
    vehicle_status = 7
    rate_index = 8

    airport_name = form[airport_idx]
    type_name = form[type_idx]

    form.insert(rate_index, 'N/A')
    form.insert(vehicle_status, 'AVAILABLE')

    types = Search.search_vehicle_type().by_name(type_name)
    for t in types:
        obj = vars(t)
        if obj['name'].lower() == type_name.lower() and obj['airport'].lower() == airport_name.lower():
            form.insert(rate_index, obj['rate'])

    return form


    

