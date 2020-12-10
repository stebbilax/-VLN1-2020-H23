''' Operations calling the invoice logic API '''

from Presentation.Operations.Generic import *

def get_invoice_report(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get_report('invoice')

def get_invoice(logicAPI, ui):
    print('Please enter Id of contract')
    id = input('ID: ')
    res = logicAPI.invoice.generate_invoice(id)
    print(res)

def pay_invoice(logicAPI, ui):
    print('Please enter Id of contract')
    id = input('ID: ')
    res = logicAPI.invoice.pay_invoice(id)
    print(res)