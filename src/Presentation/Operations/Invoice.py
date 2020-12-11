''' Operations calling the invoice logic API '''

from Presentation.Operations.Generic import *

def get_invoice_report_by_state(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get_invoice_report('state')

def get_invoice_report_by_customer(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get_invoice_report('customer')

def get_invoice(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.invoice_reciept('generate')

def pay_invoice(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.invoice_reciept('pay')