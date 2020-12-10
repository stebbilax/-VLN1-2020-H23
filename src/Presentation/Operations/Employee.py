''' Operations calling the employee logic API '''

from Presentation.Operations.Generic import *

def get_employee_after_location(logicAPI,ui):
    key_type = ui.get_user_form(
        {
            'Pick one: country, airport, title ': ['(?:country|airport|title)$','Enter valid word!']
        }  
    )
    if key_type == False: return
    o = Operations(logicAPI, ui)
    o.get_all_after_choice(o.employee,key_type[0])

def register_employee(logicAPI, ui):
    ignore_fields = []
    o = Operations(logicAPI, ui)
    o.register(o.employee, ignore_fields)
    
def edit_employee(logicAPI, ui):
    ignore_fields = ['name','ssn']
    o = Operations(logicAPI, ui)
    o.edit(o.employee, ignore_fields)

def get_employee(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get(o.employee)

def get_all_employees(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get_all(o.employee)