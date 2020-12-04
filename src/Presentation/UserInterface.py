from Logic.LogicAPI import LogicAPI
from Presentation.Menu import Menu
from Presentation.Operations import *
import os, re

class UserInterface:
    def __init__(self):
        self.logic = LogicAPI()
        self.logic.vehicles.get_all_vehicles()

        self.access = 0

        # Clear window
        os.system('cls')

        # Create main categories
        main_menu       = Menu("Main Menu", None, None, self.logic, self)
        office_menu     = Menu("Office Menu", None, main_menu, self.logic, self)
        airport_menu    = Menu("Airport menu", None, main_menu, self.logic, self)

        # Add two menu nodes to the main menu
        main_menu.selectable_options.append(office_menu)
        main_menu.selectable_options.append(airport_menu)

        #region OFFICE MENU SYSTEM      =====

        # Office submenus
        employee_menu_office    = Menu("Employee Menu", None, office_menu, self.logic, self)
        vehicle_menu_office     = Menu("Vehicle Menu", None, office_menu, self.logic, self)
        contract_menu_office    = Menu("Contract Menu", None, office_menu, self.logic, self)
        report_menu_office      = Menu("Report Menu", None, office_menu, self.logic, self)

        # Add submenus to office menu node
        office_menu.selectable_options += [
            employee_menu_office, vehicle_menu_office,
            contract_menu_office, report_menu_office
        ]

        #region Office Employee menu    -----

        # Submenu for specfic employee display options
        display_employee_menu_office = Menu("Display Employee", None, employee_menu_office, self.logic, self)

        # Employee functions with employee display menu
        employee_menu_office.selectable_options += [
            register_employee, edit_employee,
            display_employee_menu_office
        ]

        # Employee display functions
        display_employee_menu_office.selectable_options += [
            display_all_employees,
            get_employee
        ]

        #endregion                      -----

        #region Office Vehicle menu     -----

        # Submenu for specific vehicle display options
        display_vehicle_menu_office = Menu("Display Vehicle", None, vehicle_menu_office, self.logic, self)

        # Vehicle functions with vehicle display menu
        vehicle_menu_office.selectable_options += [
            register_vehicle, edit_vehicle,
            display_vehicle_menu_office
        ]

        # Vehicle display functions
        display_vehicle_menu_office.selectable_options += [
            display_all_vehicles,
            get_vehicle,
            display_all_vehicles_in_a_location,
            display_vehicle_rates,
        ]

        #endregion                      -----

        #region Office Contract menu    -----

        # Submenu for specific contract display options
        display_contract_menu_office = Menu ("Display Contract", None, contract_menu_office, self.logic, self)

        # Contract functions with contract display menu
        contract_menu_office.selectable_options += [
            register_contract, edit_contract,
            display_contract_menu_office
        ]

        # Contract display functions
        display_contract_menu_office.selectable_options += [
            display_all_contracts,
            get_contract
        ]

        #endregion                      -----
        #endregion                      =====

        #region AIRPORT MENU SYSTEM     =====

        # Airport submenus
        employee_menu_airport   = Menu("Employee Menu", None, airport_menu, self.logic, self)
        vehicle_menu_airport    = Menu("Vehicle Menu", None, airport_menu, self.logic, self)
        contract_menu_airport   = Menu("Contract Menu", None, airport_menu, self.logic, self)

        # Add submenus to airport menu node
        airport_menu.selectable_options += [
            employee_menu_airport, vehicle_menu_airport,
            contract_menu_airport
        ]

        #region Airport employee menu   -----

        # Submenu for specific employee display options
        display_employee_menu    = Menu("Display Employee", None, employee_menu_airport, self.logic, self)

        # Employee functions with employee display menu
        employee_menu_airport.selectable_options += [
            display_employee_menu
        ]

        # Employee display functions
        display_employee_menu.selectable_options += [
            display_all_employees,
            get_employee
        ]

        #endregion                      -----

        #region Airport vehicle menu    -----

        # Submenu for specific vehicle display options
        display_vehicle_menu_airport = Menu("Display Vehicle", None, vehicle_menu_airport, self.logic, self)

        # Vehicle functions with vehicle display menu
        vehicle_menu_airport.selectable_options += [
            register_vehicle, edit_vehicle,
            display_vehicle_menu_airport
        ]

        # Vehicle display functions
        display_vehicle_menu_airport.selectable_options += [
            display_all_vehicles,
            get_vehicle,
            display_all_vehicles_in_a_location,
        ]

        #endregion                      -----

        #region Airport contract menu   -----

        # Submenu for specific contract display options
        display_contract_menu_airport = Menu ("Display Contract", None, contract_menu_airport, self.logic, self)

        # Contract functions with contract display menu
        contract_menu_airport.selectable_options += [
            register_contract, edit_contract,
            display_contract_menu_airport
        ]

        # Contract display functions
        display_contract_menu_airport.selectable_options += [
            display_all_contracts,
            get_contract
        ]

        #endregion                      -----
        #endregion                      =====

        # DEVELOPER MENU
        
        developer_menu  = Menu("Developer Menu", [edit_employee], main_menu, self.logic, self)
        main_menu.selectable_options.append(developer_menu)
        
        # END DEVELOPER MENU

        self.current_menu = main_menu

    def get_user_input(self, message):
        ''' Get a single user input '''
        return input('{:>20}'.format(message))

    def get_user_form(self, fields):
        ''' Collect user inputs in a form to process with regex validation 
            Returns false if the user cancels the operation
            Fields = {Field name : [Regex, Validation instructions]}   '''
        
        form = []
        
        for field in fields:
            
            # If there is no specific regex validation to the input
            if fields[field] is None:
                answer = input(field + ': ')

                if answer.lower() == 'b':
                    return False

            else:
                match = False

                while not match:
                    answer = input(field + ': ')

                    if answer.lower() == 'b':
                        return False

                    match = re.search(fields[field][0], answer)

                    if not match:
                        print(fields[field][1])

                    ###  Calls date checking function
                    if len(fields[field]) == 3 and match:
                        if callable(fields[field][2]):
                            match = fields[field][2](form, answer)
                            if match == False:
                                print('Invalid date interval')
                    ###
            
            form.append(answer)

        return form

    def exit_prompt(self):
        ''' Prompt the user to exit the program '''

        prompt_answer = input("\n\nAre you sure you want to exit? (Y/N) ")
        if prompt_answer.lower() == 'y':
            exit()


    def display_error(self, errorMsg):
        input(errorMsg)

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