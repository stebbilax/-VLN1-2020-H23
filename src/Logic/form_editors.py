from datetime import datetime,timedelta

def vehicle_editor(form):
    # make sure no vehicle is defective and available
    if form['vehicle_state'] == 'DEFECTIVE': form['vehicle_status'] = 'Unavailable'
    
    return form



def contract_editor(form):
    if form['contract_start'] == '2020-11-01':
        if form['contract_end'] == '2021-03-31':
            if ['vehicle_type'] == 'Light water' or ['vehicle_type'] == 'Light road':
                form['late_fee'] = '0'
            if ['vehicle_type'] == 'Light water':
                form['late_fee'] = '200'
    return form

def employee_editor(form):
    if form['titel'] == 'office':
        form['airport'] = 'reykjavik'
        form['country'] = 'Iceland'

    if form['title'] == 'airport':
        if form['airport'] == 'reykjavik':
            form['country'] ='Iceland'
        if form['airport'] == 'tingwall':
            form['country'] == 'Shetland'
        if form['airport'] == 'nuuk' or form['airport'] == 'kulusuk':
            form['country'] ='Greenland'
        if form['airport'] == 'longyearbyen':
            form['country'] ='Svalbard'
        if form['airport'] == 'torshavn':
            form['country'] = 'Farao Islands'
    return form
        
        

        