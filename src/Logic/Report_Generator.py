from Data.DataAPI import DataAPI
from datetime import datetime, date

class Report_Generator:
    def __init__(self):
        self.Data = DataAPI()


    def financial_report(self, time_from=None, time_to=None):
        contracts = [vars(contract) for contract in self.Data.read_all_contracts()]
        report = {}

        def calculate_late_fee(rate, contract_end, date_return):
            ''' Calculates late fee
            For every given contract, adds 20% of the original rate for every
            day that has passed the contract_end date. If vehicle has not been returned
            the function returns late fee as it would be as of date of calculation '''
            
            try:
                d1 = datetime.fromisoformat(contract_end)
                d2 = datetime.fromisoformat(date_return)
                days_late = (d2-d1).days

                if days_late < 1 : return 0

                return (int(rate) * 0.20) * days_late

            except ValueError:
                d1 = datetime.fromisoformat(contract_end)
                d2 = datetime.today()
                days_late = (d2-d1).days

                if days_late < 1 : return 0

                return (int(rate) * 0.20) * days_late

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

        if time_from != None: contracts = select_time_period(contracts, time_from, time_to)


        for contract in contracts:
            location = contract['location_handover']
            contract_end = contract['contract_end']
            date_return = contract['date_return']
            rate = contract['rate']
            late_fee = calculate_late_fee(rate, contract_end, date_return)
            total_price = int(rate) + late_fee

            # Create a entry for each location
            if location not in report: report[location] = {}

            # Creates fields for total price of valid, invalid and completed contracts
            field = None
            if contract['state'].lower() == 'valid': field = f'{location}_valid'
            if contract['state'].lower() == 'invalid': field = f'{location}_invalid'
            if contract['state'].lower() == 'completed': field = f'{location}_completed'
                

            if field in report[location]:
                report[location][field] += total_price
            else:
                 report[location][field] = total_price
        for k, v in report.items():
            print(k, v)
        return report


    def vehicle_report(self):
        pass


    def invoice_report(self):
        pass




r = {
    'nuuk_completed_profit': 500,
    'nuuk_awaited_profit': 500,
    'nuuk_total_profit': 400,
    'most profitable vehicle': 
    'least profitable vehicle'
}