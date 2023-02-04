import pymongo
from flask import Flask, render_template, request

conn=pymongo.MongoClient()
db=conn['Mywebsite']
col=db['Userinfo']
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=='POST':

      return render_template("signup.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
     return render_template("login.html")
@app.route('/registered',methods=['POST','GET'])
def registered():
    if request.method =='POST':
            n=request.form.get('Name')
            y=request.form.get('Age')
            e=request.form.get('email')
            a=request.form.get('pw')
            a1=request.form.get('pw1')
            check = col.find_one({'EMAIL':n})
            print(f"{check}")

            if check == None:
               if a == a1:
                data ={
                  'NAME' : n,
                  'AGE': y,
                  'EMAIL' : e,
                  'PASSWORD' : a
                }
                col.insert_one(data)
                return render_template("confirm.html",name=n,age=a)


               else:
                return render_template("return.html")
            else:
             return render_template("exist.html")



app.run()