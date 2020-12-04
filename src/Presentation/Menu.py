class Menu:
    ''' Menu node, establishes a simple tree structure '''

    def __init__(self, header, options, parent, logicAPI, ui):
        self.header = header
        self.selectable_options = options or []
        self.parent = parent
        self.logicAPI = logicAPI
        self.access_level = 0
        self.ui = ui

    def display(self):
        ''' Display menu options and graphics, with context to types '''

        # Center header
        print('{:-^45}\n'.format(self.header))
        
        # Iterate the length so we can enumerate the options with an integer

        for option in range(len(self.selectable_options)):
            if callable(self.selectable_options[option]):
                print("{:>3}. {:<25} {:>8}\n".format(option + 1, format_function_name(self.selectable_options[option].__name__), '(OPERATION)'))
            else:
                print("{:>3}. {:<25} {:>8}\n".format(option + 1, self.selectable_options[option].header, '(MENU)'))


    def select_option(self, id):
        ''' Select option, check if its a function or menu '''
        if callable(self.selectable_options[id]):
            self.selectable_options[id](self.logicAPI, self.ui)
            return self.parent
        else:
            return self.selectable_options[id]    

def format_function_name(name):
    ''' Formats PEP8 function names to user friendly strings '''
    return name.replace('_', ' ').title()