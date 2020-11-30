import csv
from configparser import ConfigParser

file = 'Data/config.ini'
config = ConfigParser()
config.read(file)

contract_fields = config['fields']['contract_fields'].split(',')




class csv_manager:
    def __init__(self, dirr):
        self.dir = dirr


    # def write_all(self, data):
    #     with open(f'{self.dirr}/data/contracts.csv', 'w', newline='', encoding='utf-8') as f:
    #         writer = csv.DictWriter(f, fieldnames=fieldnames)
    #         writer.writeheader()
    #         for obj in data:
    #             line_obj = obj.__dict__()
    #             writer.writerow(line_obj)



    # def read_all(self):
    #     print('read all')

