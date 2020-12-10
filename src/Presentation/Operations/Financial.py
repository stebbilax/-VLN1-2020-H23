''' Operations calling the financial logic API '''

from Presentation.Operations.Generic import *

def get_financial_report(logicAPI, ui):
    o = Operations(logicAPI, ui)
    o.get_report('financial')