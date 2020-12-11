''' Operations calling the customer logic API '''

from Presentation.Operations.Generic import *

def register_customer(logicAPI,ui):
    '''Register new customer. Ignore fields do not get prompted in the registration process'''
    ignore_fields = []
    o = Operations(logicAPI, ui)
    o.register(o.customer, ignore_fields)

def edit_customer(logicAPI,ui):
    '''Edit customer. Ignore fields do not get prompted in the Editing process'''
    ignore_fields = []
    o = Operations(logicAPI, ui)
    o.edit(o.customer, ignore_fields)
    
def get_customer(logicAPI,ui): 
    '''Search for customer'''
    o = Operations(logicAPI, ui)
    o.get(o.customer)
     
def get_all_customers(logicAPI,ui):
    '''Get/display all customers''' 
    o = Operations(logicAPI, ui)
    o.get_all(o.customer)
