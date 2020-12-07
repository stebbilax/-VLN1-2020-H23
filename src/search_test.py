from Logic.Search_API import Search_API

SM = Search_API()

res = SM.search_vehicle().by_id('1')


print(res)

