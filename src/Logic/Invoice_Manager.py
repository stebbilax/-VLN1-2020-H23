from Logic.form_calculators import *
from Presentation.Menu import format_function_name
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
        if contract['state'] == 'Completed': return ('Contract has already been paid', False)
        if contract['state'] == 'Invalid': return ('Invoice is invalidated',False)

        # Return an error if fields are not in order
        checklist = ['date_handover','date_return', 'time_handover','time_return']
        s = 'Contract is missing the following information: '
        goback = False
        for item in checklist:
            if contract[item] == 'N/A':
                s += format_function_name(item) + ', '
                goback = True
        
        s = s[:-2]
        if goback:
            return (s, False)
        
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

        if contract['state'] == 'Awaiting Payment':
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
            'late_fee'          : contract['late_fee'],
            'total_price'       : contract['total_price'],
            'contract_start'    : contract['contract_start'],
            'contract_end'      : contract['contract_end']
        }
        else:
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
        contract = vars(res[0])

        # Check if contract has a corresponding invoice already generated
        if contract['state'] == 'Completed': return ('Contract has already been paid'.format(id),False)
        if contract['state'] != 'Awaiting Payment': return ('Invoice has not been generated for contract {}'.format(id),False)
            
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
            'contract_start'    : contract['contract_start'],
            'contract_end'      : contract['contract_end']
        }

        # Return an error if fields are not in order
        checklist = ['date_handover','date_return', 'time_handover','time_return']
        s = 'Contract is missing the following information: '
        goback = False
        for item in checklist:
            if contract[item] == 'N/A':
                s += format_function_name(item) + ', '
                goback = True
        
        s = s[:-2]
        if goback:
            return (s, False)
        

        # Mark contract as having been paid
        contract['state'] = 'Completed'
        self.lapi.contract.edit(contract, str(id))

        return receipt