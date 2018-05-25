from flask import Flask, session, escape, request, redirect, url_for
from os import urandom
import pymysql
import pymysql.cursors
from flask import render_template, json
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError
import MySQLdb
import werkzeug 


db = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'pranjal2000',
    db = 'SIGNUP'    
    )

app = Flask(__name__)

app.debug = True
app.secret_key = urandom(24)


@app.route('/', methods=['GET', 'POST'])
def index():
   

    if request.method == 'GET':
         return render_template("signup.html")	
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
        Username=request.form['username']
        phoneno=request.form['phoneno']
        emailid=request.form['email']
        gender=request.form['gender']
        password=request.form['password']
        
        cursor = db.cursor()
        cursor.execute("""
         INSERT INTO LOGIN(USERNAME,EMAIL,GENDER,PHONE_NO,PASSWORD) \
         VALUES (%s,%s,%s,%s,%s) """, (Username,emailid,gender,phoneno,password))
    
        db.commit()
        return render_template("home.html")
    if 'username' in session:
            return 'Hey, {}!'.format(escape(session['username']))
    return 'You are not signed in!'

        

  

#@app.route('/sign_in')
#def sign_in():
    


@app.route('/sign_out')
def sign_out():
    session.pop('username')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
