from Presentation.Menu import format_function_name
from datetime import datetime, date
from math import floor
import os
''' Display methods for various data '''

class Display:
    def __init__(self):
        pass


    def display_all(self, data, fields):
        ''' Display all  '''
        field_lengths = self.find_header_format(data, fields)

        header = ''
        for field in fields:
            header += '| {:^{L}} '.format(field, L=field_lengths[field])
        print('\n\t\033[4m' + header + '|\033[0m')

        for el in data:
            obj = vars(el)
            line = ''
            for field in fields:
                line += '| {:^{L}} '.format(obj[field], L=field_lengths[field])
            print('\t'+line + '|')

    
    def display(self,data,fields,choice):
        '''Display after choice'''
        field_lengths = self.find_header_format(data, fields)
        header = ''
        for field in fields:
            header += '| {:^{L}} '.format(field, L=field_lengths[field])
        print('\n\t\033[4m' + header + '|\033[0m')
        for el in data:
            obj = vars(el)
            line = ''
            #for field in fields:
            for index,(key,val) in enumerate(obj.items()):
                index +=1
                if val == choice:
                    for field in fields:
                        line += '| {:^{L}} '.format(obj[field], L=field_lengths[field])
                    print('\t'+line + '|')
    
    def display_printable_version(self,data,fields,choice):
        ''' display printable version on screen '''
        field_lengths = self.find_header_format(data, fields)
        os.system('cls')# to clear window
        header = '\n\t\t\t\033[4mThis is printable version of contract with ID: {}\033[0m'.format(choice)
        print(header)
        for el in data:
            obj = vars(el)
            line = ''
            #for field in fields:
            for index,(key,val) in enumerate(obj.items()):
                index +=1
                if key == 'id' and val == choice:
                    for field in fields:
                        line += '\n\t\t| {:<30}|{:>30} |'.format(field,obj[field])
                    print(line)


    def display_all_fit_for_rental(self,data,fields):
        """displays all vehicle fit for rental"""
        field_lengths = self.find_header_format(data, fields)
        header = ''
        for field in fields:
            header += '| {:^{L}} '.format(field, L=field_lengths[field])
        print('\n\t\033[4m' + header + '|\033[0m')


        for el in data:
            obj = vars(el)
            state = 0
            status = 0
            line = ''
            for index,(key,val) in enumerate(obj.items()):
                    if val == 'Available':
                        state = 'Available'
                    if val == 'OK':
                        status = 'OK'
            if state == 'Available' and status == 'OK':
                for field in fields:
                    line += '| {:^{L}} '.format(obj[field], L=field_lengths[field])
                print('\t'+line + '|')
    


    def find_header_format(self, data, fields):
        field_lengths = {field: 0 for field in fields}
        
        for el in data:
            obj = vars(el)
            for field in fields:
                if len(obj[field]) > field_lengths[field]:
                    field_lengths[field] = len(obj[field])
                if len(field) > field_lengths[field]:
                    field_lengths[field] = len(field)

        return field_lengths

    def display_report(self, data, report_type):
        header = '\n\t\t\t{:^71}'.format(f'\033[4m{report_type} report\033[0m')
        print(header)

        for key,val in data.items():
            location_header = '\n\t\t\t{:_^71}\n'.format(f'\033[4m{format_function_name(key)}\033[0m')
            print(location_header)
            for (k,v) in val.items():
                if type(v) is dict:
                    var_line = '\n\t\t\t{:^71}\n'.format(f'\033[4m{k}\033[0m')
                    print(var_line)
                    for (keys,vals) in v.items():
                        value_line = '\t\t\t|{:-<30}|{:->30}|'.format(format_function_name(keys),vals)
                        print(value_line)
                else:
                    value_line = '\t\t\t|{:-<30}|{:->30}|'.format(format_function_name(k),v)
                    print(value_line)

    def display_invoice_report(self,data,state):
        header = '\n\t\t\t{:^71}'.format(f'\033[4mInvoice {state} report\033[0m')
        print(header)
        for key,val in data.items():
            cust_or_status = '\n\t\t\t{:_^71}\n'.format(f'\033[4m{format_function_name(key)}\033[0m')
            print(cust_or_status)
            
            for k,v in val.items():
                if state == 'customer':
                    contract_stat_name = '\n\t\t\t{:^71}\n'.format(f'\033[4mStatus: {format_function_name(k)}\033[0m')
                else:
                    contract_stat_name = '\n\t\t\t{:^71}\n'.format(f'\033[4mName: {format_function_name(k)}\033[0m')
                print(contract_stat_name)
                if not v.items():
                    empty = '\n\t\t\t{:^63}\n'.format(f'No contracts found')
                    print(empty)
                for keys,vals in v.items():
                    contract_id = '\n\t\t\t{:<71}\n'.format(f'Contract id: {format_function_name(keys)}')
                    print(contract_id)
                    for ks,vl in vals.items():
                        value_line = '\t\t\t|{:-<30}|{:->30}|'.format(format_function_name(ks),vl)
                        print(value_line)
    
    def display_invoice(self,data,status):
        """This function is to display invoice on screen"""
        if status == 'pay':
            d1 = datetime.fromisoformat(data['contract_start'])
            d2 = datetime.fromisoformat(data['contract_end'])
            days = (d2-d1).days

            header = '\t\t\t|{:_^43}|'.format(f'\033[4mReciept\33[0m')
            print('\n\t\t\t {:_>35}'.format(''))
            print(header)
            print('\t\t\t|{:^35}|'.format('NaN Air Rentals'))
            print('\t\t\t|{:^35}|'.format('Menntavegur 1'))
            print('\t\t\t|{:^35}|'.format('Reykjavík, Iceland'))
            print('\t\t\t|{:^35}|'.format('S: +354 599 6200'))
            print('\t\t\t|{:-^35}|'.format(''))
            print('\t\t\t|{: ^35}|'.format(''))
            print('\t\t\t|\033[4m{:<25}{:>10}\033[0m|'.format('Description','Amount'))
            print('\t\t\t| {:<34}|'.format(data['VIN'] + ' ' + data['vehicle_type']))
            print('\t\t\t|     {:<20}{:>9} |'.format(str(days) + ' days @ {}'.format(data['rate']), int(days)*int(data['rate'])))
            if data['late_fee'] is not None:
                lf1 = datetime.fromisoformat(data['contract_end'])            
                lf2 = datetime.fromisoformat(data['date_return'])
                lf = (lf2-lf1).days
                print('\t\t\t| {:<34}|'.format('Late Fee'))
                print('\t\t\t|     {:<20}{:>9} |'.format(str(lf) + ' days @ {}'.format(floor(int(data['rate'])*1.2)), floor(int(data['rate'])*int(lf)*1.2)))
            print('\t\t\t|{:-^35}|'.format(''))
            print('\t\t\t| {:<23}{:>10} |'.format('TOTAL',str(floor(float(data['total_price'])))))
            print('\t\t\t|{:^35}|'.format(''))
            print('\t\t\t| {:<23}{:>10} |'.format('CARD','-'+str(floor(float(data['total_price'])))))
            print('\t\t\t|   {:<32}|'.format('Mastercard'))
            print('\t\t\t|   {:<32}|'.format('xxxx xxxx xxxx 2064'))
            print('\t\t\t|{:^35}|'.format(''))
            print('\t\t\t|{:^35}|'.format('Thanks for choosing NaN Air!'))
            print('\t\t\t|{:_^35}|'.format(''))
        else: #if status is not pay 
            print('Invoice has been generated:')
            header = '\t\t\t|{:_^78}|'.format(f'\033[4mInvoice\33[0m')

            print('\n\t\t\t {:_>70}'.format(''))
            print(header)
            print('\t\t\t|{:^70}|'.format(''))
            print('\t\t\t|{:>69} |'.format('NaN Air Rentals'))
            print('\t\t\t|{:>69} |'.format('Menntavegur 1'))
            print('\t\t\t|{:>69} |'.format('Reykjavík, Iceland'))
            print('\t\t\t|{:>69} |'.format('S: +354 599 6200'))
            print('\t\t\t|{:>69} |'.format('NaN@NaNAir.com'))
            print('\t\t\t|{:>69} |'.format('NaNAir.com'))
            
            for i in range(2):
                print('\t\t\t|{: ^70}|'.format(' '))
            
            print('\t\t\t|{:<70}|'.format('BILL TO'))
            print('\t\t\t| {:<34}{:>34} |'.format('Customer id: {}'.format(data['customer_id']),'Contract id: {}'.format(data['id'])))
            print('\t\t\t| {:<69}|'.format(data['customer_name']))
            print('\t\t\t| {:<69}|'.format(data['address']))
            print('\t\t\t|{: ^70}|'.format(''))
            print('\t\t\t|{:-^70}|'.format(''))
            print('\t\t\t|{:^14}|{:^19}|{:^7}|{:^12}|{:^14}|'.format('DATE','PRODUCT','RATE','LATE FEE','AMOUNT'))
            print('\t\t\t|{:-^70}|'.format(''))
            print('\t\t\t|{:^14}|{:^19}|{:^7}|{:^12}|{:^14}|'.format(data['date_return'],data['VIN'] + ' ' + data['vehicle_type'],data['rate'],floor(float(data['late_fee'])),floor(float(data['total_price']))))
            print('\t\t\t|{:-^70}|'.format(''))
            print('\t\t\t|{:>69} |'.format('TOTAL: {}'.format(floor(floor(data['total_price'])))))
            print('\t\t\t|{:_^70}|'.format(''))
