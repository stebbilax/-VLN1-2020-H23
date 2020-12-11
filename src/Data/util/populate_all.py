import os
import sys
import csv
from random import randint
from configparser import ConfigParser


sys.path.append(os.getcwd())

from Data.DataAPI import DataAPI
from Models.Contract import Contract
from Models.Customer import Customer
from Models.Destination import Destination
from Models.Employee import Employee
from Models.Vehicle import Vehicle
from Models.Vehicle_Type import Vehicle_Type


"""
Populates database with dummy data.
Does not go through the logic api and is thus
missing some input validation.

Must be run from src folder
"""


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
    """Returns contract with random data in it from Dummy()"""
    return Contract(
        randint(1, 10),
        D.make_vehicle_state(),
        D.make_vehicle_status(),
        D.make_licence(),
        D.make_type(),
        D.make_country(),

        '1',
        D.make_name(),
        D.make_phone(),
        D.make_email(),
        D.make_address(),
        D.make_licence(),
        
        '1',
        D.make_airport(),
        D.make_airport(),
        'N/A',
        'N/A',
        'N/A',
        'N/A',
        D.make_early_date(),
        D.make_later_date(),
        D.make_contract_state(),
        randint(100, 1000),
        randint(0, 300),
        0,
        
        

    )
def customer():
    """Returns customer with random data in it from Dummy()"""
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
    """Returns destination with random data in it from Dummy()"""
    return Destination(
        D.make_country(),
        D.make_airport_after_country(),
        D.make_phone(),
        D.make_opening_hours(),
    )

def employee():
    """Returns employee with random data in it from Dummy()"""
    return Employee(
        D.make_name(),
        D.make_address(),
        D.make_postal_code(),
        D.make_ssn(),
        D.make_phone(),
        D.make_phone(),
        D.make_email(),
        D.make_title(),
        D.make_airport_after_title(),
        D.make_country_after_airport(),


    )
def vehicle():
    """Returns vehicle with random data in it from Dummy()"""
    return Vehicle(
        D.make_type(),
        D.make_manufacturer(),
        D.make_yom(),
        D.make_color(),
        D.make_licence(),
        D.make_airport(),
        D.make_vehicle_state(),
        D.make_vehicle_status(),
        randint(100,300),
        D.make_model(),
        D.make_vehicle_id(),
    )
def vehicle_type():
    """Returns vehicle type with random data in it from Dummy()"""
    return Vehicle_Type(
        D.make_type(),
        D.make_airport(),
        randint(100, 1000),

    )



def pop_contract(num_of_lines):
    '''Writes to db'''
    arr = []
    for _ in range(num_of_lines):
        arr.append(contract())

    DB.write_all_contracts(arr)


def pop_customer(num_of_lines):
    '''Writes to db'''
    arr = []
    for _ in range(num_of_lines):
        arr.append(customer())

    DB.write_all_customers(arr)


def pop_destination(num_of_lines):
    '''Writes to db'''
    arr = []
    for _ in range(num_of_lines):
        arr.append(destination())

    DB.write_all_destinations(arr)
    

def pop_employee(num_of_lines):
    '''Writes to db'''
    arr = []
    for _ in range(num_of_lines):
        arr.append(employee())

    DB.write_all_employees(arr)

    
def pop_vehicle(num_of_lines):
    '''Writes to db'''
    arr = []
    for _ in range(num_of_lines):
        arr.append(vehicle())

    DB.write_all_vehicles(arr)
    

def pop_vehicle_type(num_of_lines):
    '''Writes to db'''
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






    
        

