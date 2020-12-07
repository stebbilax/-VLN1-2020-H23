from datetime import date
from Presentation.input_verifiers import Input_Verifiers
from Presentation.Menu import format_function_name
from Models.Enums import *
from Models.Contract import Contract
from Models.Customer import Customer
from Models.Destination import Destination
from Models.Employee import Employee
from Models.Vehicle import Vehicle
from Models.Vehicle_Type import Vehicle_Type
import re
from inspect import signature

class Operations:
    def __init__(self, lapi, ui):
        self.logicAPI = lapi
        self.ui = ui

        # Get the number of required parameters to the init method of the class
        self.contract = [Contract(*[None for i in range(len(signature(Contract).parameters))]), lapi.contract]
        self.customer = [Customer(*[None for i in range(len(signature(Customer).parameters))]), lapi.customer]
        self.destination = [Destination(*[None for i in range(len(signature(Customer).parameters))])]
        self.employee = [Employee(*[None for i in range(len(signature(Customer).parameters))]), lapi.employee]
        self.vehicle = [Vehicle(*[None for i in range(len(signature(Customer).parameters))]), lapi.vehicle]
        self.vehicle_type = [Vehicle_Type(*[None for i in range(len(signature(Customer).parameters))])]

    def register(self, model):
        pass

def test(logicAPI, ui):
    o = Operations(logicAPI, ui)
    

def register_new(logicAPI, ui, model):
    pass


def display_all_employees(logicAPI, ui):
    ''' Display all employees '''

    for employee in logicAPI.employee.get_all_employees():
        print(employee)

def register_employee(logicAPI, ui):
    ''' Register a new employee '''

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

    # User canceled operation
    if not form:
        return

    logicAPI.employee.register_employee(form)
    
def edit_employee(logicAPI, ui):
    id = ui.get_user_input('Please enter contract ID: ')
    result = logicAPI.employee.get_employee().by_id(id)
    if result == []: ui.display_error(f'No employee found with the ID {id}\n')
    else:
        employee = result[0].__dict__()
        submit = False
        options = {}

        while submit == False:
            print('Select field to edit:')                      

            for index, (key, val) in enumerate(employee.items()):
                index += 1
                options[str(index)] = key
                print('{}.{:<15} {:<20}'.format(index, format_function_name(key), val))
            print('b. BACK')                                    
            print('s. SUBMIT')                                  
            
            field_num = input('Enter field number: ')         # Select which field to edit
            if field_num.lower() == 'b':
                submit = True
                continue
            if field_num.lower() == 's':
                submit = True
                logicAPI.employee.edit_employee(employee, employee['id'])
                continue
            
            
            verifiers = Input_Verifiers().fields[options[field_num]]                              # Get regex and error msg
            new_entry = ui.get_user_form({format_function_name(options[field_num]) : verifiers})  # Get input with validation
            
            if new_entry == False: return
            
            employee[options[field_num]] = new_entry[0]

def get_employee(logicAPI, ui):
    # "Search by: name, address, postal code, SSID, landline, phone number, email, airport, country"
    printlist = ["\nSearch by:","\n1. Name","\n2. Address", "\n3. Postal Code", "\n4. SSID", "\n5. Landline", "\n6. Phone Number", "\n7. Email", "\n8. Job Title", "\n9. Airport", "\n10. Country"]
    print(*printlist)

    # Get the user input with regex validation 
    choice = ui.get_user_form(
        {'Enter Number': ['^([1-9]|1[0]|q)$',"Enter valid number between 1-10, enter q to quit"]
        }
    )[0] # Index the first and only answer

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

def register_contract(logicAPI, ui):
    # Need to impliment date checking
    field_names = ['vehicle_id','vehicle_state','vehicle_status','vehicle_licence','country',
    'customer_id','customer_name','phone','email','address','customer_licence','employee_id','date_of_handover',
    'date_of_return','contract_start','contract_end','state','rate','late_fee','total_price']


    empty_form = {format_function_name(field) : Input_Verifiers().fields[field] for field in field_names} # Create field object from the input_verifiers
    form = ui.get_user_form(empty_form)  # Fill form with data
    
    # User canceled operation
    if not form:
        return
    
    logicAPI.contract.register_contract(form)

