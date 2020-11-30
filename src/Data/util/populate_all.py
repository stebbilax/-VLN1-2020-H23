import os
import csv
from configparser import ConfigParser
from Dummy import Dummy

D = Dummy()
directory = os.getcwd()


file = '../config.ini'
config = ConfigParser()
config.read(file)

contract_fields = config['fields']['contract_fields'].split(',')
customer_fields = config['fields']['customer_fields'].split(',')
destination_fields = config['fields']['destination_fields'].split(',')
employee_fields = config['fields']['employee_fields'].split(',')
vehicle_fields = config['fields']['vehicle_fields'].split(',')

def contract():
    return {
        'name' : D.make_name(),
        'phone' : D.make_phone(),
        'address' : D.make_address(),
        'email' : D.make_email(),
        'date_from' : D.make_early_date(),
        'date_to' : D.make_later_date(),
        'vehicle_id' : D.make_vehicle_id(),
        'country' : D.make_country(),
        'vehicle_status' : D.make_vehicle_status(),
        'employee_id' : D.make_employee_id(),
        'loan_date' : D.make_early_date(),
        'return_date' : D.make_later_date(),
        'total' : D.make_total(),
        'loan_status' : D.make_loan_status()
    }
def customer():
    return {
        'name' : D.make_name(),
        'ssn' : D.make_ssn(),
        'address' : D.make_address(),
        'postal_code' : D.make_postal_code(),
        'phone' : D.make_phone(),
        'email' : D.make_email(),
        'country' : D.make_country()
    }
def destination():
    return {
        'country' : D.make_country(),
        'airport' : D.make_airport(),
        'phone' : D.make_phone(),
        'opening_hours' : D.make_opening_hours(),
    }

def employee():
    return {
        'name' : D.make_name(),
        'address' : D.make_address(),
        'postal_code' : D.make_postal_code(),
        'ssn' : D.make_ssn(),
        'phone' : D.make_phone(),
        'mobile_phone' : D.make_phone(),
        'email' : D.make_email(),
        'title' : D.make_title(),
        'location' : D.make_airport(),
        'country' : D.make_country(),
    }
def vehicle():
    return {
        'type' : D.make_type(),
        'manufacturer' : D.make_manufacturer(),
        'yom' : D.make_yom(),
        'color' : D.make_color(),
        'req_rights' : D.make_req_rights(),
        'location' : D.make_airport(),
        'condition' : D.make_vehicle_status(),
        'model' : D.make_model(),
    }



def pop_contract(num_of_lines):
    with open(f'../data/contracts.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=contract_fields)
            writer.writeheader()
            for _ in range(num_of_lines):
                line_obj = contract()
                writer.writerow(line_obj)


def pop_customer(num_of_lines):
    with open(f'../data/customers.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=customer_fields)
            writer.writeheader()
            for _ in range(num_of_lines):
                line_obj = customer()
                writer.writerow(line_obj)


def pop_country(num_of_lines):
    with open(f'../data/destinations.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=destination_fields)
            writer.writeheader()
            for _ in range(num_of_lines):
                line_obj = destination()
                writer.writerow(line_obj)


def pop_employee(num_of_lines):
    with open(f'../data/employees.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=employee_fields)
            writer.writeheader()
            for _ in range(num_of_lines):
                line_obj = employee()
                writer.writerow(line_obj)

def pop_vehicle(num_of_lines):
    with open(f'../data/vehicles.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=vehicle_fields)
            writer.writeheader()
            for _ in range(num_of_lines):
                line_obj = vehicle()
                writer.writerow(line_obj)




def pop_all(n):
    pop_contract(n)
    pop_customer(n)
    pop_country(n)
    pop_employee(n)
    pop_vehicle(n)


if __name__ == '__main__':
    pop_all(10)







    
        

