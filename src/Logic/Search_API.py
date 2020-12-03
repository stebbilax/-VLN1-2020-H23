from Logic.Search_Manager import Search_Manager


class Search_API:
    def __init__(self):
        self.Search_Manager = Search_Manager()

    def search_contract(self,search_string = "895-2459", search_field = "phone", search_catagory = "contract"):
        return self.Search_Manager.search

    def search_customer(self,search_string = "121073-1785", search_field = "ssn", search_catagory = "customer"):
        return self.Search_Manager.search

    def search_destination(self,search_string = "Svalbard", search_field = "country", search_catagory = "destination"):
        return self.Search_Manager.search

    def search_employee(self,search_string = "Oliver", search_field = "name", search_catagory = "employee"):
        return self.Search_Manager.search
    
    def search_vehicle(self,search_string = "10", search_field = "id", search_catagory = "vehicle"):
        return self.Search_Manager.search

    def search_vehicle_type(self,search_string = "Light water", search_field = "name", search_catagory = "vehicle_type"):
        return self.Search_Manager.search
        
