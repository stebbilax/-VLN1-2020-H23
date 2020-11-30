import csv
fieldnames = [
    'name', 
    'phone',
    'address', 
    'email', 
    'date_from', 
    'date_to', 
    'vehicle_id', 
    'location', 
    'vehicle_status', 
    'employee_id', 
    'loan_date', 
    'return_date', 
    'total', 
    'loan_status'
    ]

class Contract_DB:
    def __init__(self, dir):
        self.dir = dir


    def write_all(self, data):
        with open(f'{self.dir}/data/contracts.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for obj in data:
                line_obj = obj.__dict__()
                writer.writerow(line_obj)



    def read_all(self):
        print('read all')
