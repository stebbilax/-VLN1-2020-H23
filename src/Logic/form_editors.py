from Presentation.input_verifiers import Input_Verifiers
from Logic.Enums import EnumManager

def vehicle_editor(form):
    # make sure no vehicle is defective and available
    if form['vehicle_state'] == 'DEFECTIVE': form['vehicle_status'] = 'Unavailable'
    
    return form

def contract_editor(form):    
    #Ediors for HR univeristy contract and Icelandi space agency
    if form['contract_start'] == '2020-11-01' and form['contract_end'] == '2021-03-31':
            if form['vehicle_type'].lower() == 'light water' or form['vehicle_type'].lower() == 'light road':
                form['late_fee'] = '0'
            if form['vehicle_type'].lower() == 'medium road':
                form['late_fee'] = '200'
    return form

def employee_editor(form):
    #editor so that if employee title is edited to office location will be reykjavik and country iceland
    if form['title'] == 'office':
        form['airport'] = 'reykjavik'
        form['country'] = 'Iceland'
    return form


        