def edit_contract(logicAPI, ui):    
    id = ui.get_user_input('Please enter contract ID: ')
    result = logicAPI.contract.get_contract().by_id(id)
    if result == []: ui.display_error(f'No contract found with the ID {id}\n')
    else:
        contract = result[0].__dict__()
        submit = False
        options = {}

        while submit == False:
            print('Select field to edit: ')                      

            for index, (key, val) in enumerate(contract.items()):
                index += 1
                options[str(index)] = key
                print('{}.{:<15} {:<20}'.format(index, format_function_name(key), val))
            print('b. BACK')                                    
            print('s. SUBMIT')                                  
            
            field_num = input('Enter field number: ')         # Select which field to edit
            if field_num.lower() == 'b':
                submit = True
                continue
            if field_num.lower() == 's':
                submit = True
                logicAPI.contract.edit_contract(contract, contract['id'])
                continue
            
            
            verifiers = Input_Verifiers().fields[options[field_num]]                              # Get regex and error msg
            new_entry = ui.get_user_form({format_function_name(options[field_num]) : verifiers})  # Get input with validation
            
            if new_entry == False: return
            
            contract[options[field_num]] = new_entry[0]
      
def get_contract(logicAPI, ui):
    search = logicAPI.contract.get_contract
    field_names = ['vehicle_id','vehicle_state','vehicle_status','vehicle_licence','country',
    'customer_id','customer_name','phone','email','address','customer_licence','employee_id','date_of_handover',
    'date_of_return','contract_start','contract_end','state','rate','late_fee','total_price']
    field_dict = {
        'vehicle_id': search().by_vehicle_id,
        'vehicle_state': search().by_vehicle_state,
        'vehicle_status': search().by_vehicle_status,
        'vehicle_licence': search().by_vehicle_licence,
        'country': search().by_country,
        'customer_id': search().by_customer_id,
        'customer_name': search().by_customer_id,
        'phone': search().by_phone,
        'email': search().by_email,
        'address': search().by_address,
        'customer_licence': search().by_customer_licence,
        'employee_id': search().by_employee_id,
        'date_of_handover': search().by_date_of_handover,
        'date_of_return': search().by_date_of_return,
        'contract_start': search().by_contract_start,
        'contract_end': search().by_contract_end,
        'state': search().by_state,
        'rate': search().by_rate,
        'late_fee': search().by_late_fee,
        'total_price': search().by_total_price,
        }


    print('Search by:')
    for i, field in enumerate(field_names):
        index = i+1
        print(f'{index}. {format_function_name(field_names[i])}')

    choice = ui.get_user_form({'Enter Number' : ['^([1-9]|1[012345]|q)$', f'Enter valid number between 1-{len(field_names)}, enter q to quit']})[0]
    search_term = input(f'{field_names[int(choice)-1]}: ')
    res = field_dict[field_names[int(choice)-1]](search_term)
    
    for result in res:
        print(result)

def display_all_vehicles(logicAPI, ui):
    '''Display all vehicles'''
    number = 0
    formid = vehicle_header(logicAPI)
    for vehicle in logicAPI.vehicles.get_all_vehicles():
        number +=1
        print_display_vehicle(vehicle,number,formid)

