from Logic.Search_API import Search_API

SM = Search_API()

res = SM.search_vehicle().by_id('1')


print(res)

'''
99,OK,Available,None,Light off-road,Shetland,1,Ava,887-8966,Benjamin@nan.is,IsabellaStreet 30,Drivers licence,1,reykjavik,kulusuk,N/A,N/A,N/A,N/A,2020-02-03,2020-02-08,Valid,305,42,0,1
Light water,Cani-Fit,1994,green,Drivers licence,tingwall,OK,Available,169,Free Fly II,NZ450,99




'''