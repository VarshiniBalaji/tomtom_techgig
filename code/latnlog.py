import requests
import json
import pandas as pd
# import datetime

api_token = 'oyq2afLK8q9KJG8yDiojI3gldjCBkkN0'
data=pd.read_csv('db/data.csv')
print("datttttttttt",data)
data['latitude']=0
data['longitude']=0
# def display():
# 	df=pd.read_csv('db/data.csv')
# 	return df


def latlog():
	la=[]
	lo=[]
	for i,j,k in zip(data['address'],data['pincode'],data['city']):
		if(i!='1' and j!='1' and k!='1'):
			tomtomgeo = 'https://api.tomtom.com/search/2/geocode/{}.json?countrySet=IN&lat=20.5937&lon=78.9629&key={}'.format(str(i)+str(j)+str(k),api_token)
			req = requests.get(tomtomgeo)
			req.status_code
			a=req.json()
			print(a)
			lat=a['results'][0]['position']['lat']
			lon=a['results'][0]['position']['lon']
			la.append(lat)
			lo.append(lon)
		else:
			la.append('0')
			lo.append('0')
	data['latitude']=la
	data['longitude']=lo
	print("list",la,lo)
	data.to_csv('db/data.csv',index=False)