def display_all_vehicles_in_a_location(logicAPI,ui):
    '''Display all vehicles in a location'''

    vehicle_location_list = ['\nDisplay vehicles after location:','\n1. Reykjavik','\n2. Nuuk','\n3. Kulusk','\n4. Tingwall','\n5. Longyearbyen','\n6. Torshavn']
    print(*vehicle_location_list)
    choice = ui.get_user_form(
        {
            'Enter Number': ['^[1-6]$','Enter valid number between 1 and 6']
        }  
    )
    choice=choice[0]
    number = 0
    formid = vehicle_header(logicAPI)

    if choice == "1":
        for vehicles in logicAPI.vehicles.get_all_vehicles():
            if vehicles.__dict__()['airport'] == 'reykjavik':
                number +=1
                print_display_vehicle(vehicles,number,formid)

    elif choice == "2":
        for vehicles in logicAPI.vehicles.get_all_vehicles():
            if vehicles.__dict__()['airport'] == 'nuuk':
                number +=1
                print_display_vehicle(vehicles,number,formid)

    elif choice == "3":
        for vehicles in logicAPI.vehicles.get_all_vehicles():
            if vehicles.__dict__()['airport'] == 'kulusk':
                number +=1
                print_display_vehicle(vehicles,number,formid)

    elif choice == "4":
        for vehicles in logicAPI.vehicles.get_all_vehicles():
            if vehicles.__dict__()['airport'] == 'tingwall':
                number +=1
                print_display_vehicle(vehicles,number,formid)

    elif choice == "5":
        for vehicles in logicAPI.vehicles.get_all_vehicles():
            if vehicles.__dict__()['airport'] == 'longyearbyen':
                number +=1
                print_display_vehicle(vehicles,number,formid)

    elif choice == "6":
        for vehicles in logicAPI.vehicles.get_all_vehicles():
            if vehicles.__dict__()['airport'] == 'torshavn':
                number +=1
                print_display_vehicle(vehicles,number,formid)

def display_vehicle_condition(logicAPI,ui):
    '''Display vehicle condition'''
    vehicle_condition_list = ["\nDisplay vehicles after condition: \n1. OK \n2. DEFECTIVE" ]
    print(*vehicle_condition_list)
    choice = ui.get_user_form(
        {
            'Enter Number': ['^[1-2]$','Enter valid number between 1 and 2']
        }  
    )
    choice=choice[0]
    number = 0
    formid = vehicle_header(logicAPI)



    if choice == "1":
        for vehicles in logicAPI.vehicles.get_all_vehicles():
            if vehicles.__dict__()['condition'] == 'OK':
                number +=1
                print_display_vehicle(vehicles,number,formid)
    elif choice == "2":
        for vehicles in logicAPI.vehicles.get_all_vehicles():
            if vehicles.__dict__()['condition'] == 'DEFECTIVE':
                number +=1
                print_display_vehicle(vehicles,number,formid)
           # was like this before: print("Type: {}, Location: {}, Condition: {}, ID: {}".format(vehicles.__dict__()['type'], vehicles.__dict__()['airport'], vehicles.__dict__()['condition'], vehicles.__dict__()['id']))

def vehicle_header(logicAPI):
    formid = vehicle_print_formatting(logicAPI)
    header = "\n\t \033[4m| {:^{MAN}} | {:^{MOD}} | {:^{TYP}} | {:^{YOM}} | {:^{VIN}} | {:^{COL}} | {:^{CON}} | {:^{LIC}} | {:^{LOC}} | {:^{ID}} |\033[0m".format('Manufacturer', 'Model', 'Type',
    'YOM','VIN','Color','Condition','Licence','Location','ID',MAN = formid[0],MOD = formid[1],TYP=formid[2],YOM=formid[3],VIN = formid[4],COL = formid[5], CON = formid[6], LIC =formid[7],LOC = formid[8], ID = formid[9])
    print(header)
    return formid

def vehicle_rates_header(logicAPI):
    formid = vehicle_rates_print_formatting(logicAPI)
    header = "\n\t \033[4m| {:^{NAM}} | {:^{REG}} | {:^{RAT}} | {:^{ID}} |\033[0m".format('Type','Location','Rate','ID', NAM=formid[0], REG = formid[1], RAT = formid[2], ID = formid[3])
    print(header)
    return formid       

