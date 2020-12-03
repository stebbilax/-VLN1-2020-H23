def test(logicAPI, ui):
    print(ui.get_user_form(['SSID', 'TYPE', 'COLOR']))

def display_all_employees(logicAPI, ui):
    for employee in logicAPI.employee.get_all_employees():
        print(employee)



def display_all_contracts(logicAPI, ui):
    for contract in logicAPI.contract.get_all_contracts():
        print(contract)

def get_contract(logicAPI, ui):
    # "Search by: name, phone, address, email, date_from, date_to, vehicle_id, country, vehicle_status, employee_id, loan_date, return_date, total, loan_status, id"
    print("\nSearch by: ")
    print("1. Name")
    print("2. Email")
    print("3. Vehicle ID")
    print("4. Vehicle Status")
    print("5. Loan Status")
    print("6. Contract ID")
    choice = input("Enter a choice: ")
    if choice == "1":
        print(logicAPI.contract.get_contract().by_name(input("Name: ")))
    elif choice == "2":
        print(logicAPI.contract.get_contract().by_email(input("Email: ")))
    elif choice == "3":
        print(logicAPI.contract.get_contract().by_vehicle_id(input("Vehicle ID: ")))
    elif choice == "4":
        print(logicAPI.contract.get_contract().by_vehicle_status(input("Vehicle Status: ")))
    elif choice == "5":
        print(logicAPI.contract.get_contract().by_id(input("Contract ID: ")))
