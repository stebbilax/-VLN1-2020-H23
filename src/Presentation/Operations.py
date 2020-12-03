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
    
        
def get_employee(logicAPI, ui):
    # "Search by: name, address, postal code, SSID, landline, phone number, email, airport, country"
    printlist = ["\nSearch by:","\n1. Name","\n2. Address", "\n3. Postal Code", "\n4. SSID", "\n5. Landline", "\n6. Phone Number", "\n7. Email", "\n8. Job Title", "\n9. Airport", "\n10. Country"]
    print(*printlist)
    choice = input("Enter a choice: ")
    if choice == '1':
        for employee in logicAPI.employee.get_employee().by_name(input("Name: ")):
            print(employee)
    elif choice == '2':
        for employee in logicAPI.employee.get_employee().by_address(input("Address: ")):
            print(employee)
    elif choice == '3':
        for employee in logicAPI.employee.get_employee().by_postal_code(input("Postal Code: ")):
            print(employee)
    elif choice == '4':
        for employee in logicAPI.employee.get_employee().by_ssid(input("SSID: ")):
            print(employee)
    elif choice == '5':
        for employee in logicAPI.employee.get_employee().by_landline(input("Landline: ")):
            print(employee)
    elif choice == '6':
        for employee in logicAPI.employee.get_employee().by_phone(input("Phone Number: ")):
            print(employee)
    elif choice == '7':
        for employee in logicAPI.employee.get_employee().by_email(input("Email: ")):
            print(employee)
    elif choice == '8':
        for employee in logicAPI.employee.get_employee().by_job_title(input("Job Title: ")):
            print(employee)
    elif choice == '9':
        for employee in logicAPI.employee.get_employee().by_airport(input("Airport: ")):
            print(employee)
    elif choice == '10':
        for employee in logicAPI.employee.get_employee().by_country(input("Country: ")):
            print(employee)
    
        

def display_all_contracts(logicAPI, ui):
    for contract in logicAPI.contract.get_all_contracts():
        print(contract)


def register_employee(logicAPI, ui):
    form = ui.get_user_form(
        {
            'Name': None,
            'Phone': ['(\d{7,15})', 'Phone number must be between 7 and 15 digits'],
            'Address': None,
            'Email': ['(.+@.+\..+)', 'Must be a valid email format.'],
            'Date From': ['\d{4}-(([1][0-2])|([0][1-9]))-(([0-2][\d])|([3][01]))', 'Must be a valid date (2020-01-01)'],
            'Date Too': ['\d{4}-(([1][0-2])|([0][1-9]))-(([0-2][\d])|([3][01]))', 'Must be a valid date (2020-01-01)'],
            'Vehicle Id': ['(\d)', 'Must be digits only'],
            'Country': [enum_to_regex(Enum_Country), enum_to_instructions(Enum_Country)],
            'Vehicle Status': [],
            'Employee Id': None,
            'Loan Date': None,
            'Return Date': None,
            'Total': None,
            'Loan Status': None,
        }
    )
    logicAPI.employee.register_employee(form)



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

def get_vehicle(logicAPI,ui):

def register_new_vehicle(logicAPI,ui):
    #must include vehicle authentication
    #must include vehicle condition
    form = ui.get_user_form(
        {
            'type': None,
            'manufacturer': ['[a-z]+$', 'Alphabetical letters only'] ,
            'year of manufacturer': ['\\d{4}$', 'Digits only'], #named YOM in model vehicle class
            'color': ['[a-z]+$', 'Alphabetical letters only'],
            'licence': None,
            'airport': [enum_to_regex(Enum_Airport),enum_to_instructions(Enum_Airport)],
            'condition (good or bad)': ['[a-z]+$', 'Alphabetical letters only'],
            'model': ['[a-z]+$', 'Alphabetical letters only'],
            'vehicle id': None, # this is licence plate on a car
        } 
    )
    
def get_vehicle(logicAPI,ui):
    printlist = ["\nSearch by:","\n1. Manufacturer","\n2. Model","\n3. Type","\n4. Year of manufacturer","\n5. Vehicle identification number","\n6. Color","\n7. Condition","\n8. Drivers licence","\n9. Location"]
    print(*printlist)
    choice = input("Enter a choice:")]
    if choice =="1":
        for vehicle in logicAPI.vehicles.get_vehicle().by_name(input("Enter name: "))
        print(vehicle)
    elif choice == "2":
        print(logicAPI.vehicles.get_vehicle().by_model(input("Enter model: ")))
    elif choice == "3":
        print(logicAPI.vehicle.get_vehicle().by_type(input("Enter type: ")))
    elif choice == "4":
        print(logicAPI.vehicle.get_vehicle().by_YOM(input("Enter year of manufacturer: "))
    elif choice == "5":
        print(logicAPI.vehicle.get_vehicle().by_VIN(input("Enter vehicle identification number: ")))
    elif choice == "6":
        print(logicAPI.vehicle.get_vehicle().by_color(input("Enter color: ")))   

    """FINISH THIS!!!!! NEED 7,8,9 """

def edit_vehicle(logicAPI,ui):
    #might call get vehicle function to search for vehicle and then edit information of that vehicle over here
    pass

def display_vehicle_rates(logicAPI,ui):
    pass


