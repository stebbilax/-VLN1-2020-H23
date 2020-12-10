''' Operations calling the financial logic API '''

from Presentation.Operations.Generic import *
import re

def get_financial_report(logicAPI, ui):
    o = Operations(logicAPI, ui)
    res = get_choice()
    if res == 'b': return
    if res == '2':
        time_from = get_time_format('Date from: ')
        if time_from == 'b': return

        time_to = get_time_format('Date To: ')
        if time_to == 'b': return

        o.get_report('financial',time_from,time_to)
    
    if res == '1':
        o.get_report('financial',None,None)




def get_time_format(msg):
    match = None

    while not match:
        print('Please enter time in valid format (Example: 2020-01-01)')
        res = input(msg)

        if res == 'b' or res == 'B':
            return 'b'

        match = re.search('\d{4}-(([1][0-2])|([0][1-9]))-(([0-2][\d])|([3][01]))', res)
        if match: return res


def get_choice():
    res = None
    print('How would you like to search?')

    while res != '1' and res != '2' and res != 'b':
        print('1. Over all contracts')
        print('2. By time period.')
        print('b. Back.')
        res = input('Enter choice: ')

    return res