def vehicle_print_formatting(logicAPI):
    MAN = 0; MOD = 0; TYP = 0; YOM = 0; VIN = 0; COL = 0; CON = 0; LIC = 0; LOC = 0; ID = 0

    for i in logicAPI.vehicles.get_all_vehicles():
        if len(i.__dict__()['manufacturer']) > MAN: 
            MAN = len(i.__dict__()['manufacturer'])
        if len(i.__dict__()['model']) > MOD: 
            MOD = len(i.__dict__()['model'])
        if len(i.__dict__()['type']) > TYP: 
            TYP = len(i.__dict__()['type'])
        if len(i.__dict__()['yom']) > YOM: 
            YOM = len(i.__dict__()['yom'])
        if len(i.__dict__()['vehicle_id']) > VIN: 
            VIN = len(i.__dict__()['vehicle_id'])
        if len(i.__dict__()['color']) > COL: 
            COL = len(i.__dict__()['color'])
        if len(i.__dict__()['condition']) > CON: 
            CON = len(i.__dict__()['condition'])
        if len(i.__dict__()['licence']) > LIC: 
            LIC = len(i.__dict__()['licence'])
        if len(i.__dict__()['airport']) > LOC: 
            LOC = len(i.__dict__()['airport'])
        if len(i.__dict__()['id']) > ID: 
            ID = len(i.__dict__()['id'])
    
    if MAN < len('manufacturer'): 
        MAN = len('manufacturer')
    if MOD < len('model'): 
        MOD = len('model')
    if TYP < len('type'): 
        TYP = len('type')
    if YOM < len('yom'): 
        YOM = len('yom')
    if VIN < len('vehicle_id'): 
        VIN = len('vehicle_id')
    if COL < len('color'): 
        COL = len('color')
    if CON < len('condition'): 
        CON = len('condition')
    if LIC < len('licence'): 
        LIC = len('licence')
    if LOC < len('airport'): 
        LOC = len('airport')
    if ID < len('id'): 
        ID = len('id')

            
    LIST = [MAN,MOD,TYP,YOM,VIN,COL,CON,LIC,LOC,ID]
    
    return LIST

def vehicle_rates_print_formatting(logicAPI):
    NAM = 0; REG = 0; RAT = 0; ID = 0
    
    for i in logicAPI.vehicles.get_all_vehicle_types():
        if len(i.__dict__()['name']) > NAM: 
            NAM = len(i.__dict__()['name'])
        if len(i.__dict__()['regions']) > REG: 
            REG = len(i.__dict__()['regions'])
        if len(i.__dict__()['rate']) > RAT: 
            RAT = len(i.__dict__()['rate'])
        if len(i.__dict__()['id']) > ID: 
            ID = len(i.__dict__()['id'])

    if NAM < len('Type'): 
        NAM = len('Type')
    if REG < len('Location'): 
        REG = len('Location')
    if RAT < len('Rate'): 
        RAT = len('Rate') 
    if ID < len('ID'): 
        ID = len('ID')

    LIST = [NAM,REG,RAT,ID]

    return LIST
    
def print_display_vehicle(vehicles,number,formid):
    '''Print function for display vehicle informations'''
    # print("Vehicle number", number,":")
    # print("\n\t\tType: {},\n\t\tManufacturer: {}\n\t\tYear of manufacture: {},"
    #     "\n\t\tColor: {},\n\t\t Drivers Licence: {},\n\t\tAirport: {},"
    #     "\n\t\tCondition: {},\n\t\tModel: {},\n\t\tVehicle ID: {},\n\t\tID: {}"
    #     .format(vehicles.__dict__()['type'],vehicles.__dict__()['manufacturer'],
    #     vehicles.__dict__()['yom'],vehicles.__dict__()['color'],vehicles.__dict__()['licence'],
    #     vehicles.__dict__()['airport'],vehicles.__dict__()['condition'],vehicles.__dict__()['model'],
    #     vehicles.__dict__()['vehicle_id'],vehicles.__dict__()['id']))


    print("\t | {:^{MAN}} | {:^{MOD}} | {:^{TYP}} | {:^{YOM}} | {:^{VIN}} | {:^{COL}} | {:^{CON}} | {:^{LIC}} | {:^{LOC}} | {:^{ID}} |".format(vehicles.__dict__()['manufacturer'], 
    vehicles.__dict__()['model'], vehicles.__dict__()['type'],vehicles.__dict__()['yom'],vehicles.__dict__()['vehicle_id'],
    vehicles.__dict__()['color'],vehicles.__dict__()['condition'],vehicles.__dict__()['licence'],vehicles.__dict__()['airport'],
    vehicles.__dict__()['id'],MAN = formid[0],MOD = formid[1],TYP=formid[2],YOM=formid[3],VIN = formid[4],COL = formid[5], CON = formid[6], LIC =formid[7],LOC = formid[8], ID = formid[9]))

