import os
from Data.Contract_DB import Contract_DB

class DataAPI:
    def __init__(self):
        self.data_dir = os.getcwd() + '\data/'
        self.contract_db = Contract_DB(self.data_dir)


    def get_contract(self):
        return self.contract_db





