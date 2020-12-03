def test(api):
    print("123")

def display_all_employees(api):
    for employee in api.employee.get_all_employees():
        print(employee)