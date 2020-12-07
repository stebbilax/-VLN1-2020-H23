from Models.Enums import *
from Logic.Search_API import Search_API
import re
from datetime import datetime


class Input_Verifiers:
    def __init__(self):
        
        self.fields = {
            'name': None,
            'phone': ['(\d{7,15})', 'Phone number must be between 7 and 15 digits'],
            'address': None,
            'email': ['(.+@.+\..+)', 'Must be a valid email format.'],
            'contract_start': ['\d{4}-(([1][0-2])|([0][1-9]))-(([0-2][\d])|([3][01]))', 'Must be a valid date (2020-01-01)'],
            'contract_end': ['\d{4}-(([1][0-2])|([0][1-9]))-(([0-2][\d])|([3][01]))', 'Must be a valid date (2020-01-01)',compare_and_verify_times],
            'vehicle_id': ['(\d)', 'Must be digits only', find_vehicle],
            'country': [enum_to_regex(Enum_Country), enum_to_instructions(Enum_Country)],
            'vehicle_state': ['(OK|DEFECTIVE)', 'Please enter valid vehicle state (OK or DEFECTIVE)'],
            'vehicle_status': ['(ON LOAN|AVAILABLE)', 'Please enter valid vehicle status (ON LOAN or AVAILABLE)'],
            'rate': ['(\d)', 'Must be digits only'],
            'late_fee': ['(\d)', 'Must be digits only'],
            'vehicle_licence': None,
            'customer_id': None,
            'customer_name': None,
            'id': None,
            'employee_id': None,
            'customer_licence': None,
            'employee_id': None,
            'state': ['(VALID|INVALID|COMPLETED)', 'Please enter valid contract status (VALID or INVALID or COMPLETED)'], #Contract state
            'date_of_handover': ['\d{4}-(([1][0-2])|([0][1-9]))-(([0-2][\d])|([3][01]))', 'Must be a valid date (2020-01-01)'],
            'date_of_return': ['\d{4}-(([1][0-2])|([0][1-9]))-(([0-2][\d])|([3][01]))', 'Must be a valid date (2020-01-01)', compare_and_verify_times],
            'total_price': ['(\d)', 'Must be digits only'],
            'loan_status': ['(OK|RETURNED|LATE)', 'Please enter a valid loan status (OK or RETURNED or LATE)'],
            #this must be so that edit vehicle works
            'type': None,
            'manufacturer': ['[a-z]+$', 'Alphabetical letters only'] ,
            'yom': ['\\d{4}$', 'Digits only'], #named YOM in model vehicle class
            'color': ['[a-z]+$', 'Alphabetical letters only'],
            'licence': None,
            'airport': [enum_to_regex(Enum_Airport),enum_to_instructions(Enum_Airport)],
            'condition': ['(OK|DEFECTIVE)', 'Please enter valid vehicle status (OK or DEFECTIVE)'],
            'model': ['[a-z]+$', 'Alphabetical letters only'],
            'vehicle id': None, # this is licence plate on a car
            'postal_code': ['(\d)', 'Must be digits only'],
            'ssn': ['(\d{6})-(\d{4})', 'SSN must be in format (6 digits - 4 digits)'],
            'mobile_phone': ['(\d{7,15})', 'Mobile phone number must be between 7 and 15 digits'],
            'email': ['(.+@.+\..+)', 'Must be a valid email format.'],
            'title': [enum_to_regex(Enum_Title), enum_to_instructions(Enum_Title)],
            'airport': [enum_to_regex(Enum_Airport), enum_to_instructions(Enum_Airport)],
        }

    def get_verifier(self, key):
        if key in self.fields:
            return self.fields[key]
        else:
            return None



# Compares a previous date to the newly entered date
# Returns false if newly entered date is earlier in time line
def compare_and_verify_times(form, last_time):
    first_time = form[-1]
    
    d1 = datetime.fromisoformat(first_time)
    d2 = datetime.fromisoformat(last_time)
    if d2 > d1: return (True, 'Success')

    return (False, 'Invalid date interval')


# Checks if vehicle exists
def find_vehicle(form, id):
    res = Search_API().search_vehicle().by_id(id)
    if res != []: return (True, 'Success')

    return (False, 'Vehicle does not exist')


    




