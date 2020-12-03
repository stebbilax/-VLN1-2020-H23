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
    form = ui.get_user_form(
        {
            'Name': None,
            'Address': None,
            'Postal code': ['(\d)', 'Must be digits only'],
            'SSID': ['(\d{6})-(\d{4})', 'SSID must be in format (6 digits - 4 digits)'],
            'Landline': ['(\d{7,15})', 'Landline must be between 7 and 15 digits'],
            'Phone number': ['(\d{7,15})', 'Phone number must be between 7 and 15 digits'],
            'Email': ['(.+@.+\..+)', 'Must be a valid email format.'],
            'Job Title': [enum_to_regex(Enum_Title), enum_to_instructions(Enum_Title)],
            'Airport': [enum_to_regex(Enum_Airport), enum_to_instructions(Enum_Airport)],
            'Country': [enum_to_regex(Enum_Country), enum_to_instructions(Enum_Country)]
        }
    )

    logicAPI.employee.register_employee(form)

def display_all_contracts(logicAPI, ui):
    for contract in logicAPI.contract.get_all_contracts():
        print(contract)

def get_contract(logicAPI, ui):
    # "Search by: name, phone, address, email, date_from, date_to, vehicle_id, country, vehicle_status, employee_id, loan_date, return_date, total, loan_status, id"
    printlist = ["\nSearch by:","\n1. Name","\n2. Email", "\n3. Vehicle ID", "\n4. Vehicle Status", "\n5. Loan Status", "\n6. Contract ID"]
    print(*printlist)
    choice = input("Enter a choice: ")
    if choice == "1":
        print(logicAPI.contract.get_contract().by_name(input("Name: ")))
    elif choice == "2":
        print(logicAPI.contract.get_contract().by_email(input("Email: ")))
    elif choice == "3":
        print(logicAPI.contract.get_contract().by_vehicle_id(input("Vehicle ID: ")))
    elif choice == "4":
        print(logicAPI.contract.get_contract().by_vehicle_status(input("Vehicle Status: ")))
    elif choice == "5":
        print(logicAPI.contract.get_contract().by_loan_status(input("Loan Status: ")))
    elif choice == "6":
        print(logicAPI.contract.get_contract().by_id(input("Contract ID: ")))
#vehicles


def display_all_vehicles(logicAPI, ui):
    for vehicles in logicAPI.vehicles.get_all_vehicles():
        print(vehicles)

def display_all_vehicles_in_a_location(logicAPI,ui):
    pass

def display_vehicle_condition(logicAPI,ui):
    pass


def register_new_vehicle(logicAPI,ui):
    #must include vehicle authentication
    #must include vehicle condition
    ui.get_user_form(
        ['manufacturer','model','type','year of manufacturer','vehicle identification number','color','condition','licence','location'], #ath data vehicle.csv i odruvisi rod, tharf ad laga
        ['[a-z]+$',None,None,'\\d{4}$',None,'[a-z]+$','[a-z]+$',None,enum_to_regex(Enum_Airport)],
        ['','','','','','','','','']
    )
    

def edit_vehicle(logicAPI,ui):
    #serch for vehicle to be able to edit
    pass

def display_vehicle_rates(logicAPI,ui):
    pass

