from Logic.form_calculators import *

class Invoice_Manager:
    def __init__(self, dapi, sapi, lapi):
        self.dapi = dapi #dataAPI
        self.sapi = sapi #searchAPI
        self.lapi = lapi #logicAPI


    def generate_invoice(self, id):
        """Generates an invoice for the customer
        Only works for a valid contract that has not been paid or invalidated"""

        #If contract does not exist, return False
        res = self.sapi.search_contract().by_id(str(id))
        if res == []: return False
        
        contract = vars(res[0])
        if contract['state'] == 'Completed': 
            return False
        if contract['state'] == 'Invalid': 
            return False

        # Find corresponding customer and vehicle
        res = self.sapi.search_customer().by_id(contract['customer_id'])
        cust = vars(res[0])
        res = self.sapi.search_vehicle().by_id(contract['vehicle_id'])
        veh = vars(res[0])

        rate = contract['rate']
        contract_end = contract['contract_end']
        date_return = contract['date_return']
        contract_start = contract['contract_start']
        contract_end = contract['contract_end']
 
        # Generate invoice
        invoice = {
            'state'             : contract['state'],
            'address'           : cust['address'],
            'VIN'               : veh['vehicle_authentication'],
            'customer_id'       : contract['customer_id'],
            'id'                : contract['id'],
            'customer_name'     : contract['customer_name'],
            'phone'             : contract['phone'],
            'email'             : contract['email'],
            'phone'             : contract['phone'],
            'vehicle_type'      : contract['vehicle_type'],
            'date_handover'     : contract['date_handover'],
            'date_return'       : contract['date_return'],
            'location_handover' : contract['location_handover'],
            'location_return'   : contract['location_return'],
            'country'           : contract['country'],
            'rate'              : contract['rate'],
            'price'             : calculate_base_price(contract_start, contract_end, rate),
            'late_fee'          : calculate_late_fee(rate, contract_end, date_return),
            'total_price'       : calculate_total_price(contract),
            'date_from'         : contract['date_handover'],
            'date_to'           : contract['date_return'],
            'contract_start'    : contract['contract_start'],
            'contract_end'      : contract['contract_end']
        }


        # Edit contract to reflect that an invoice has been generated for it
        contract['state']       = 'Awaiting Payment'
        contract['late_fee']    = invoice['late_fee']
        contract['total_price'] = invoice['total_price']
        self.lapi.contract.edit(contract, str(id))

        return invoice



    def pay_invoice(self, id):
        """Generates an invoice receipt for the customer
        Only works for a contract who's invoice has already been generated"""
        # If contract does not exist return False
        res = self.sapi.search_contract().by_id(str(id))
        if res == []: return False

        # Check if contract has a corresponding invoice already generated
        contract = vars(res[0])
        if contract['state'] != 'Awaiting Payment': 
            return False
            
        # Find customer and vehicle
        res = self.sapi.search_customer().by_id(contract['customer_id'])
        cust = vars(res[0])
        res = self.sapi.search_vehicle().by_id(contract['vehicle_id'])
        veh = vars(res[0])

        # Generate receipt
        receipt = {
            'state'             : contract['state'],
            'address'           : cust['address'],
            'VIN'               : veh['vehicle_authentication'],
            'customer_id'       : contract['customer_id'],
            'id'                : contract['id'],
            'customer_name'     : contract['customer_name'],
            'phone'             : contract['phone'],
            'email'             : contract['email'],
            'phone'             : contract['phone'],
            'vehicle_type'      : contract['vehicle_type'],
            'date_handover'     : contract['date_handover'],
            'date_return'       : contract['date_return'],
            'location_handover' : contract['location_handover'],
            'location_return'   : contract['location_return'],
            'country'           : contract['country'],
            'rate'              : contract['rate'],
            'late_fee'          : contract['late_fee'],
            'total_price'       : contract['total_price'],
            'date_from'         : contract['date_handover'],
            'date_to'           : contract['date_return'],
            'contract_start'    : contract['contract_start'],
            'contract_end'      : contract['contract_end']
        }

        # Return an error if fields are not in order
        if receipt['date_from'] == 'N/A': return False
        if receipt['date_to'] == 'N/A': return False
        if receipt['date_handover'] == 'N/A': return False
        if receipt['date_return'] == 'N/A': return False

        # Mark contract as having been paid
        contract['state'] = 'Completed'
        self.lapi.contract.edit(contract, str(id))

        return receipt