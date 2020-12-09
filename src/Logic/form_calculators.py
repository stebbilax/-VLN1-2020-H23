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