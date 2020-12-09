from Logic.form_calculators import *

class Invoice_Manager:
    def __init__(self, dapi, sapi, lapi):
        self.dapi = dapi
        self.sapi = sapi
        self.lapi = lapi


    def generate_invoice(self, id):
        contract = vars(self.sapi.search_contract().by_id(str(id))[0])
        rate = contract['rate']
        contract_end = contract['contract_end']
        date_return = contract['date_return']
        contract_start = contract['contract_start']
        contract_end = contract['contract_end']

        # days, vehicle type
        # Generate invoice
        invoice = {
            'price'      : calculate_base_price(contract_start, contract_end, rate),
            'late_fee'   : calculate_late_fee(rate, contract_end, date_return),
            'total_price': calculate_total_price(contract),
        }

        # Edit contract
        contract['state'] = 'Completed'
        self.lapi.contract.edit(contract, str(id))

        return invoice