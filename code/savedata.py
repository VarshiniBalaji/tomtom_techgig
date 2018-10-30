import pandas as pd
import requests
import json
# import pandas as pd

def saveusrdata(val):
	data=pd.read_csv('db/data.csv')
	data_copy=data.copy()
	n=list(data.columns)
	print(n)
	print(val)
	a=[[],[],[],[],[],[],[]]
	for i in range(len(val)):
		a[i]=list(data_copy[n[i]])
		a[i].append(val[i])
# 		data_copy[n[i]]=a
		print(n[i],val[i])
	print({n[0]:a[0],n[1]:a[1],n[2]:a[2],n[3]:a[3],n[4]:a[4],n[5]:a[5],n[6]:a[6]})
	sub=pd.DataFrame({n[0]:a[0],n[1]:a[1],n[2]:a[2],n[3]:a[3],n[4]:a[4],n[5]:a[5],n[6]:a[6]})    
	sub.to_csv('db/data.csv',index=False)
	a=pd.read_csv('db/data.csv')
	print("aaaaaaaaaaaa",a)
	latlog(data=a)
	return "done"

def latlog(data):
	api_token = 'oyq2afLK8q9KJG8yDiojI3gldjCBkkN0'
	data['latitude']=0
	data['longitude']=0
	la=[]
	lo=[]
	for i,j,k in zip(data['address'],data['pincode'],data['city']):
		if(i!='1' and j!='1' and k!='1'):
			tomtomgeo = 'https://api.tomtom.com/search/2/geocode/{}.json?countrySet=IN&lat=20.5937&lon=78.9629&key={}'.format(str(i)+str(j)+str(k),api_token)
			req = requests.get(tomtomgeo)
			req.status_code
			a=req.json()
			lat=a['results'][1]['position']['lat']
			lon=a['results'][1]['position']['lon']
			la.append(lat)
			lo.append(lon)
		else:
			la.append('0')
			lo.append('0')
	data['latitude']=la
	data['longitude']=lo
	print("list",la,lo)
	data.to_csv('db/data.csv',index=False)