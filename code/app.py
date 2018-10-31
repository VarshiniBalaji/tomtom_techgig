from flask import Flask, render_template, request
from savedata import saveusrdata
#from latnlog import latlog
import datetime
import pandas as pd
from optpath import path,start_point

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/user')
def user():
   return render_template('user.html')

@app.route('/admin')
def admin():
   return render_template('admin.html')


@app.route('/saveuserdetails',methods = ['POST', 'GET'])
def saveuserdetails():
   if request.method == 'POST':
      name = request.form["nm"]
      contact = request.form["con"]
      address = request.form["addr"]
      pin = request.form["pin"]
      state = request.form["stat"]
      city = request.form["cit"]
      date=datetime.datetime.now()
      a=[date,name,contact,address,city,pin,state]
      print(a)
      b=saveusrdata(val=a)
      if(b=="done"):
         return render_template('userdetails.html')
      else:
         print("error")

@app.route('/ll')
def ll():
   # latlog()
   df=pd.read_csv('db/data.csv')
   print(df)
   df[1:].to_html('templates/df.html')
   return render_template('table.html')

@app.route('/opt')
def opt():
   st_ll=start_point(data='perungudi garbage dump yard chennai,600096')
   p=path(st_ll=st_ll)
   print(p)
   return render_template('graph.html',p=p[0])

if __name__ == '__main__':
   app.run(debug = True)