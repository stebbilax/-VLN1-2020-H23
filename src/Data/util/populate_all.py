import os
import sys
import csv
from random import randint
from configparser import ConfigParser
from Dummy import Dummy


sys.path.append(os.getcwd())
from Data.DataAPI import DataAPI
from Models.Contract import Contract
from Models.Customer import Customer
from Models.Destination import Destination
from Models.Employee import Employee
from Models.Vehicle import Vehicle
from Models.Vehicle_Type import Vehicle_Type

# Must be in src folder to use


D = Dummy()
directory = os.getcwd()


file = 'Data/config.ini'
config = ConfigParser()
config.read(file)

contract_fields = config['fields']['contract_fields'].split(',')
customer_fields = config['fields']['customer_fields'].split(',')
destination_fields = config['fields']['destination_fields'].split(',')
employee_fields = config['fields']['employee_fields'].split(',')
vehicle_fields = config['fields']['vehicle_fields'].split(',')
vehicle_type_fields = config['fields']['vehicle_type_fields'].split(',')

DB = DataAPI()


def contract():
    return Contract(
        D.make_name(),
        D.make_phone(),
        D.make_address(),
        D.make_email(),
        D.make_early_date(),
        D.make_later_date(),
        D.make_vehicle_id(),
        D.make_country(),
        D.make_vehicle_status(),
        D.make_employee_id(),
        D.make_early_date(),
        D.make_later_date(),
        D.make_total(),
        D.make_loan_status(),
    )
def customer():
    return Customer(
        D.make_name(),
        D.make_ssn(),
        D.make_address(),
        D.make_postal_code(),
        D.make_phone(),
        D.make_email(),
        D.make_country(),
        D.make_licence(),
    )
def destination():
    return Destination(
        D.make_country(),
        D.make_airport(),
        D.make_phone(),
        D.make_opening_hours(),
    )

def employee():
    return Employee(
        D.make_name(),
        D.make_address(),
        D.make_postal_code(),
        D.make_ssn(),
        D.make_phone(),
        D.make_phone(),
        D.make_email(),
        D.make_title(),
        D.make_airport(),
        D.make_country(),
    )
def vehicle():
    return Vehicle(
        D.make_type(),
        D.make_manufacturer(),
        D.make_yom(),
        D.make_color(),
        D.make_licence(),
        D.make_airport(),
        D.make_vehicle_status(),
        D.make_model(),

    )
def vehicle_type():
    return Vehicle_Type(
        D.make_type(),
        D.make_country(),
        1337,

    )



def pop_contract(num_of_lines):
    arr = []
    for _ in range(num_of_lines):
        arr.append(contract())

    DB.write_all_contracts(arr)


def pop_customer(num_of_lines):
    arr = []
    for _ in range(num_of_lines):
        arr.append(customer())

    DB.write_all_customers(arr)


def pop_destination(num_of_lines):
    arr = []
    for _ in range(num_of_lines):
        arr.append(destination())

    DB.write_all_destinations(arr)
    

def pop_employee(num_of_lines):
    arr = []
    for _ in range(num_of_lines):
        arr.append(employee())

    DB.write_all_employees(arr)

    
def pop_vehicle(num_of_lines):
    arr = []
    for _ in range(num_of_lines):
        arr.append(vehicle())

    DB.write_all_vehicles(arr)
    

def pop_vehicle_type(num_of_lines):
    arr = []
    for _ in range(num_of_lines):
        arr.append(vehicle_type())

    DB.write_all_vehicle_types(arr)
    

def pop_all(n):
    pop_contract(n)
    pop_customer(n)
    pop_destination(n)
    pop_employee(n)
    pop_vehicle(n)
    pop_vehicle_type(n)


if __name__ == '__main__':
    pop_all(20)



## Old version that writes directly to database

