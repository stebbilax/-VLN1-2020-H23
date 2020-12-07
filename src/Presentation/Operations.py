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
        self.verify = Input_Verifiers()

        # Get the number of required parameters to the init method of the class
        self.contract = [Contract(*[None for i in range(len(signature(Contract).parameters))]), lapi.contract]
        self.customer = [Customer(*[None for i in range(len(signature(Customer).parameters))]), lapi.customer]
        self.destination = [Destination(*[None for i in range(len(signature(Destination).parameters))]), lapi.destination]
        self.employee = [Employee(*[None for i in range(len(signature(Employee).parameters))]), lapi.employee]
        self.vehicle = [Vehicle(*[None for i in range(len(signature(Vehicle).parameters))]), lapi.vehicle]
        self.vehicle_type = [Vehicle_Type(*[None for i in range(len(signature(Vehicle_Type).parameters))]), lapi.vehicle_type]
        self.display = Display()

    def register(self, model):
        ''' Register a new object by model '''

        form = self.ui.get_user_form(
            {key:self.verify.get_verifier(key) for key in model[0].fields()}
        )

        if not form:
            return

        model[1].register(form)


    def edit(self, model):
        fields = model[0].fields()
        logic = model[1]

        # Get id
        id = self.ui.get_user_form({
                'ID' : ['\d', 'Please enter a digit']
            })[0]

        # Search for match
        result = logic.get().by_id(id)
        if result == []: self.ui.display_error(f'No Matches found with ID {id}\n')
        else:
            obj = vars(result[0])
            submit = False
            options = {}

            # Enter editing loop
            while submit == False:
                print('Select field to edit: ')                      

                for index, (key, val) in enumerate(obj.items()):
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
                    logic.edit(obj, obj['id'])
                    continue
                
                
                verifiers = self.verify.fields[options[field_num]]                              # Get regex and error msg
                new_entry = self.ui.get_user_form({format_function_name(options[field_num]) : verifiers})  # Get input with validation
                
                if new_entry == False: return
                
                obj[options[field_num]] = new_entry[0]


    def get(self, model):
        fields = model[0].fields()
        field_length = len(fields)
        logic = model[1]

        # Get input from user
        print('Search by:')
        for i, field in enumerate(fields):
            print(f'{i+1}. {format_function_name(field)}')

        # Validate input
        ans = -1
        while not (0 < ans <= field_length):
            ans = int(self.ui.get_user_form({
                'selection' : ['\d', 'Must be digit between 1-{}'.format(field_length, field_length)]
            })[0])

        # Search and Display
        func = getattr(logic.get(), f'by_{fields[ans-1]}')
        result = func(input(f'Enter {fields[ans-1]}: '))
        for i in result:
            print(i)


    def get_all(self, model):
        res = model[1].get_all()
        fields = model[0].fields()
        self.display.display_all(res, fields)




class Display:
    def __init__(self):
        pass


    def display_all(self, data, fields):
        ''' Register a new object by model '''

        header = ' '.join([f'{field}' for field in fields])
        print(header)



        # for field in fields:
        #     print(field, end='  ')
        # print()
        # for obj in data:
        #     d = vars(obj)
            
        #     for field in fields:
        #         print(d[field], end='  ')
        #     print()









def test(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get(o.contract)
    



def register_employee(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.register(o.employee)
    
def edit_employee(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.edit(o.employee)

def get_employee(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get(o.employee)

def get_all_employees(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get_all(o.employee)


def register_contract(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.register(o.contract)

def edit_contract(logicAPI, ui):    
    o = Operations(logicAPI, ui)
    o.edit(o.employee)
      
def get_contract(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get(o.employee)

def get_all_contracts(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get_all(o.contract)



def register_vehicle(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.register(o.vehicle)
    
def get_vehicle(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.get(o.vehicle)
     
def edit_vehicle(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.edit(o.vehicle)

def get_all_vehicles(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get_all(o.vehicle)



def register_customer(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.register(o.customer)
    
def get_customer(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.get(o.customer)
     
def edit_customer(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.edit(o.customer)



def register_destination(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.register(o.destination)
    
def get_destination(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.get(o.destination)
     
def edit_destination(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.edit(o.destination)



def register_vehicle_type(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.register(o.vehicle_type)
    
def get_vehicle_type(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.get(o.vehicle_type)
     
def edit_vehicle_type(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.edit(o.vehicle_type)





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
    header = "\n\t\033[4m| {:^{MAN}} | {:^{MOD}} | {:^{TYP}} | {:^{YOM}} | {:^{VIN}} | {:^{COL}} | {:^{CON}} | {:^{LIC}} | {:^{LOC}} | {:^{ID}} |\033[0m".format('Manufacturer', 'Model', 'Type',
    'YOM','VIN','Color','Condition','Licence','Location','ID',MAN = formid[0],MOD = formid[1],TYP=formid[2],YOM=formid[3],VIN = formid[4],COL = formid[5], CON = formid[6], LIC =formid[7],LOC = formid[8], ID = formid[9])
    print(header)
    return formid

def vehicle_rates_header(logicAPI):
    formid = vehicle_rates_print_formatting(logicAPI)
    header = "\n\t\033[4m| {:^{NAM}} | {:^{REG}} | {:^{RAT}} | {:^{ID}} |\033[0m".format('Type','Location','Rate','ID', NAM=formid[0], REG = formid[1], RAT = formid[2], ID = formid[3])
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


    print("| {:^{MAN}} | {:^{MOD}} | {:^{TYP}} | {:^{YOM}} | {:^{VIN}} | {:^{COL}} | {:^{CON}} | {:^{LIC}} | {:^{LOC}} | {:^{ID}} |".format(vehicles.__dict__()['manufacturer'], 
    vehicles.__dict__()['model'], vehicles.__dict__()['type'],vehicles.__dict__()['yom'],vehicles.__dict__()['vehicle_id'],
    vehicles.__dict__()['color'],vehicles.__dict__()['condition'],vehicles.__dict__()['licence'],vehicles.__dict__()['airport'],
    vehicles.__dict__()['id'],MAN = formid[0],MOD = formid[1],TYP=formid[2],YOM=formid[3],VIN = formid[4],COL = formid[5], CON = formid[6], LIC =formid[7],LOC = formid[8], ID = formid[9]))



def display_vehicle_rates(logicAPI,ui):
    formid = vehicle_rates_header(logicAPI)
    for vehicles in logicAPI.vehicles.get_all_vehicle_types():
        print("\t | {:^{NAM}} | {:^{REG}} | {:^{RAT}} | {:^{ID}} |".format(vehicles.__dict__()['name'],vehicles.__dict__()['regions'],
            vehicles.__dict__()['rate'],vehicles.__dict__()['id'],NAM = formid[0],REG=formid[1],RAT=formid[2],ID=formid[3]))
