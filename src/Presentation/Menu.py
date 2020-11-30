class Menu:
    def __init__(self, header, options, parent):
        self.header = header
        self.selectable_options = options or []
        self.parent = parent

    def display(self):
        print(self.header)
        
        # Iterate the length so we can enumerate the options with an integer
        for option in range(len(self.selectable_options)):
            print("%d. %s" % (option, self.selectable_options[option].header))

    def select_option(self, id):
        return self.selectable_options[id]