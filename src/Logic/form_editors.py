from Presentation.input_verifiers import Input_Verifiers
from Logic.Enums import EnumManager

"""PÆLING AÐ BREYTA ÞESSU Í CLASA? þá get ég gert dict en ekki if if if """
def vehicle_editor(form):
    # make sure no vehicle is defective and available
    if form['vehicle_state'] == 'DEFECTIVE': form['vehicle_status'] = 'Unavailable'
    
    return form

def contract_editor(form):    
 
    if form['contract_start'] == '2020-11-01' and form['contract_end'] == '2021-03-31':
            if ['vehicle_type'] == 'Light water' or ['vehicle_type'] == 'Light road':
                form['late_fee'] = '0'
            if ['vehicle_type'] == 'Medium water':
                form['late_fee'] = '200'
    return form

def employee_editor(form):
    if form['title'] == 'office':
        form['airport'] = 'reykjavik'
        form['country'] = 'Iceland'

    return form

def destination_editor(form):
    if form['destination_name'] == 'iceland':
        form['destination_airport'] = 'reykjavik'
    if form['destination_name'] == 'Greenland':
        choice = self.ui.get_user_form(
            {
                'Airports in greenland': ['(nuuk|kulusuk)','Enter valid airport: nuuk or kulusuk']
            }  
        )
        form['destination_airport'] = choice
    if form['destination_name'] == 'svalbard':
        form['destination_airport'] = 'longyearbyen'
    if form['destination_name'] == 'farao islands':
        form['destination_airport'] = 'torshavn'
    if form['destination_name'] == 'shetland':
        form['destination_airport'] = 'tingwall'

        