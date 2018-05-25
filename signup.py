"""from PIL import Image
import urllib2 as urllib
from traceback import print_exc
import io
import os
import sys"""
import pymysql
import pymysql.cursors
from flask import render_template, json
from flask import Flask, request, jsonify
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
app= Flask(__name__)

@app.route('/',methods=['GET','POST'])
def get_data(): 
 if request.method == 'GET':
    return render_template("signup.html")
 if request.method=='POST':
    Username=request.form['username']
    phoneno=request.form['phoneno']
    emailid=request.form['email']
    gender=request.form['gender']
    password=request.form['password']

    cursor = db.cursor()
    cursor.execute("""
    INSERT INTO LOGIN(USERNAME,EMAIL,GENDER,PHONE_NO,PASSWORD) \
    VALUES (%s,%s,%s,%s,%s) """, (Username,emailid,gender,phoneno,password))
    #cursor.execute(sql)
#    results = cursor.fetchall()
#    print "columns :", 
 #   for col_name in cursor.description:
#	print col_name[0],
#	print
 #   for row in results:
#	print row
    db.commit()
    return '''

<html lang="en">
<head>
<title>HOME PAGE </title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
    box-sizing: border-box;
}

body {
  margin: 0;
}

/* Style the header */
.header {
    background-color: #f1f1f1;
    padding: 20px;
    text-align: center;
}

/* Style the top navigation bar */
.topnav {
    overflow: hidden;
    background-color: #333;
}

/* Style the topnav links */
.topnav a {
    float: right;
    display: block;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

/* Change color on hover */
.topnav a:hover {
    background-color: #ddd;
    color: black;
}

/* Create three equal columns that floats next to each other */
.column { 
	background: grey;
    float: left;
    width: 100%;
    padding: 15px;
    text-align: center;
}

/* Clear floats after the columns */


/* Responsive layout - makes the three columns stack on top of each other instead of next to each other */
@media screen and (max-width:600px) {
    .column {
        width: 100%;
    }
}
</style>
</head>
<body>

<div class="header">
  <h1>WELCOME!!    ''' + Username +'''</h1>

  
</div>

<div class="topnav">
  <a href="/">LOGOUT</a>
  
</div>


  <div class="column">
    <h2>Column</h2>
    <p>
    <img src="https://index.tnwcdn.com/images/c6c66fb234fc7cf614d146ca9c277d079bce8e48.jpg" alt="Image result for stashfin.jpeg" onload="typeof google==='object'&amp;&amp;google.aft&amp;&amp;google.aft(this)" width="229" height="229" style="margin-top: 185px;">
    </p>
    <p>
    This is the test home page for stashfin 
    Lets see how it goes from here </p>
	<p> upload a photo </p>
   <form action = "http://localhost:5000/uploader" method = "POST" 
         enctype = "multipart/form-data">
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>
  </div>

 
  


</body>
</html>'''
 
 #   cursor.close()
  
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
            elif not check_password_hash(user['password'], password):
            	error = 'Incorrect password.'
            if error is None:
		    session.clear()
		    session['user_id'] = user['id']
		    return redirect(url_for('home'))

           flash(error)

   return render_template('login.html')

<html lang="en">
<head>
<title>HOME PAGE </title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
    box-sizing: border-box;
}

body {
  margin: 0;
}

/* Style the header */
.header {
    background-color: #f1f1f1;
    padding: 20px;
    text-align: center;
}

/* Style the top navigation bar */
.topnav {
    overflow: hidden;
    background-color: #333;
}

/* Style the topnav links */
.topnav a {
    float: right;
    display: block;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

/* Change color on hover */
.topnav a:hover {
    background-color: #ddd;
    color: black;
}

/* Create three equal columns that floats next to each other */
.column { 
	background: grey;
    float: left;
    width: 100%;
    padding: 15px;
    text-align: center;
}

/* Clear floats after the columns */


/* Responsive layout - makes the three columns stack on top of each other instead of next to each other */
@media screen and (max-width:600px) {
    .column {
        width: 100%;
    }
}
</style>
</head>
<body>

<div class="header">
  <h1>WELCOME!!    ''' + username+'''</h1>

  
</div>

<div class="topnav">
  <a href="/">LOGOUT</a>
  
</div>


  <div class="column">
    <h2>Column</h2>
    <p>
    <img src="https://index.tnwcdn.com/images/c6c66fb234fc7cf614d146ca9c277d079bce8e48.jpg" alt="Image result for stashfin.jpeg" onload="typeof google==='object'&amp;&amp;google.aft&amp;&amp;google.aft(this)" width="229" height="229" style="margin-top: 185px;">
    </p>
    <p>
    This is the test home page for stashfin 
    Lets see how it goes from here </p>
	
  </div>

 
  


</body>
</html>


if __name__=='__main__':
	app.run(debug=True)
