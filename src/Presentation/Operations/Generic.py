from datetime import date,datetime
from Presentation.input_verifiers import Input_Verifiers
from Presentation.Menu import format_function_name
from Models.Contract import Contract
from Models.Customer import Customer
from Models.Destination import Destination
from Models.Employee import Employee
from Models.Vehicle import Vehicle
from Models.Vehicle_Type import Vehicle_Type
import os, re
from inspect import signature

from Presentation.Display import Display

class Operations:
    def __init__(self, lapi, ui):
        self.logicAPI = lapi
        self.ui = ui
        self.verify = Input_Verifiers(lapi)

        # Get the number of required parameters to the init method of the class
        self.contract = [Contract(*[None for i in range(len(signature(Contract).parameters))]), lapi.contract]
        self.customer = [Customer(*[None for i in range(len(signature(Customer).parameters))]), lapi.customer]
        self.destination = [Destination(*[None for i in range(len(signature(Destination).parameters))]), lapi.destination]
        self.employee = [Employee(*[None for i in range(len(signature(Employee).parameters))]), lapi.employee]
        self.vehicle = [Vehicle(*[None for i in range(len(signature(Vehicle).parameters))]), lapi.vehicle]
        self.vehicle_type = [Vehicle_Type(*[None for i in range(len(signature(Vehicle_Type).parameters))]), lapi.vehicle_type]
        self.display = Display()

    def register(self, model, ignore_fields=[]):
        ''' Register a new object by model '''
        form = self.ui.get_user_form(
            {key:self.verify.get_verifier(key) for key in model[0].fields() if key not in ignore_fields}
        )

        if not form:
            return
        
        model[1].register(form)


    def edit(self, model, ignore_fields=[]):
        fields = model[0].fields()
        logic = model[1]

        # Get Object
        print("Choose a method to select a %s" % model[0].__class__.__name__)
        search_query = self.ui.get_user_option(logic.get_search_options())

        if not search_query:
            return
        else:
            employee = search_query(self.ui.get_user_input("Enter a search term: "))

        if len(employee) > 1:
            print("Multiple results, select a %s" % model[0].__class__.__name__)
            employee = self.ui.get_user_option(employee)
            id = employee.id
        elif len(employee) == 0:
            print("Search returned no %s" % model[0].__class__.__name__)
            return
        else:
            id = employee[0].id

        if not id:
            return

        # Search for match
        if type(employee) is list:
            obj = vars(employee[0])
        else:
            obj = vars(employee)

        submit = False
        options = {}

        # Enter editing loop
        while submit == False:
            print('Select field to edit: ')                      

            for index, (key, val) in enumerate(obj.items()):
                # Disable id display in editing screen
                if key in ignore_fields or key == 'id': continue

                index += 1
                options[str(index)] = key
                print('{}.{:<15} {:<20}'.format(index, format_function_name(key), val))
            print('b. BACK')                                    
            print('s. SUBMIT')                                  
            
            field_num = self.ui.get_user_form({
                'selection' : ['\d|s|b', 'Please select a valid option.'.format(len(fields), len(fields))]
            })
        
            if not field_num:
                break

            field_num = field_num[0]

            if field_num.lower() == 'b':
                submit = True
                continue
            if field_num.lower() == 's':
                submit = True
                logic.edit(obj, obj['id'])
                continue
            
            try:
                verifiers = self.verify.fields[options[field_num]]  
            except:
                return                            # Get regex and error msg
            new_entry = self.ui.get_user_form({format_function_name(options[field_num]) : verifiers})  # Get input with validation
            
            if not new_entry:
                return
            
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
            ans = (self.ui.get_user_form({
                'selection' : ['\d', 'Must be digit between 1-{}'.format(field_length, field_length)]
            }))

            if not ans:
                return

            ans = int(ans[0])

        # Search and Display
        func = getattr(logic.get(), f'by_{fields[ans-1]}')
        query = input(f'Enter {fields[ans-1]}: ')
        result = func(query)

        if result != []:
            self.display.display_all(result, fields)
        else: 
            print("There is no {} that matches {}".format(fields[ans-1], query))

    def get_all(self, model):
        res = model[1].get_all()
        fields = model[0].fields()
        self.display.display_all(res, fields)

    def get_all_after_choice(self, model,key_type):
        #get all vehicle/staff after choice
        choice_list = ["\nDisplay all after {}".format(key_type)] #list to append choices to
        choice_dict = {} # dictionary to numerate and append choices to
        counter = 0  #count number of vehicles
        res = model[1].get_all_after_choice()

        fields = model[0].fields()


        for element in res:
            obj = vars(element)
            for index,(key,val) in enumerate(obj.items()):
                    for field in fields:
                        if key == str(key_type):
                            if val not in choice_list:
                                choice_list.append(val)

        print(choice_list[0])

        for destination in choice_list[1:]:
            counter +=1
            print(' %s. %s'% (counter,destination))
            choice_dict.update({str(counter):destination})

        choice = self.ui.get_user_form(
            {
                'Enter Number': ['^[1-6]$','Enter valid number between 1 and 6']
            }  
        )

        if not choice:
            return

        for key,val in choice_dict.items():
            if key == str(choice[0]):
                choice = val
        res = model[1].get_all_after_choice()
        fields = model[0].fields()

        #calls display function in Display class
        self.display.display(res, fields,choice)

    def get_all_fit_for_rental(self,model):
        '''Get all vehicles that are fit for rental'''
        res = model[1].get_all()
        fields = model[0].fields()
        self.display.display_all_fit_for_rental(res, fields)

    def printable_version(self, model):
        res = model[1].get_all()
        fields = model[0].fields()
        counter= 0
        counter_list= []

        for element in res:
            obj = vars(element)
            for index,(key,val) in enumerate(obj.items()):
                    if key == 'id':
                        counter +=1
                        counter_list.append(str(counter))
        choice = input('Enter valid number between 1 and {}: '.format(counter))
        if str(choice) not in counter_list:
            print("invalid number entered!")
        self.display.display_printable_version(res,fields,choice)

    def get_overview(self,model):
        """For papa chuck menu"""
        # •Til að hafa yfirlit með rekstrinum vill Chuck geta kallað fram eftirfarandi skýrslur í prentvænusniðmáti (print friendly formatting):
        # –Yfirlit yfir tekjur þar sem ætti að vera hægt að velja tímabilið sem á að skoða. Einnigværi gott að sjá sundurliðun á tekjum útibúa og tegund farartækja.
        # –Yfirlit yfir nýtingu farartækja á hverjum stað, flokkað eftir tegund.
        # –Yfirlit yfir reikninga á ákveðnu tímabili, þar sem hægt er að flokka eftir viðskiptavinumog hvort þeir séu farnir í inheimtu (rukkaðir).
        res = model[1].get_all()
        fields = model[0].fields()
        money_counter = 0
        dates_list = []
        dates_dict = {}
        # for element in res:
        #     obj = vars(element)
        #     for index, (key,val) in enumerate(obj.items()):
        #         if key == 'total_price':
        #             money_counter += int(val) 
        #         if key == 'late_fee':
        #             money_counter += int(val)
    
    def get_report(self,report_type):
        data = getattr(self.logicAPI.report, f'{report_type}_report')
        self.display.display_report(data(), report_type)

def test(logicAPI, ui):
    print(ui.get_user_login())