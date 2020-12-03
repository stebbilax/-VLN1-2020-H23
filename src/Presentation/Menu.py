class Menu:
    def __init__(self, header, options, parent):
        self.header = header
        self.selectable_options = options or []
        self.parent = parent

    def display(self):
        print(self.header)
        
        # Iterate the length so we can enumerate the options with an integer
        for option in range(len(self.selectable_options)):
            print("%d. %s" % (option + 1, self.selectable_options[option].header))

    def select_option(self, id):
        return self.selectable_options[id]    

class FuncMenu:
    def __init__(self, header, options, parent, api):
        self.header = header
        self.selectable_options = options or []
        self.parent = parent
        self.logicAPI = api

    def display(self):
        print(self.header)

        # Iterate the length so we can enumerate the options with an integer
        for option in range(len(self.selectable_options)):
            print("%d. %s" % (option + 1, format_function_name(self.selectable_options[option].__name__)))

    def select_option(self, func):
        self.selectable_options[func](self.logicAPI)
        return self.parent

def format_function_name(name):
    ''' Formats PEP8 function names to user friendly strings '''
    return name.replace('_', ' ').title()