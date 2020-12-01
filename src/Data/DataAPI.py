import os
from Data.csv_manager import Csv_Manager

class DataAPI:
    def __init__(self):
        self.data_dir = os.getcwd() + '\data/'
        self.manager = Csv_Manager(self.data_dir)


    def get_writer(self):
        return self.manager.write_all

    def get_reader(self):
        return self.manager.read_all






