from Logic.Search_Manager import Search_Manager

class Search_API:
    """
    Use by calling Search API, followed by data file to search, followed by catagory

    Example: Search_API().search_vehicle().by_id('1')
    """

    def __init__(self):
        self.Search_Contract = Search_Contract()
        self.Search_Customer = Search_Customer()
        self.Search_Destination = Search_Destination()
        self.Search_Employee = Search_Employee()
        self.Search_Vehicle_Type = Search_Vehicle_Type()
        self.Search_Vehicle = Search_Vehicle()
        
    def search_contract(self):
        return self.Search_Contract

    def search_customer(self):
        return self.Search_Customer

    def search_destination(self):
        return self.Search_Destination

    def search_employee(self):
        return self.Search_Employee

    def search_vehicle_type(self):
        return self.Search_Vehicle_Type

    def search_vehicle(self):
        return self.Search_Vehicle



class Search_Contract:
    def __init__(self):
        self.Search_Manager = Search_Manager()

    def by_vehicle_id(self, string):
        return self.Search_Manager.search(string, 'vehicle_id', 'contract')

    def by_vehicle_state(self, string):
        return self.Search_Manager.search(string, 'vehicle_state', 'contract')

    def by_vehicle_status(self, string):
        return self.Search_Manager.search(string, 'vehicle_status', 'contract')

    def by_vehicle_licence(self, string):
        return self.Search_Manager.search(string, 'vehicle_licence', 'contract')

    def by_country(self, string):
        return self.Search_Manager.search(string, 'country', 'contract')
    
    def by_customer_id(self, string):
        return self.Search_Manager.search(string, 'customer_id', 'contract')

    def by_customer_name(self, string):
        return self.Search_Manager.search(string, 'customer_name', 'contract')

    def by_phone(self, string):
        return self.Search_Manager.search(string, 'phone', 'contract')

    def by_email(self, string):
        return self.Search_Manager.search(string, 'email', 'contract')

    def by_address(self, string):
        return self.Search_Manager.search(string, 'address', 'contract')

    def by_customer_licence(self, string):
        return self.Search_Manager.search(string, 'customer_licence', 'contract')

    def by_employee_id(self, string):
        return self.Search_Manager.search(string, 'employee_id', 'contract')

    def by_date_of_handover(self, string):
        return self.Search_Manager.search(string, 'date_of_handover', 'contract')

    def by_date_of_return(self, string):
        return self.Search_Manager.search(string, 'date_of_return', 'contract')

    def by_contract_start(self, string):
        return self.Search_Manager.search(string, 'contract_start', 'contract')

    def by_contract_end(self, string):
        return self.Search_Manager.search(string, 'contract_end', 'contract')

    def by_state(self, string):
        return self.Search_Manager.search(string, 'state', 'contract')

    def by_rate(self, string):
        return self.Search_Manager.search(string, 'rate', 'contract')

    def by_late_fee(self, string):
        return self.Search_Manager.search(string, 'late_fee', 'contract')

    def by_total_price(self, string):
        return self.Search_Manager.search(string, 'total_price', 'contract')

    def by_id(self, string):
        return self.Search_Manager.search(string, 'id', 'contract')


class Search_Customer:
    def __init__(self):
        self.Search_Manager = Search_Manager()

    def by_name(self, string):
        return self.Search_Manager.search(string, 'name', 'customer')

    def by_ssn(self, string):
        return self.Search_Manager.search(string, 'ssn', 'customer')

    def by_address(self, string):
        return self.Search_Manager.search(string, 'address', 'customer')

    def by_postal_code(self, string):
        return self.Search_Manager.search(string, 'postal_code', 'customer')

    def by_phone(self, string):
        return self.Search_Manager.search(string, 'phone', 'customer')

    def by_email(self, string):
        return self.Search_Manager.search(string, 'email', 'customer')

    def by_country(self, string):
        return self.Search_Manager.search(string, 'country', 'customer')

    def by_licence(self, string):
        return self.Search_Manager.search(string, 'licence', 'customer')

    def by_id(self, string):
        return self.Search_Manager.search(string, 'id', 'customer')


class Search_Destination:
    def __init__(self):
        self.Search_Manager = Search_Manager()

    def by_country(self, string):
        return self.Search_Manager.search(string, 'country', 'destination')

    def by_airport(self, string):
        return self.Search_Manager.search(string, 'airport', 'destination')

    def by_phone(self, string):
        return self.Search_Manager.search(string, 'phone', 'destination')

    def by_opening_hours(self, string):
        return self.Search_Manager.search(string, 'opening_hours', 'destination')

    def by_id(self, string):
        return self.Search_Manager.search(string, 'id', 'destination')


class Search_Employee:
    def __init__(self):
        self.Search_Manager = Search_Manager()

    def by_name(self, string):
        return self.Search_Manager.search(string, 'name', 'employee')

    def by_address(self, string):
        return self.Search_Manager.search(string, 'address', 'employee')

    def by_postal_code(self, string):
        return self.Search_Manager.search(string, 'postal_code', 'employee')

    def by_ssn(self, string):
        return self.Search_Manager.search(string, 'ssn', 'employee')

    def by_phone(self, string):
        return self.Search_Manager.search(string, 'phone', 'employee')

    def by_mobile_phone(self, string):
        return self.Search_Manager.search(string, 'mobile_phone', 'employee')

    def by_email(self, string):
        return self.Search_Manager.search(string, 'email', 'employee')

    def by_title(self, string):
        return self.Search_Manager.search(string, 'title', 'employee')

    def by_airport(self, string):
        return self.Search_Manager.search(string, 'airport', 'employee')

    def by_country(self, string):
        return self.Search_Manager.search(string, 'country', 'employee')

    def by_id(self, string):
        return self.Search_Manager.search(string, 'id', 'employee')


class Search_Vehicle_Type:
    def __init__(self):
        self.Search_Manager = Search_Manager()

    def by_name(self, string):
        return self.Search_Manager.search(string, 'name', 'vehicle_type')

    def by_airport(self, string):
        return self.Search_Manager.search(string, 'airport', 'vehicle_type')

    def by_rate(self, string):
        return self.Search_Manager.search(string, 'rate', 'vehicle_type')

    def by_id(self, string):
        return self.Search_Manager.search(string, 'id', 'vehicle_type')


class Search_Vehicle:
    def __init__(self):
        self.Search_Manager = Search_Manager()

    def by_type(self, string):
        return self.Search_Manager.search(string, 'type', 'vehicle')

    def by_manufacturer(self, string):
        return self.Search_Manager.search(string, 'manufacturer', 'vehicle')

    def by_yom(self, string):
        return self.Search_Manager.search(string, 'yom', 'vehicle')

    def by_color(self, string):
        return self.Search_Manager.search(string, 'color', 'vehicle')

    def by_licence(self, string):
        return self.Search_Manager.search(string, 'licence', 'vehicle')

    def by_airport(self, string):
        return self.Search_Manager.search(string, 'airport', 'vehicle')

    def by_condition(self, string):
        return self.Search_Manager.search(string, 'condition', 'vehicle')

    def by_model(self, string):
        return self.Search_Manager.search(string, 'model', 'vehicle')

    def by_vehicle_id(self, string):
        return self.Search_Manager.search(string, 'vehicle_id', 'vehicle')

    def by_id(self, string):
        return self.Search_Manager.search(string, 'id', 'vehicle')