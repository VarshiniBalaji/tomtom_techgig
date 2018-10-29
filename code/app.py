from flask import Flask, render_template, request
from savedata import saveusrdata
import datetime

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/user')
def user():
   return render_template('user.html')

@app.route('/admin')
def admin():
   return 'admin'

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

if __name__ == '__main__':
   app.run(debug = True)