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

                return (days_late * int(rate)) + ((days_late * int(rate)) * 0.2)

            except ValueError:
                d1 = datetime.fromisoformat(contract_end)
                d2 = datetime.today()
                days_late = (d2-d1).days

                if days_late < 1 : return 0

                return (days_late * int(rate)) + ((days_late * int(rate)) * 0.2)


def calculate_base_price(start, end, rate):
    d1 = datetime.fromisoformat(start)
    d2 = datetime.fromisoformat(end)
    return (d2-d1).days * int(rate)




def calculate_total_price(contract):
    contract_start = contract['contract_start']
    contract_end = contract['contract_end']
    date_return = contract['date_return']
    rate = contract['rate']

    late_fee = calculate_late_fee(rate, contract_end, date_return)
    base_price = calculate_base_price(contract_start, contract_end, rate)
    
    return late_fee + base_price