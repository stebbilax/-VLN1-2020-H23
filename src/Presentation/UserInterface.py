from Logic.LogicAPI import LLAPI
from Presentation.Menu import Menu
import os

class UserInterface:
    def __init__(self):
        self.logic = LLAPI()

        main_menu = Menu("Main Menu", None, None)
        office_menu = Menu("Office Menu", None, main_menu)
        airport_menu = Menu("Airport menu", None, main_menu)

        main_menu.selectable_options.append(office_menu)
        main_menu.selectable_options.append(airport_menu)

        office_menu.selectable_options += [
            Menu("Employee Managment", None, office_menu),
            Menu("Vehicle Managment", None, office_menu),
            Menu("Contract Managment", None, office_menu),
            Menu("Reports", None, office_menu)
        ]

        self.current_menu = main_menu

    def get_user_input(self, message):
        return input(message)

    def change_menu(self):
        pass

    def interface_loop(self):
        while True:
            # Clear the screen
            os.system('cls')

            self.current_menu.display()

            choice = self.get_user_input("Enter a choice: ")

            # Check if the option is a command
            if not str.isnumeric(choice):
                if choice == 'q':
                    exit()
                elif choice == 'b':
                    self.current_menu = self.current_menu.parent
                else:
                    print("Invalid command: %s" % (choice))

            else:

                choice = int(choice)

                # Check if the input is invalid, below 0 or above the range of options
                if choice < 0 or choice > len(self.current_menu.selectable_options):
                    print("Invalid input, please input a range between %d and %d." % (0, len(self.current_menu.selectable_options)))
                else:
                    self.current_menu = self.current_menu.select_option(choice)