from Logic.Search_API import Search_API


# Finds vehicle with matching id and inserts relevant information about it
def contract_filler(form):
    Search = Search_API()

    vehicle_id_idx = 0
    vehicle_state_idx = 1
    vehicle_status_idx = 2
    vehicle_licence_idx = 3
    vehicle_rate_idx = 17
    vehicle_late_fee_idx = 18

    vehicle_id = form[vehicle_id_idx]

    vehicle = Search.search_vehicle().by_id(vehicle_id)[0].__dict__()
    
    
    form.insert(vehicle_state_idx, vehicle['condition'])
    form.insert(vehicle_status_idx, 'Available')    #### Should come from model
    form.insert(vehicle_licence_idx, vehicle['licence'])
    form.insert(vehicle_rate_idx, '500')         #### Should come from model
    form.insert(vehicle_late_fee_idx, 'N/A')
    
    return form


