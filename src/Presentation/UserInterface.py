from Logic.LogicAPI import LogicAPI
from Presentation.Menu import Menu, FuncMenu
from Presentation.Operations import *
import os

class UserInterface:
    def __init__(self):
        self.logic = LogicAPI()

        self.logic.vehicles.get_all_vehicles()

        main_menu = Menu("Main Menu", None, None)
        office_menu = Menu("Office Menu", None, main_menu)
        airport_menu = Menu("Airport menu", None, main_menu)

        main_menu.selectable_options.append(office_menu)
        main_menu.selectable_options.append(airport_menu)

        office_menu.selectable_options += [
            Menu("Employee Managment", [
                FuncMenu("Register Employee", [display_all_employees, display_all_employees], office_menu, self.logic, self),
                FuncMenu("Edit Employee", [test, test], office_menu, self.logic, self),
                FuncMenu("Display Employee", [display_all_employees, test], office_menu, self.logic, self),
            ], office_menu),
            Menu("Vehicle Managment", [
                
            ], office_menu),
            Menu("Contract Managment", [
                FuncMenu('Display Contract', [display_all_contracts], office_menu, self.logic, self),
                FuncMenu('Register New Contract', [register_new_contract], office_menu, self.logic, self )
            ], office_menu),
            Menu("Reports", [
               
            ], office_menu)
        ]

        self.current_menu = main_menu

    def get_user_input(self, message):
        return input(message)

    def get_user_form(self, parameters):
        response = []

        for parameter in parameters:
            response.append(input(parameter + ': '))

        return response

    def change_menu(self):
        pass

    def interface_loop(self):
        while True:
            # Clear the screen
            #os.system('cls')

            self.current_menu.display()

            choice = self.get_user_input("Enter a choice: ")

            # Check if the option is a command
            if not str.isnumeric(choice):
                if choice == 'q' or choice == 'Q':
                    exit()
                elif choice == 'b' or choice == 'B':
                    # If the parent menu is None, the current menu is the main menu
                    if self.current_menu.parent is None:
                        if input("Are you sure you want to exit? (y\\n): ") == 'y':
                            exit()
                        else:
                            pass
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