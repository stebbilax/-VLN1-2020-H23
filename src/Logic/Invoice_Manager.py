from Logic.form_calculators import *

class Invoice_Manager:
    def __init__(self, dapi, sapi, lapi):
        self.dapi = dapi
        self.sapi = sapi
        self.lapi = lapi


    def generate_invoice(self, id):
        res = self.sapi.search_contract().by_id(str(id))
        if res == []: return {}
        contract = vars(res[0])


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
        contract['state']       = 'Awaiting Payment'
        contract['rate']       = invoice['price']
        contract['late_fee']    = invoice['late_fee']
        contract['total_price'] = invoice['total_price']
        self.lapi.contract.edit(contract, str(id))

        return invoice



    def pay_invoice(self, id):
        res = self.sapi.search_contract().by_id(str(id))
        if res == []: return False


        contract = vars(res[0])
        
        if contract['state'] == 'Completed': return 'Invoice already paid'
        if contract['state'] != 'Awaiting Payment': return 'Must generate invoice before paying it'

        receipt = {
            'type': contract['vehicle_type'],
            'country': contract['country'],
            'price': contract['rate'],
            'late_fee': contract['late_fee'],
            'total_price': contract['total_price'],
            'date_from' : contract['date_handover'],
            'date_to' : contract['date_return']
        }

        contract['state'] = 'Completed'
        self.lapi.contract.edit(contract, str(id))

        return receipt