def register_vehicle(logicAPI,ui):
    '''Register new vehicle'''

    field_names = ['type','manufacturer','year of manufacturer','color','licence','airport','condition','model','vehicle id']
    # User canceled operation
    
    empty_form = {format_function_name(field) : Input_Verifiers().fields[field] for field in field_names} # Create field object from the input_verifiers
    form = ui.get_user_form(empty_form)  # Fill form with data

    if not form:
        return

    logicAPI.vehicles.register_vehicle(form)
    
def get_vehicle(logicAPI,ui):
    ''' Get  '''
    printlist = ["\nSearch by:","\n1. Type","\n2. Manufacturer","\n3. Year Of Manufacturer","\n4. Color","\n5. drivers licence","\n6. Airport location","\n7. Condition","\n8. Model","\n9. Vehicle ID"]
    print(*printlist)

    # Get the user input with regex validation
    choice = ui.get_user_form(
        {
            'Enter Number': ['^([1-9]{1}|b|q)$',"Enter valid number between 1-9, enter q to quit"]
        }
    )[0] # Index the first and only answer

    if choice == "1":
        for vehicle in logicAPI.vehicles.get_vehicle().by_type(input("Enter type: ")):
            print(vehicle)
    elif choice =="2":
        for vehicle in logicAPI.vehicles.get_vehicle().by_manufacturer(input("Enter manufacturer: ")):
            print(vehicle)
    elif choice == "3":
        for vehicle in logicAPI.vehicles.get_vehicle().by_yom(input("Enter year of manufacturer: ")): #yom: year of manufacturer
            print(vehicle)
    elif choice == "4":
        for vehicle in logicAPI.vehicles.get_vehicle().by_color(input("Enter color: ")):
            print(vehicle)   
    elif choice == "5":
        for vehicle in logicAPI.vehicles.get_vehicle().by_licence(input("Enter licence: ")):
            print(vehicle)
    elif choice == "6":
        for vehicle in logicAPI.vehicles.get_vehicle().by_airport(input("Enter airport: ")):
            print(vehicle)
    elif choice == "7":
        for vehicle in logicAPI.vehicles.get_vehicle().by_condition(input("Enter condition: ")):
            print(vehicle)
    elif choice == "8":
        for vehicle in logicAPI.vehicles.get_vehicle().by_model(input("Enter model: ")):
            print(vehicle)
    elif choice == "9":
        for vehicle in logicAPI.vehicles.get_vehicle().by_vehicle_id(input("Enter vehicle identification number: ")): 
            print(vehicle)
     
def edit_vehicle(logicAPI,ui):
    #might call get vehicle function to search for vehicle and then edit information of that vehicle over here
    id = ui.get_user_input("Please enter vehicle identification number: ")
    result = logicAPI.vehicles.get_vehicle().by_id(id)
    if result == []: ui.display_error(f'No vehicle found with this identification number')
    else:
        vehicle = result[0].__dict__()
        submit = False
        options = {}

        while submit == False:
            print("Select field to edit: ")

            for index, (key, val) in enumerate(vehicle.items()):         
                index += 1
                options[str(index)] = key
                print('{}.{:<15} {:<20}'.format(index, format_function_name(key), val))
            print('b. BACK')                                            
            print('s. SUBMIT')                                  
            
            field_num = input()         # Select which field to edit
            if field_num.lower() == 'q':
                submit = True
                continue
            if field_num.lower() == 's':
                submit = True
                logicAPI.vehicles.edit_vehicle(vehicle, vehicle['id'])
                continue
            

            verifiers = Input_Verifiers().fields[options[field_num]]                              # Get regex and error msg
            new_entry = ui.get_user_form({format_function_name(options[field_num]) : verifiers})  # Get input with validation

            vehicle[options[field_num]] = new_entry[0]

def display_vehicle_rates(logicAPI,ui):
    formid = vehicle_rates_header(logicAPI)
    for vehicles in logicAPI.vehicles.get_all_vehicle_types():
        print("\t | {:^{NAM}} | {:^{REG}} | {:^{RAT}} | {:^{ID}} |".format(vehicles.__dict__()['name'],vehicles.__dict__()['regions'],
            vehicles.__dict__()['rate'],vehicles.__dict__()['id'],NAM = formid[0],REG=formid[1],RAT=formid[2],ID=formid[3]))
