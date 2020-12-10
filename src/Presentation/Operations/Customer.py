''' Operations calling the customer logic API '''

from Presentation.Operations.Generic import *

def register_customer(logicAPI,ui):
    ignore_fields = []
    o = Operations(logicAPI, ui)
    o.register(o.customer, ignore_fields)

def edit_customer(logicAPI,ui):
    ignore_fields = []
    o = Operations(logicAPI, ui)
    o.edit(o.customer, ignore_fields)
    
def get_customer(logicAPI,ui):
    o = Operations(logicAPI, ui)
    o.get(o.customer)
     
def get_all_customers(logicAPI,ui):
    #get all customers table is too large for terminal
    o = Operations(logicAPI, ui)
    o.get_all(o.customer)
