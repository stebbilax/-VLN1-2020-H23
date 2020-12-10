class Menu:
    ''' Menu node, establishes a simple tree structure '''

    def __init__(self, header, options, parent, logicAPI, ui, required_access):
        self.header = header
        self.selectable_options = options or []
        self.parent = parent
        self.logicAPI = logicAPI
        self.required_access = required_access
        self.ui = ui

    def display(self):
        ''' Display menu options and graphics, with context to types '''

        # Center header
        print('{:-^45}\n'.format(self.header))

        accessable_menus = []

        # Create a list of menus accessable
        for option in self.selectable_options:
            # The option is not a menu but a function object with no access level
            if callable(option):
                accessable_menus.append(option)
            elif self.ui.access == option.required_access or self.ui.access == 'admin' or option.required_access == 0:
                accessable_menus.append(option)

        # Enumerate and present accessable menus
        for index, option in enumerate(accessable_menus):
            if callable(option):
                print("{:>3}. {:<25} {:>8}\n".format(index + 1, format_function_name(option.__name__), '(OPERATION)'))
            else:
                print("{:>3}. {:<25} {:>8}\n".format(index + 1, option.header, '(MENU)'))

        return accessable_menus


    def select_option(self, id, options):
        ''' Select option, check if its a function or menu '''
        if callable(options[id]):
            options[id](self.logicAPI, self.ui)
            return self
        else:
            return options[id]    

def format_function_name(name):
    ''' Formats PEP8 function names to user friendly strings '''
    return name.replace('_', ' ').title()