import pandas as pd

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
	return "done"