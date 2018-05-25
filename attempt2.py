from flask import Flask, session, escape, request, redirect, url_for
import pymysql
import pymysql.cursors
from flask import render_template, json,flash
from flask import Flask, request, jsonify
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError
import MySQLdb
import werkzeug 
from os import urandom

db = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'pranjal2000',
    db = 'SIGNUP'    
    )

app= Flask(__name__)


@app.route('/',methods=['GET','POST'])
def get_data(): 
 if request.method == 'GET':
    return render_template("signup.html")
 if request.method=='POST':
    username=request.form['username']
    phoneno=request.form['phoneno']
    emailid=request.form['email']
    gender=request.form['gender']
    password=request.form['password']

    cursor = db.cursor()
    cursor.execute("""
    INSERT INTO LOGIN(USERNAME,EMAIL,GENDER,PHONE_NO,PASSWORD) \
    VALUES (%s,%s,%s,%s,%s) """, (username,emailid,gender,phoneno,password))
    db.commit()
    session[ussername]
    return redirect(url_for('home'))
    return render_template('home.html',username=username)

 flash(error)

 return render_template('/')

@app.route("/login", methods=['GET','POST'])
def Authenticate():
    if request.method == 'GET':
    	return render_template("login.html")
    if request.method=='POST':
	    username = request.form['username']
	    password = request.form['password']
	    print "  > username :", username
	    print "  > password :", password
	    cursor = db.cursor()
	    error = None
	    cursor.execute("SELECT * from LOGIN where USERNAME='" + username + "' and PASSWORD='" + password + "'")
	    data = cursor.fetchone()
	    if data is None:
	     error = 'Incorrect username.'
            #elif not check_password_hash(data['password'], password):
            #	error = 'Incorrect password.'
            if error is None:
		    session.clear()
		    session['username'] = data['username']
		    secret_key = 'develop'	
		    return redirect(url_for('home'))
                    
            flash(error)

    return render_template('login.html')

'''@app.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()'''

@app.route("/home",methods=['GET','POST'])
def home():
    if request.method == 'GET':
    	return render_template("home.html")
    if request.method=='GET':
	    username = request.form['username']
    if request.method == 'POST':
            return render_template('home.html', username = uesrname)



if __name__=='__main__':
	app.run(debug=True, port= 8002)
	app.secret_key = 'develop'
	app.config['SESSION_TYPE'] = 'filesystem'



