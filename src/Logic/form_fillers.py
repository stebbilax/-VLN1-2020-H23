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
    
    contract = {
        'vehicle_id': form[0],
        'country': form[1],
        'customer_id': form[2],
        'employee_id': form[3],
        'location_handover': form[4],
        'location_return': form[5],
        'contract_start': form[6],
        'contract_end': form[7],
    }
    vehicle         = vars(Search.search_vehicle().by_id(contract['vehicle_id'])[0])
    vehicle_type    = Search.search_vehicle_type().by_type_name(vehicle['type'])
    customer        = vars(Search.search_customer().by_id(contract['customer_id'])[0])

    contract['vehicle_state']       = vehicle['vehicle_state']
    contract['vehicle_status']      = vehicle['vehicle_status']
    contract['vehicle_licence']     = vehicle['licence']
    contract['vehicle_type']        = vehicle['type']
    contract['vehicle_id']          = vehicle['id']

    contract['customer_id']         = customer['id']
    contract['customer_name']       = customer['name']
    contract['phone']               = customer['phone']
    contract['email']               = customer['email']
    contract['address']             = customer['address']
    contract['customer_licence']    = customer['licence']

    contract['date_handover']       = 'N/A'
    contract['date_return']         = 'N/A'
    contract['time_handover']       = 'N/A'
    contract['time_return']         = 'N/A'
    contract['late_fee']            = 'N/A'
    contract['total_price']         = 'N/A'
    contract['state']               = 'Valid'

    if vehicle_type == []: 
        contract['rate'] = 'N/A'
    else: 
        contract['rate'] = vars(vehicle_type[0])['rate']
    
    return contract


def vehicle_filler(form):
    Search = Search_API()

    vehicle = {
        'type' : form[0],
        'manufacturer' : form[1],
        'yom' : form[2],
        'color' : form[3],
        'licence' : form[4],
        'airport' : form[5],
        'vehicle_state' : 'OK',
        'vehicle_status' : 'Available',
        'rate': 'N/A',
        'model' : form[6],
        'vehicle_authentication' : form[7],
        'id' : None,
    }

    types = Search.search_vehicle_type().by_type_name(vehicle['type'])
    for t in types:
        obj = vars(t)
        if obj['type_name'].lower() == vehicle['type'].lower() and obj['airport'].lower() == vehicle['airport'].lower():
            vehicle['rate'] = obj['rate']

    
    return vehicle

def employee_filler(form):
    
    employee = {
        'name' : form[0],
        'address' : form[1],
        'postal_code' : form[2],
        'ssn' : form[3],
        'phone' : form[4],
        'mobile_phone' : form[5],
        'email' : form[6],
        'title' : form[7],
        'airport': form[8],
        'country' : form[9],
        'id' : None,

    }
    if employee['title'] == 'office':
        employee['airport'] = 'reykjavik'
        employee['country'] = 'Iceland' 
    if employee['airport'] == 'reykjavik': employee['country'] = 'Iceland'
    if employee['airport'] == 'kulusuk' or employee['airport'] == 'nuuk': employee['country'] = 'Greenland'
    if employee['airport'] == 'tingwall': employee['country'] = 'Shetland'
    if employee['airport'] == 'longyearbyen': employee['country'] = 'Svalbard'
    if employee['airport'] == 'torshavn': employee['country'] = 'Farao Islands'

    
    return employee


    

