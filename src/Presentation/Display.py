from Presentation.Menu import format_function_name
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
        ''' display printable ersion on screen '''
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
    


    def display_for_papa_chuck(self,data,fields,choice):
        '''This is for some papa chuck dinero'''
        pass



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
        if status == 'pay':
            header = '\t\t\t|{:_^70}|'.format(f'\033[4mInvoice Reciept\33[0m')
        else:
            print('Invoice has been generated:')
            header = '\t\t\t|{:_^78}|'.format(f'\033[4mInvoice\33[0m')

            print('\n\t\t\t {:_>70}'.format(''))
            print(header)
            print('\t\t\t|{:>70}|'.format(f'NaN Air Rentals'))
            print('\t\t\t|{:>70}|'.format(f'Menntavegur 1'))
            print('\t\t\t|{:>70}|'.format(f'+354 599 6200'))
            print('\t\t\t|{:>70}|'.format(f'NaN@NaNAir.com'))
            print('\t\t\t|{:>70}|'.format(f'NaNAir.com'))
            
            for i in range(3):
                print('\t\t\t|{: ^70}|'.format(' '))
            print('\t\t\t|{:<70}|'.format('BILL TO'))
            
            print('\t\t\t|{:<35}{:>35}|'.format('Customer id: {}'.format(data['customer_id']),'Contract id: {}'.format(data['id'])))
            print('\t\t\t|{:<70}|'.format(data['customer_name']))
            print('\t\t\t|{:<70}|'.format(data['address']))
            print('\t\t\t|{: ^70}|'.format(''))
            print('\t\t\t|{:-^70}|'.format(''))
            print('\t\t\t|{:^14}|{:^14}|{:^10}|{:^14}|{:^14}|'.format('DATE','PRODUCT','RATE','LATE FEE','AMOUNT'))
            print('\t\t\t|{:-^70}|'.format(''))
            print('\t\t\t|{:^14}|{:^14}|{:^10}|{:^14}|{:^14}|'.format(data['date_return'],data['VIN'],data['rate'],data['late_fee'],data['total_price']))
            print('\t\t\t|{:-^70}|'.format(''))
            print('\t\t\t|{:>70}|'.format('TOTAL: {}'.format(data['total_price'])))
            print('\t\t\t|{:_^70}|'.format(''))
