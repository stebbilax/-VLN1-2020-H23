from datetime import datetime, date
from Logic.form_calculators import *

class Report_Generator:
    def __init__(self, dapi, sapi):
        self.Data = dapi
        self.Search = sapi


    def financial_report(self, time_from=None, time_to=None):
        contracts = [vars(contract) for contract in self.Data.read_all_contracts()]
        report = {}
        overall_income = 0


        if time_from != None: contracts = select_time_period(contracts, time_from, time_to)


        for contract in contracts:
            location = contract['location_handover']
            contract_end = contract['contract_end']
            date_return = contract['date_return']
            rate = contract['rate']
            
            total_price = calculate_total_price(contract)

            # Create a entry for each location
            if location not in report: report[location] = {
                'valid'             : 0,
                'invalid'           : 0,
                'awaiting payment'  : 0,
                'complete'          : 0,
                'total_income'      : 0,
            }

            # Creates fields for total price of valid, invalid and completed contracts
            field = None
            if contract['state'].lower() == 'valid': field = 'valid'
            if contract['state'].lower() == 'invalid': field = 'invalid'
            if contract['state'].lower() == 'awaiting payment': field = 'awaiting payment'
            if contract['state'].lower() == 'completed': field = 'completed'

            if field in report[location]:
                report[location][field] += total_price
                if field != 'invalid':
                    report[location]['total_income'] += total_price
                    overall_income += total_price

            
        report['net_income'] = {'net_income': overall_income}
        
        return report



    def vehicle_report(self,time_from=None,time_to=None):
        contracts = self.Data.read_all_contracts()
        vehicles = self.Data.read_all_vehicles()
        report = {}
        
        # Run over every vehicle in database
        for vehicle in vehicles:
            vehicle = vars(vehicle)

            if vehicle:
                airport = vehicle['airport']
                v_type = vehicle['type']
                model = vehicle['model']
                state = vehicle['vehicle_state']
                status = vehicle['vehicle_status']
                
                # Initial setup for new locations and types
                if airport not in report: report[airport] = {}
                if v_type not in report[airport]:
                    report[airport][v_type] = {}
                    report[airport][v_type]['total_times_loaned'] = 0
                    report[airport][v_type]['currently_on_loan'] = 0
                    report[airport][v_type]['currently_available'] = 0
                    report[airport][v_type]['currently_in_repair'] = 0

                if status == 'Available' and state == 'OK': 
                    report[airport][v_type]['currently_available'] += 1
                if status == 'Available' and state == 'DEFECTIVE':
                    report[airport][v_type]['currently_in_repair'] += 1
                if status == 'Unavailable' and state == 'DEFECTIVE':
                    report[airport][v_type]['currently_in_repair'] += 1
                if status == 'Unavailable' and state == 'OK':
                    report[airport][v_type]['currently_on_loan'] += 1

        
        # Run over every vehicle mentioned in contracts
        for contract in contracts:
            contract_id = vars(contract)['vehicle_id']
            vehicle = vars(self.Search.search_vehicle().by_id(contract_id)[0])

            airport = vehicle['airport']
            v_type = vehicle['type']
            model = vehicle['model']
            state = vehicle['vehicle_state']
            status = vehicle['vehicle_status']

            # Add to total_times_loaned variable for each location and type
            report[airport][v_type]['total_times_loaned'] += 1


        def get_vehicle_stats(obj):
            # Add extra fields to each airport
            for airport, fields in obj.items():
                most_popular_vehicle        = 'None'
                most_popular_num            = 0
                total_vehicles_in_use       = 0
                total_vehicles_in_repair    = 0
                total_vehicles_available    = 0

                
                
                for field in fields:
                    current_loan   =    int(obj[airport][field]['currently_on_loan'])
                    current_avail  =    int(obj[airport][field]['currently_available'])
                    current_repair =    int(obj[airport][field]['currently_in_repair'])
                    total          =    int(obj[airport][field]['total_times_loaned'])

                    total_vehicles_in_use       += current_loan
                    total_vehicles_in_repair    += current_repair
                    total_vehicles_available    += current_avail
                    
                    if total > most_popular_num: most_popular_vehicle = field

                obj[airport]['location_stats'] = {
                    'most_popular_vehicle':None,
                    'total_vehicles_in_use':0,
                    'total_vehicles_in_repair':0,
                    'total_vehicles_available':0,
                }

                obj[airport]['location_stats']['most_popular_vehicle'] = most_popular_vehicle
                obj[airport]['location_stats']['total_vehicles_in_use'] = total_vehicles_in_use
                obj[airport]['location_stats']['total_vehicles_in_repair'] = total_vehicles_in_repair
                obj[airport]['location_stats']['total_vehicles_available'] = total_vehicles_available
                
            return obj

        report = get_vehicle_stats(report)

        return report
            


    def invoice_report_by_state(self, time_from=None, time_to=None):
        contracts = [vars(contract) for contract in self.Data.read_all_contracts()]
        if time_from != None: contracts = select_time_period(contracts, time_from, time_to)
        
        report = {
            'Awaiting Payment' : {},
            'Completed' : {}
        }
        for contract in contracts:

            country = contract['country']
            customer_id = contract['customer_id']
            customer_name = contract['customer_name']
            date_handover = contract['date_handover']
            date_return = contract['date_return']
            contract_start = contract['contract_start']
            contract_end = contract['contract_end']
            rate = contract['rate']
            state = contract['state']
            id = contract['id']

            if state == 'Awaiting Payment' or state == 'Completed':
                    if customer_name not in report[state]: report[state][customer_name] = {}
                    report[state][customer_name][id] = {
                        'price'      : calculate_base_price(contract_start, contract_end, rate),
                        'late_fee'   : calculate_late_fee(rate, contract_end, date_return),
                        'total_price': calculate_total_price(contract),
                    }

        return report

    
    def invoice_report_by_customer(self, time_from=None, time_to=None):
        contracts = [vars(contract) for contract in self.Data.read_all_contracts()]
        if time_from != None: contracts = select_time_period(contracts, time_from, time_to)
        
        report = {
            
        }
        for contract in contracts:

            country = contract['country']
            customer_id = contract['customer_id']
            customer_name = contract['customer_name']
            date_handover = contract['date_handover']
            date_return = contract['date_return']
            contract_start = contract['contract_start']
            contract_end = contract['contract_end']
            rate = contract['rate']
            state = contract['state']
            id = contract['id']

            if state == 'Awaiting Payment' or state == 'Completed':
                    if customer_name not in report: report[customer_name] = {'Awaiting Payment':{}, 'Completed':{}}
                    report[customer_name][state][id] = {
                        'price'      : calculate_base_price(contract_start, contract_end, rate),
                        'late_fee'   : calculate_late_fee(rate, contract_end, date_return),
                        'total_price': calculate_total_price(contract),
                    }

        return report
            

           