from Models.Enums import *


class Input_Verifiers:
    def __init__(self):
        
        self.fields = {
            'name': None,
            'phone': ['(\d{7,15})', 'Phone number must be between 7 and 15 digits'],
            'address': None,
            'email': ['(.+@.+\..+)', 'Must be a valid email format.'],
            'date_from': ['\d{4}-(([1][0-2])|([0][1-9]))-(([0-2][\d])|([3][01]))', 'Must be a valid date (2020-01-01)'],
            'date_to': ['\d{4}-(([1][0-2])|([0][1-9]))-(([0-2][\d])|([3][01]))', 'Must be a valid date (2020-01-01)',test_func],
            'vehicle_id': ['(\d)', 'Must be digits only'], #this was vehicle Id 
            'country': [enum_to_regex(Enum_Country), enum_to_instructions(Enum_Country)],
            'vehicle_status': ['(OK|DEFECTIVE)', 'Please enter valid vehicle status (OK or DEFECTIVE)'],
            'employee_id': None,
            'loan_date': ['\d{4}-(([1][0-2])|([0][1-9]))-(([0-2][\d])|([3][01]))', 'Must be a valid date (2020-01-01)'],
            'return_date': ['\d{4}-(([1][0-2])|([0][1-9]))-(([0-2][\d])|([3][01]))', 'Must be a valid date (2020-01-01)'],
            'total': ['(\d)', 'Must be digits only'],
            'loan_status': ['(OK|RETURNED|LATE)', 'Please enter a valid loan status (OK or RETURNED or LATE)'],
            #this must be so that edit vehicle works
            'type': None,
            'manufacturer': ['[a-z]+$', 'Alphabetical letters only'] ,
            'year of manufacturer': ['\\d{4}$', 'Digits only'], #named YOM in model vehicle class
            'color': ['[a-z]+$', 'Alphabetical letters only'],
            'licence': None,
            'airport': [enum_to_regex(Enum_Airport),enum_to_instructions(Enum_Airport)],
            'condition': ['(OK|DEFECTIVE)', 'Please enter valid vehicle status (OK or DEFECTIVE)'],
            'model': ['[a-z]+$', 'Alphabetical letters only'],
            'vehicle id': None, # this is licence plate on a car
        }






def test_func():
    print('works')