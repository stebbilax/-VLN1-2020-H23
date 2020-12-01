import os
from Data.csv_manager import Csv_Manager

class DataAPI:
    def __init__(self):
        self.data_dir = os.getcwd() + '\data/'
        self.contract_db = Csv_Manager(self.data_dir)


    def get_contract(self):
        return self.contract_db





