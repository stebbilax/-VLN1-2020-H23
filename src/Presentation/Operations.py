from Models.Enums import *

def test(logicAPI, ui):
    print(ui.get_user_form(
            ['SSID', 'Favorite Animal'],
            ['(\\d{7})-(\\d{4})', None],
            ['Please use a valid SSID format (6 letters - 4 letters)'])
    )

def display_all_employees(logicAPI, ui):
    for employee in logicAPI.employee.get_all_employees():
        print(employee)

def register_employee(logicAPI, ui):
    ui.get_user_form(
        ['Name', 'SSID', 'Job Title', 'Address', 'Phone number', 'Email', 'Landline', 'Country'],
        [None, '(\\d{6})-(\\d{4})', enum_to_regex(Enum_Title), None, None, None, None, enum_to_regex(Enum_Country)],
        ['','','','','','','','']
    )



def display_all_contracts(logicAPI, ui):
    for contract in logicAPI.contract.get_all_contracts():
        print(contract)


def register_new_contract(logicAPI, ui):
    print(ui.get_user_form([
        'NAME',
        'PHONE',
        'ADDRESS',
        'EMAIL',
        'DATE FROM',
        'DATE TOO',
        'VEHICLE ID',
        'COUNTRY',
        'VEHILE STATUS',
        'EMPLOYEE ID',
        'LOAN DATE',
        'RETURN DATE',
        'TOTAL',
        'LOAN STATUS',
    ],[
        None,
        '(\d)',
        None,
        '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', # EMAIL
        '\d{4}-([01][012])-(([012]\d)|([3][01]))', #DATE
        '\d{4}-([01][012])-(([012]\d)|([3][01]))', #DATE
        None,
        enum_to_regex(Enum_Country),
        '(OK|DEFECTIVE)',
        None,
        '\d{4}-([01][012])-(([012]\d)|([3][01]))', #DATE
        '\d{4}-([01][012])-(([012]\d)|([3][01]))', #DATE
        '(\d)',
        '(OK|RETURNED|LATE)'
    ],[
        None,
        'Please enter a valid phone number (Only digits)',
        None,
        'Please enter a valid email address (example@nan.is)',
        'Please enter a valid date (2020-05-05)',
        'Please enter a valid date (2020-05-05)',
        None,
        'Please select a valid country (iceland, greenland, shetland, svalbard, faroe_islands',
        'Please enter valid vehicle status (OK or DEFECTIVE)',
        None,
        'Please enter a valid date (2020-05-05)',
        'Please enter a valid date (2020-05-05)',
        'Please enter a valid total amount (Only digits)',
        'Please enter a valid loan status (OK or RETURNED or LATE)' 
    ]
    ))
#vehicles

def display_all_vehicles(logicAPI, ui):
    for vehicles in logicAPI.vehicles.get_all_vehicles():
        print(vehicles)

def display_all_vehicles_in_a_location(logicAPI,ui):
    pass

def display_vehicle_condition(logicAPI,ui):
    pass


def register_vehicle(logicAPI,ui):
    #must include vehicle authentication
    #must include vehicle condition
    pass

def  edit_veichle(logicAPI,ui):
    #serch for vehicle to be able to edit
    pass
