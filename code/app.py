from flask import Flask, render_template, request
from savedata import saveusrdata
#from latnlog import latlog
import datetime
import pandas as pd
from optpath import path,start_point
from logval import validate
from chat import talk


app = Flask(__name__,template_folder='templates')	
i=0
v=''
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/user')
def user():
   return render_template('user.html')

@app.route('/admin')
def admin():
   return render_template('admin.html')
   
@app.route('/user_reg')
def user_reg():
   return render_template('reg.html')
   
@app.route('/user_login')
def user_login():
   return render_template('login.html')
   
@app.route('/login_val',methods = ['POST', 'GET'])
def login_val():
   if(request.args.get("tt")):
      text=request.args.get("tt")
      print(text)
      global i
      i=i+1
      txt=talk(i,n=None)
      print(txt)
      return txt                
   if request.method == 'POST':
      name = request.form["nm"]
      contact = request.form["con"]
      global v
      v=validate(name,contact)
      #if(request.args.get("tt")):
      #   text=request.args.get("tt")
      #   print(text)
      txt=talk(i,n=name)
      print(txt)
      if(v=="True"):
        return render_template("chatbot.html",t=txt)
		 
@app.route('/test',methods = ['POST', 'GET'])
def test():
   text=request.args.get("tt")
   print(text)
   global i
   i=i+1
   txt=talk(i,n=None)
   print(txt)
   return render_template("chatbot.html",t1=txt)

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
   df=pd.read_csv('db/datall.csv')
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