from datetime import datetime, date

def calculate_late_fee(rate, contract_end, date_return):
            ''' Calculates late fee
            For every given contract, adds 20% of the rate on top of the original rate for every
            day that has passed the contract_end date. If vehicle has not been returned
            the function returns late fee as it would be as of date of calculation '''
            
            try:
                d1 = datetime.fromisoformat(contract_end)
                d2 = datetime.fromisoformat(date_return)
                days_late = (d2-d1).days

                if days_late < 1 : return 0

                return ((days_late * int(rate)) * 0.2)

            except ValueError:
                #if date return has not been listed late fee wont be calculated
                d1 = datetime.fromisoformat(contract_end)
                d2 = datetime.today()
                days_late = (d2-d1).days

                if days_late < 1 : return 0

                return ((days_late * int(rate)) * 0.2)


def calculate_base_price(start, end, rate):
    """Calculates price of vehicle (this does not include late return fee) 
       tries to calculate base price from date handout and date return,
       if date handover has been given but not date return it calculates the total cost until this day
       if they are not found then returnes rate """
    try:
        d1 = datetime.fromisoformat(start)
        d2 = datetime.fromisoformat(end)
        return (d2-d1).days * int(rate)
    except ValueError:
        #base price wont be calculated until date_handout and date_return on contract has been made
        if start == 'N/A' and end == 'N/A':
            return int(rate)
        else: 
            d1 = datetime.fromisoformat(start)
            d2 = datetime.today()
            return (d2-d1).days * int(rate)




def calculate_total_price(contract):
    """Calculations of total price"""
    contract_start = contract['contract_start']
    contract_end = contract['contract_end']
    date_return = contract['date_return']
    date_handover = contract['date_handover']
    rate = contract['rate']

    #late fee calculated as the day the contract ended versus the return date of the vehicle
    late_fee = calculate_late_fee(rate, contract_end, date_return)  
    #base fee calculated from day wehicle was handed over vs day it was returned 
    base_price = calculate_base_price(date_handover, date_return, rate)
    
    return late_fee + base_price



def select_time_period(contracts, date_from, date_to):
            '''Recieves contracts and a start and end date.
            Filters out any contract that does not fit within the 
            given time frame and returns the filtered list
            '''
            date_from = datetime.fromisoformat(date_from)
            date_to = datetime.fromisoformat(date_to)
            new_contracts = []
            for contract in contracts:
                contract_start = datetime.fromisoformat(contract['contract_start'])
                contract_end = datetime.fromisoformat(contract['contract_end'])

                # Check if contract fits in the given window
                if contract_start <= date_from: continue
                if contract_end >= date_to: continue

                new_contracts.append(contract)

            return new_contracts