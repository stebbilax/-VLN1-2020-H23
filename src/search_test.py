from Logic.Search_API import Search_API

SM = Search_API()

a = SM.search_contract()

b = SM.search_customer()

c = SM.search_destination()

d = SM.search_employee()

e = SM.search_vehicle()

f = SM.search_vehicle_type()

print(e("red", "color", "vehicle"))

