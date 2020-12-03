def test(logicAPI, ui):
    print(ui.get_user_form(
            ['SSID', 'Favorite Animal'],
            ['(\\d{6})-(\\d{4})', None],
            ['Please use a valid SSID format (6 letters - 4 letters)'])
    )

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
    ],[
        None,
        '(\d)',
        None,
        '([\w-\.]+@+[\w-]+\.+[\w]{2,4})',
        '([\d{1,9}]{4}-[\d{1,9}]{2}-[\d{1,9}]{2})',
        '([\d{1,9}]{4}-[\d{1,9}]{2}-[\d{1,9}]{2})',
        None,
        
    ],
    
    ))
2022-14-05