from Data.DataAPI import DataAPI as DB

# Example: Search_Manager.search('Oliver', 'name', 'employee')
class Search_Manager:
    def __init__(self):
        self.DB = DB()
        self.current_data = None
        self.search_string = None
        self.search_field = None
        self.result = []


    def search(self, search_string, search_field, search_catagory):
        self.search_field = search_field.lower()
        self.current_data = self.fetch(search_catagory)
        self.search_string = str(search_string.lower())
        self._search()

        results = self.result
        self.clear()

        return results


    def fetch(self, cat):
        if cat == 'contract': return self.DB.read_all_contracts()
        if cat == 'customer': return self.DB.read_all_customers()
        if cat == 'destination': return self.DB.read_all_destinations()
        if cat == 'employee': return self.DB.read_all_employees()
        if cat == 'vehicle': return self.DB.read_all_vehicles()
        if cat == 'vehicle_type': return self.DB.read_all_vehicle_types()


    def _search(self):
        for el in self.current_data:
            obj = el.__dict__()
            if obj[self.search_field].lower() == self.search_string:
                self.result.append(el)
            

    def clear(self):
        self.result = []






    