from Logic.Search_API import Search_API
import re
from datetime import datetime


class Input_Verifiers:
    def __init__(self, lapi):
        self.enum = lapi.enums
        self.generate_fields()

    def generate_fields(self):
        self.fields = {
            'name': None,
            'phone': ['(\d{7,15})', 'Phone number must be between 7 and 15 digits'],
            'address': None,
            'email': ['(.+@.+\..+)', 'Must be a valid email format.'],
            'contract_start': ['\d{4}-(([1][0-2])|([0][1-9]))-(([0-2][\d])|([3][01]))', 'Must be a valid date (2020-01-01)'],
            'contract_end': ['\d{4}-(([1][0-2])|([0][1-9]))-(([0-2][\d])|([3][01]))', 'Must be a valid date (2020-01-01)',compare_and_verify_times],
            'vehicle_id':['(\d)', 'Must be digits only', check_vehicle_id],
            'country': [self.enum.enum_to_regex(self.enum.country_enum), self.enum.enum_to_instructions(self.enum.country_enum)],
            'vehicle_state': ['(OK|DEFECTIVE)', 'Please enter valid vehicle state (OK or DEFECTIVE)'],
            'vehicle_status': ['(Unavailable|Available)', 'Please enter valid vehicle status (Unavailable or Available)'],
            'rate': ['(\d)', 'Must be digits only'],
            'late_fee': ['(\d)', 'Must be digits only'],
            'vehicle_licence': None,
            'customer_id': ['(\d|n|N)', 'Must be digits only', check_customer_id],
            'vehicle_authentication': None,
            'customer_name': None,
            'id': ['(\d)','Must be digits only'],
            'employee_id':['(\d)', 'Must be digits only'],
            'customer_licence': ['(None|Drivers licence)', 'Invalid input! Input examples: None, Drivers licence'],
            'state': ['(Valid|Invalid|Completed)', 'Please enter valid contract status (Vaild or Invalid or Completed)'], #Contract state
            'date_handover': ['\d{4}-(([1][0-2])|([0][1-9]))-(([0-2][\d])|([3][01]))', 'Must be a valid date (2020-01-01)'],
            'date_return': ['\d{4}-(([1][0-2])|([0][1-9]))-(([0-2][\d])|([3][01]))', 'Must be a valid date (2020-01-01)', compare_and_verify_times],
            'total_price': ['(\d)', 'Must be digits only'],
            'loan_status': ['(OK|RETURNED|LATE)', 'Please enter a valid loan status (OK or RETURNED or LATE)'],
            'type': ['(.*)','wrong',find_vehicle_type],
            'manufacturer': ['[a-z]+$', 'Alphabetical letters only'] ,
            'yom': ['^\d{4}$', 'Digits only'], #named YOM in model vehicle class
            'color': ['[a-z]+$', 'Alphabetical letters only'],
            'licence': None,
            'airport': [self.enum.enum_to_regex(self.enum.airport_enum), self.enum.enum_to_instructions(self.enum.airport_enum)],
            'location_handover': [self.enum.enum_to_regex(self.enum.airport_enum), self.enum.enum_to_instructions(self.enum.airport_enum)],
            'location_return': [self.enum.enum_to_regex(self.enum.airport_enum), self.enum.enum_to_instructions(self.enum.airport_enum)],
            'condition': ['(OK|DEFECTIVE)', 'Please enter valid vehicle status (OK or DEFECTIVE)'],
            'model': ['[a-z]+$', 'Alphabetical letters only'],
            'postal_code': ['(\d)', 'Must be digits only'],
            'ssn': ['(\d{6})-(\d{4})', 'SSN must be in format (6 digits - 4 digits)'],
            'mobile_phone': ['(\d{7,15})', 'Mobile phone number must be between 7 and 15 digits'],
            'email': ['(.+@.+\..+)', 'Must be a valid email format.'],
            'title': [self.enum.enum_to_regex(self.enum.title_enum), self.enum.enum_to_instructions(self.enum.title_enum)],
            'airport': [self.enum.enum_to_regex(self.enum.airport_enum), self.enum.enum_to_instructions(self.enum.airport_enum)],
            'opening_hours': ['^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])-(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$','Invalid clock format, right format: 03:15-04:33'],
            'time_handover': ['^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$', 'Invalid clock format, right format 00:00'],
            'time_return': ['^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$', 'Invalid clock format, right format 00:00'],
        }

    def get_verifier(self, key):
        if key in self.fields:
            return self.fields[key]
        else:
            return None

# Compares a previous date to the newly entered date
# Returns false if newly entered date is earlier in time line
def compare_and_verify_times(form, last_time):
    if form == []: return (True, 'Success')
    first_time = form[-1]
    
    d1 = datetime.fromisoformat(first_time)
    d2 = datetime.fromisoformat(last_time)
    if d2 > d1: return (True, 'Success')

    return (False, 'Invalid date interval')


# Checks if vehicle exists
def find_vehicle(form, vehicle_id):
    res = Search_API().search_vehicle().by_vehicle_id(vehicle_id)
    if res == []: return (True, 'Success')

    return (False, 'Vehicle with that authentication already exists!')


def find_vehicle_type(form, type):
    res = Search_API().search_vehicle_type().by_type(type)
    if res == []: return (False, 'Vehicle Type does not exist, vehicle type examples: Light road, Medium water')

    return (True, 'Success')
    



def check_customer_id(form, id):
    # Check if customer exists
    res = Search_API().search_customer().by_id(id)
    if res == []: return (False, 'Customer does not exist. Please register customer')

    vehicle = vars(Search_API().search_vehicle().by_id(form[0])[0])
    customer = vars(res[0])
    # Check permitions for specified vehicle
    if vehicle['licence'] != customer['licence']: return (False, 'Customer does not carry a licence for this vehicle')

    

        
    return (True, 'Success')


def check_vehicle_id(form, id):
    res = Search_API().search_vehicle().by_id(id)
    if res == []: return (False, 'Vehicle does not exist. Please register Vehicle')

    vehicle = vars(res[0])
    # Check if vehicle is available
    if vehicle['vehicle_status'] == 'Unavailable' or vehicle['vehicle_state'] == 'DEFECTIVE': return (False, 'Vehicle is unavailable or undergoing repair')

    return (True, 'Success')


