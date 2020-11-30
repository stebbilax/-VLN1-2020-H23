import os
from Data.csv_manager import csv_manager

class DataAPI:
    def __init__(self):
        self.data_dir = os.getcwd() + '\data/'
        self.contract_db = csv_manager(self.data_dir)


    def get_contract(self):
        return self.contract_db





