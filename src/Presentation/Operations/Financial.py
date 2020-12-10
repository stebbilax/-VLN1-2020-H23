''' Operations calling the financial logic API '''

from Presentation.Operations.Generic import *

def get_financial_report(logicAPI, ui):
    o = Operations(logicAPI, ui)
    time_from = input('Time from (ex. 2020-01-01): ')
    time_to = input('Time to (ex. 2020-10-10): ')
    o.get_report('financial',time_from,time_to)