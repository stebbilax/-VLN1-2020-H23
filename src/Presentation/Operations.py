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


def display_all_vehicles(logicAPI, ui):
    for vehicles in logicAPI.vehicles.get_all_vehicles():
        print(vehicles)

def display_all_vehicles_in_a_location(logicAPI,ui):
    pass

def display_vehicle_condition(logicAPI,ui):
    pass

def get_vehicle(logicAPI,ui):

def register_new_vehicle(logicAPI,ui):
    #must include vehicle authentication
    #must include vehicle condition
    ui.get_user_form(
        ['manufacturer','model','type','year of manufacturer','vehicle identification number','color','condition (good or bad)','licence','location'], #ath data vehicle.csv i odruvisi rod, tharf ad laga
        ['[a-z]+$',None,None,'\\d{4}$',None,'[a-z]+$','[a-z]+$',None,enum_to_regex(Enum_Airport)],
        ['','','','','','','','','']
        # 
    )
    

def get_vehicle(logicAPI,ui):
    print("\nSearch by:")
    print("1. Manufacturer")
    print("2. Model")
    print("3. Type")
    print("4. Year of manufacturer")
    print("5. Vehicle identification number")
    print("6. Color")
    print("7. Condition")
    print("8. Drivers licence")
    print("9. Location")
    choice = input("Enter a choice:")
    if choice =="1":
        print(logicAPI.vehicles.get_vehicle().by_name(input("Enter name: ")))
    elif choice == "2":
        print(logicAPI.vehicles.get_vehicle().by_model(input("Enter model: ")))
    elif choice == "3":
        print(logicAPI.vehicle.get_vehicle().by_type(input("Enter type: ")))
    elif choice == "4":
        print(logicAPI.vehicle.get_vehicle().by_YOM(input("Enter year of manufacturer: "))
    elif choice == "5":
        print(logicAPI.vehicle.get_vehicle().by_VIN(input("Enter vehicle identification number: ")))
    elif choice == "6":
        print(logicAPI.vehicle.get_vehicle().by_)    

def edit_vehicle(logicAPI,ui):
    #might call get vehicle function to search for vehicle and then edit information of that vehicle over here
    pass

def display_vehicle_rates(logicAPI,ui):
    pass


