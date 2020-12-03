def test(logicAPI, ui):
    print(ui.get_user_form(['SSID', 'TYPE', 'COLOR']))

def display_all_employees(logicAPI, ui):
    for employee in logicAPI.employee.get_all_employees():
        print(employee)



def display_all_contracts(logicAPI, ui):
    for contract in logicAPI.contract.get_all_contracts():
        print(contract)


def register_new_contract(logicAPI, ui):
    print(ui.get_user_form([
        'NAME',
        'PHONE',
        'ADDRESS',
        'EMAIL',
        'DATE FROM',
        'DATE TOO',
        'VEHICLE ID',
        'COUNTRY',
        'VEHILE STATUS',
        'EMPLOYEE ID',
        'LOAN DATE',
        'RETURN DATE',
        'TOTAL',
        'LOAN STATUS',
    ]))