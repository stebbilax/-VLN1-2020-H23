class Invoice_Manager:
    def __init__(self, dapi, sapi):
        self.dapi = dapi
        self.sapi = sapi


    def generate_invoice(self, id):
        contract = self.sapi.search_contract().by_id(str(id))
        print(contract)