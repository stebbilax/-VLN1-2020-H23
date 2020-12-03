def test(logicAPI, ui):
    print(ui.get_user_form(['SSID', 'TYPE', 'COLOR']))

def display_all_employees(logicAPI, ui):
    for employee in logicAPI.employee.get_all_employees():
        print(employee)