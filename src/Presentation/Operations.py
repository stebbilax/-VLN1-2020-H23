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

<<<<<<< HEAD
def get_contract(logicAPI, ui):
    # "Search by: name, phone, address, email, date_from, date_to, vehicle_id, country, vehicle_status, employee_id, loan_date, return_date, total, loan_status, id"
    print("\nSearch by: ")
    print("1. Name")
    print("2. Email")
    print("3. Vehicle ID")
    print("4. Vehicle Status")
    print("5. Loan Status")
    print("6. Contract ID")
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
        print(logicAPI.contract.get_contract().by_id(input("Contract ID: ")))
=======
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
    pass
    

def edit_vehicle(logicAPI,ui):
    #serch for vehicle to be able to edit
    pass

def display_vehicle_rates(logicAPI,ui):
    pass

>>>>>>> 21c5f8edeceb3c4da2396f9c5d074b3b7c7dd6b8
