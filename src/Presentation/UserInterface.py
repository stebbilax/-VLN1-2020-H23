from Logic.LogicAPI import LogicAPI
from Presentation.Menu import Menu, format_function_name
from Presentation.Operations import *
import os, re

# Import all operations
from Presentation.Operations.Generic import *
from Presentation.Operations.Contract import *
from Presentation.Operations.Customer import *
from Presentation.Operations.Destination import *
from Presentation.Operations.Employee import *
from Presentation.Operations.Financial import *
from Presentation.Operations.Invoice import *
from Presentation.Operations.Vehicle import *
from Presentation.Operations.Vehicle_type import *

class UserInterface:
    def __init__(self):
        self.logic = LogicAPI()
        self.operation = Operations(self.logic, self)

        # Clear window
        os.system('cls')

        self.access = self.get_user_login()

        # Create main categories
        main_menu       = Menu("Main Menu", None, None, self.logic, self, 0)
        office_menu     = Menu("Office Menu", None, main_menu, self.logic, self, 'office')
        airport_menu    = Menu("Airport menu", None, main_menu, self.logic, self, 'airport')
        papa_chuck_menu = Menu("Papa Chuck menu", None,main_menu,self.logic, self, 'admin')

        # Add three menu nodes to the main menu
        main_menu.selectable_options.append(office_menu)
        main_menu.selectable_options.append(airport_menu)
        main_menu.selectable_options.append(papa_chuck_menu)

        #region OFFICE MENU SYSTEM      =====

        # Office submenus
        employee_menu_office    = Menu("Employee Menu", None, office_menu, self.logic, self, 'office')
        vehicle_menu_office     = Menu("Vehicle Menu", None, office_menu, self.logic, self, 'office')
        contract_menu_office    = Menu("Contract Menu", None, office_menu, self.logic, self, 'office')
        report_menu_office      = Menu("Report Menu", None, office_menu, self.logic, self, 'office')
        customer_menu_office    = Menu("Customer Menu", None, office_menu, self.logic, self, 'office')
        destination_menu_office    = Menu("Destination Menu", None, office_menu, self.logic, self, 'office')
        vehicle_type_menu_office    = Menu("Vehicle Type Menu", None, office_menu, self.logic, self, 'office')



        # Add submenus to office menu node
        office_menu.selectable_options += [
            employee_menu_office, vehicle_menu_office,
            contract_menu_office, report_menu_office,
            customer_menu_office, destination_menu_office,
            vehicle_type_menu_office
        ]

        #region Office Employee menu    -----

        # Submenu for specfic employee display options
        display_employee_menu_office = Menu("Display Employee", None, employee_menu_office, self.logic, self, 'office')

        # Employee functions with employee display menu
        employee_menu_office.selectable_options += [
            register_employee, edit_employee,
            display_employee_menu_office
        ]

        # Employee display functions
        display_employee_menu_office.selectable_options += [
            get_all_employees,
            get_employee,
            get_employee_after_location,
        ]

        #endregion                      -----

        #region Office Vehicle menu     -----

        # Submenu for specific vehicle display options
        display_vehicle_menu_office = Menu("Display Vehicle", None, vehicle_menu_office, self.logic, self, 'office')

        # Vehicle functions with vehicle display menu
        vehicle_menu_office.selectable_options += [
            register_vehicle, edit_vehicle,
            display_vehicle_menu_office,
            
        ]

        # Vehicle display functions
        display_vehicle_menu_office.selectable_options += [
            get_all_vehicles,
            get_vehicle,
            get_vehicle_after_location,
            get_all_vehicle_types,
            get_vehicle_after_condition,
            get_vehicle_fit_for_rental,
        ]

        #endregion                      -----

        #region Office Contract menu    -----

        # Submenu for specific contract display options
        display_contract_menu_office = Menu ("Display Contract", None, contract_menu_office, self.logic, self, 'office')

        # Contract functions with contract display menu
        contract_menu_office.selectable_options += [
            register_contract, edit_contract,
            display_contract_menu_office,
        ]

        # Contract display functions
        display_contract_menu_office.selectable_options += [
            get_all_contracts,
            get_contract,
            get_printable_contract
        ]

        #endregion                      -----

        #region Report menu

        report_menu_office.selectable_options += [
            get_financial_report,
            get_vehicle_report,
            get_invoice_report_by_state,
            get_invoice_report_by_customer,
        ]


        #endregion


        #region Customer Contract menu    -----

        # Submenu for specific customer display options
        display_customer_menu_office = Menu ("Display Customer", None, customer_menu_office, self.logic, self, 'office')

        # Customer functions with customer display menu
        customer_menu_office.selectable_options += [
            register_customer, edit_customer,
            display_customer_menu_office
        ]

        # Customer display functions
        display_customer_menu_office.selectable_options += [
            get_customer,
            get_all_customers,
        ]

        #endregion                      -----

        #region Vehicle Type Contract menu    -----

        # Submenu for specific vehicle type display options
        display_vehicle_type_menu_office = Menu ("Display Vehicle Type", None, vehicle_type_menu_office, self.logic, self, 'office')

        # Vehicle type functions with vehicle type display menu
        vehicle_type_menu_office.selectable_options += [
            register_vehicle_type, edit_vehicle_type,
            display_vehicle_type_menu_office
        ]

        # vehicle_type display functions
        display_vehicle_type_menu_office.selectable_options += [
            get_vehicle_type,
            get_vehicle_type_rates
        ]

        #endregion                      -----

        #region destination Contract menu    -----

        # Submenu for specific destination display options
        display_destination_menu_office = Menu ("Display destination", None, destination_menu_office, self.logic, self, 'office')

        # destination functions with destination display menu
        destination_menu_office.selectable_options += [
            register_destination, edit_destination,
            display_destination_menu_office
        ]

        # destination display functions
        display_destination_menu_office.selectable_options += [
            get_destination,
            get_all_destinations,
        ]

        #endregion                      -----
        #endregion                      =====

        #region AIRPORT MENU SYSTEM     =====

        # Airport submenus
        employee_menu_airport   = Menu("Employee Menu", None, airport_menu, self.logic, self, 'airport')
        vehicle_menu_airport    = Menu("Vehicle Menu", None, airport_menu, self.logic, self, 'airport')
        contract_menu_airport   = Menu("Contract Menu", None, airport_menu, self.logic, self, 'airport')

        # Add submenus to airport menu node
        airport_menu.selectable_options += [
            employee_menu_airport, vehicle_menu_airport,
            contract_menu_airport
        ]

        #region Airport employee menu   -----

        # Submenu for specific employee display options
        display_employee_menu    = Menu("Display Employee", None, employee_menu_airport, self.logic, self, 'airport')

        # Employee functions with employee display menu
        employee_menu_airport.selectable_options += [
            display_employee_menu
        ]

        # Employee display functions
        display_employee_menu.selectable_options += [
            get_all_employees,
            get_employee,
            get_employee_after_location,
        ]

        #endregion                      -----

        #region Airport vehicle menu    -----

        # Submenu for specific vehicle display options
        display_vehicle_menu_airport = Menu("Display Vehicle", None, vehicle_menu_airport, self.logic, self, 'airport')

        # Vehicle functions with vehicle display menu
        vehicle_menu_airport.selectable_options += [
            register_vehicle, edit_vehicle,
            display_vehicle_menu_airport
        ]

        # Vehicle display functions
        display_vehicle_menu_airport.selectable_options += [
            get_all_vehicles,
            get_vehicle,
            get_vehicle_after_location,
            get_vehicle_after_condition,
            get_vehicle_fit_for_rental,
        ]

        #endregion                      -----

        #region Airport contract menu   -----

        # Submenu for specific contract display options
        display_contract_menu_airport = Menu ("Display Contract", None, contract_menu_airport, self.logic, self, 'airport')

        # Contract functions with contract display menu
        contract_menu_airport.selectable_options += [
            register_contract, edit_contract,
            display_contract_menu_airport
        ]

        # Contract display functions
        display_contract_menu_airport.selectable_options += [
            get_all_contracts,
            get_contract,
        ]

        #endregion                      -----
        #endregion                      =====
        

        #Menu for Chuck to get over view of his companys income
        company_overview_menu   = Menu("Overview of business", None, papa_chuck_menu, self.logic, self, 'airport')
        papa_chuck_menu.selectable_options += [
            company_overview_menu,
        ]

        company_overview_menu.selectable_options += [
            get_printable_overview_of_business,
        ]

        # DEVELOPER MENU
        
        developer_menu  = Menu("Developer Menu", [test], main_menu, self.logic, self, 'admin')
        main_menu.selectable_options.append(developer_menu)
        
        # END DEVELOPER MENU

        self.current_menu = main_menu

    def get_user_login(self):
        ''' Get user login credentials and assign access values '''

        # Enumerate registered employees, relevant information to login
        employees = {employee.ssn:employee.title for employee in self.logic.employee.get_all()}
        
        # Custom login credentials for administrative purposes
        employees['admin'] = 'admin'

        login = False

        print('{:-^45}\n'.format('Login'))

        while not login:
            user_ssid = self.get_user_input('Enter SSID: ')

            if user_ssid not in employees:
                self.display_error('Invalid login, please try again')
            else:
                return employees[user_ssid]

    def get_user_input(self, message):
        ''' Get a single user input '''
        return input('{:>20}'.format(message))

    def get_user_form(self, fields):
        ''' Collect user inputs in a form to process with regex validation 
            Returns false if the user cancels the operation
            Fields = {Field name : [Regex, Validation instructions]}   '''
        print("Press b to go back")
        form = []

        for field in fields:
            # Disable the ability to change id's
            if field == 'id': continue

            
            
            # If there is no specific regex validation to the input
            if fields[field] is None:
                answer = input(field + ': ')

                if answer.lower() == 'b':
                    return False

            else:
                match = False
                # Check for input message
                msg = None
                if len(fields[field]) == 4: 
                    msg = fields[field][3]
                else:
                    msg = field

                while not match:
                    answer = input(msg + ': ')

                    if answer.lower() == 'b':
                        return False

                    match = re.search(fields[field][0], answer)

                    if not match:
                        print(fields[field][1])

                    # Calls validation function, if one is provided
                    if len(fields[field]) == 3 and match:
                        if callable(fields[field][2]):
                            res = fields[field][2](form, answer)
                            match = res[0]
                            if res[0] == False:
                                print(res[1])
                    
            
            form.append(answer)

        return form

    def exit_prompt(self):
        ''' Prompt the user to exit the program '''

        prompt_answer = input("\n\nAre you sure you want to exit? (Y/N) ")
        if prompt_answer.lower() == 'y':
            exit()

    def get_user_option(self, options):
        ''' Prompt the user to select an option from a list 
            Returns the selected item and supports a list of methods ''' 

        invalid = True

        # Check if options are methods
        if callable(options[0]):
            temp_options = [format_function_name(option.__name__) for option in options]
        else:
            temp_options = options

        for index, option in enumerate(temp_options):
            print(str(index + 1) + '.', option)
        while invalid:
            opt = self.get_user_input('Select an option: ')
            if opt.isnumeric():
                opt = int(opt)
                if opt < 0 or opt > len(temp_options):
                    print("Invalid input, please input a range between %d and %d." % (1, len(temp_options)))
                else:
                    invalid = False
            elif opt == 'b':
                return False

        return options[opt - 1]

    def display_error(self, errorMsg):
        print(errorMsg)

    def interface_loop(self):
        while True:
            self.current_menu.display()

            choice = self.get_user_input("Enter a choice: ")

            # Check if the option is a command
            if not str.isnumeric(choice):
                if choice == 'q' or choice == 'Q':
                    exit()
                elif choice == 'b' or choice == 'B':
                    # If the parent menu is None, the current menu is the main menu
                    if self.current_menu.parent is None:
                        self.exit_prompt()
                    else:
                        self.current_menu = self.current_menu.parent
                else:
                    print("Invalid command: %s" % (choice))

            else:

                choice = int(choice) - 1

                # Check if the input is invalid, below 1 or above the range of options
                if choice < 0 or choice > len(self.current_menu.selectable_options) - 1:
                    print("Invalid input, please input a range between %d and %d." % (1, len(self.current_menu.selectable_options)))
                else:
                    self.current_menu = self.current_menu.select_option(choice)

            print('\n\n')