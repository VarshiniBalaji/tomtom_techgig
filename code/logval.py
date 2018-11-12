import pandas as pd

data=pd.read_csv('db/data.csv')
df=pd.DataFrame	()
def validate(name,contact):
	if(name != None and contact != None):
		print(type(contact),type(name))
		print(contact,name)
		df=data[data['contactno']==int(contact)]
		print(df)
		nm=str(df['name'].str)
		print(type(nm))
		print(nm,'==',name)
		return "True"
	
	