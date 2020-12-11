''' Operations calling the destination logic API '''

from Presentation.Operations.Generic import *

def register_destination(logicAPI,ui):
    '''Register new destination. Ignore fields do not get prompted in the registration process'''
    ignore_fields = []
    o = Operations(logicAPI, ui)
    o.register(o.destination, ignore_fields)

    # Regenerate fields due to changed enums
    ui.operation.verify.generate_fields()

def edit_destination(logicAPI,ui):
    '''Edit destination. Ignore fields do not get prompted in the Editing process'''
    ignore_fields = []
    o = Operations(logicAPI, ui)
    o.edit(o.destination, ignore_fields)
    
def get_destination(logicAPI,ui):
    '''Search for destination'''
    o = Operations(logicAPI, ui)
    o.get(o.destination)

def get_all_destinations(logicAPI,ui):
    '''Get/display all destinations''' 
    o = Operations(logicAPI, ui)
    o.get_all(o.destination)
