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