# def contract():
#     return {
#         'id' : D.make_id(),
#         'name' : D.make_name(),
#         'phone' : D.make_phone(),
#         'address' : D.make_address(),
#         'email' : D.make_email(),
#         'date_from' : D.make_early_date(),
#         'date_to' : D.make_later_date(),
#         'vehicle_id' : D.make_vehicle_id(),
#         'country' : D.make_country(),
#         'vehicle_status' : D.make_vehicle_status(),
#         'employee_id' : D.make_employee_id(),
#         'loan_date' : D.make_early_date(),
#         'return_date' : D.make_later_date(),
#         'total' : D.make_total(),
#         'loan_status' : D.make_loan_status()
#     }
# def customer():
#     return {
#         'id' : D.make_id(),
#         'name' : D.make_name(),
#         'ssn' : D.make_ssn(),
#         'address' : D.make_address(),
#         'postal_code' : D.make_postal_code(),
#         'phone' : D.make_phone(),
#         'email' : D.make_email(),
#         'country' : D.make_country(),
#         'licence' : D.make_licence()
#     }
# def destination():
#     return {
#         'id' : D.make_id(),
#         'country' : D.make_country(),
#         'airport' : D.make_airport(),
#         'phone' : D.make_phone(),
#         'opening_hours' : D.make_opening_hours(),
#     }

# def employee():
#     return {
#         'id' : D.make_id(),
#         'name' : D.make_name(),
#         'address' : D.make_address(),
#         'postal_code' : D.make_postal_code(),
#         'ssn' : D.make_ssn(),
#         'phone' : D.make_phone(),
#         'mobile_phone' : D.make_phone(),
#         'email' : D.make_email(),
#         'title' : D.make_title(),
#         'airport' : D.make_airport(),
#         'country' : D.make_country(),
#     }
# def vehicle():
#     return {
#         'id' : D.make_id(),
#         'type' : D.make_type(),
#         'manufacturer' : D.make_manufacturer(),
#         'yom' : D.make_yom(),
#         'color' : D.make_color(),
#         'licence' : D.make_licence(),
#         'airport' : D.make_airport(),
#         'condition' : D.make_vehicle_status(),
#         'model' : D.make_model(),
#     }

# def vehicle_type():
#     return {
#         'id' : D.make_id(),
#         'name': D.make_type(),
#         'regions': D.make_country(),
#         'rate' : 1337
#     }



# def pop_contract(num_of_lines):
#     with open(f'Data/data/contracts.csv', 'w', newline='', encoding='utf-8') as f:
#             writer = csv.DictWriter(f, fieldnames=contract_fields)
#             writer.writeheader()
#             for _ in range(num_of_lines):
#                 line_obj = contract()
#                 writer.writerow(line_obj)


# def pop_customer(num_of_lines):
#     with open(f'Data/data/customers.csv', 'w', newline='', encoding='utf-8') as f:
#             writer = csv.DictWriter(f, fieldnames=customer_fields)
#             writer.writeheader()
#             for _ in range(num_of_lines):
#                 line_obj = customer()
#                 writer.writerow(line_obj)


# def pop_country(num_of_lines):
#     with open(f'Data/data/destinations.csv', 'w', newline='', encoding='utf-8') as f:
#             writer = csv.DictWriter(f, fieldnames=destination_fields)
#             writer.writeheader()
#             for _ in range(num_of_lines):
#                 line_obj = destination()
#                 writer.writerow(line_obj)


# def pop_employee(num_of_lines):
#     with open(f'Data/data/employees.csv', 'w', newline='', encoding='utf-8') as f:
#             writer = csv.DictWriter(f, fieldnames=employee_fields)
#             writer.writeheader()
#             for _ in range(num_of_lines):
#                 line_obj = employee()
#                 writer.writerow(line_obj)

# def pop_vehicle(num_of_lines):
#     with open(f'Data/data/vehicles.csv', 'w', newline='', encoding='utf-8') as f:
#             writer = csv.DictWriter(f, fieldnames=vehicle_fields)
#             writer.writeheader()
#             for _ in range(num_of_lines):
#                 line_obj = vehicle()
#                 writer.writerow(line_obj)

# def pop_vehicle_type(num_of_lines):
#     with open(f'Data/data/vehicle_types.csv', 'w', newline='', encoding='utf-8') as f:
#             writer = csv.DictWriter(f, fieldnames=vehicle_type_fields)
#             writer.writeheader()
#             for _ in range(num_of_lines):
#                 line_obj = vehicle_type()
#                 writer.writerow(line_obj)




# def pop_all(n):
#     pop_contract(n)
#     pop_customer(n)
#     pop_country(n)
#     pop_employee(n)
#     pop_vehicle(n)
#     pop_vehicle_type(n)


# if __name__ == '__main__':
#     pop_all(10)







    
        

