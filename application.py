import datetime
from os import link
import re
from flask import Flask, flash, redirect, render_template, request, session
from types import MethodType
from flask.helpers import url_for
from flask_session import Session
from tempfile import mkdtemp
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer ,SignatureExpired
import secrets
import math  
import random
# from flask_assets import Bundle , Enviornment, assets
from werkzeug import datastructures


# from requests.sessions import _Data
# import helpers
from helpers import apology, datad_collector, login_required, test 
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from search_engine import main_work
app = Flask(__name__)
# app.config.from_pyfile('config.cfg')
# js = Bundle('vendor.js' , output='gen/main.js')
# Assets = Enviornment(app)
# Assets.register()
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ma-nazari83@hotmail.com'
app.config['MAIL_PASSWORD'] = 'm.salah11'
secret_key = secrets.token_urlsafe(16)
app.config["SECRET_KEY"] = secret_key
s = URLSafeTimedSerializer(secret_key)
app.config["TEMPLATES_AUTO_RELOAD"] = True
mail = Mail(app)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# const = random_str
db = SQL("sqlite:///info.db")
# def
@app.route("/")
@login_required
def main():
    if request.method =="GET":
        # data = test("headphone")
        data = main_work("headphone" , 4)
        # print(data)
        # print(data)
        return render_template("index.html" ,  API_INFOS = data)






@app.route("/register" , methods=["GET" , "POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        email = request.form.get("email")
        if db.execute("SELECT * FROM users WHERE username=?" , email)!=[]:
            return render_template("custom.html" , message = "Your username has already been used" , code = 404)
        # print(db.execute("SELECT * FROM users WHERE username=?" , "email"))
        # print(email)
        if not email:
            return apology("Please Enter a Valid Email" , 403)
        password = request.form.get("password")
        # print(password)
        if not password:
            return apology("Please Enter a Valid Email" , 403)
        confirm = request.form.get("confirm")
        # print(confirm)
        if not confirm:
            return apology("Please Enter a Valid Email" , 403)
        if confirm!= password:
            return apology("Please confirm Your password" , 403)
        db.execute("INSERT INTO users(username , hash) VALUES(?  ,? )" ,email , generate_password_hash(password))
        
        
## storing strings in a list
        

## displaying the random string
        # print(random_str)
        
        token = s.dumps(email , salt="email-confirm")
        msg = Message("Confirm email" , sender="ma-nazari83@hotmail.com" , recipients=[email])
        # print(msg)
        link = url_for('confirm_email' , token = token , _external = True)
        # print(link)
        msg.body ="Your mail was used to sign in into this website your link = {}  ".format(link)
        # print(msg.body)
        mail.send(msg)
        # return redirect("/confirm")
        flash("successfully signed in")
        # return redirect("login.html")
    # TODO
        return redirect("/confirm")
@app.route('/confirm_email/<token>')  
def confirm_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
    except SignatureExpired:
        db.execute("DELETE * FROM Table ORDER BY ID DESC LIMIT 1")
        return '<h1>The token is expired!</h1>'
    return redirect("/")
@app.route("/confirm" , methods=["GET" , "POST"] )
def confirm():
    if request.method=="GET":
        return redirect("/login")
    else:
        
        confirm_code = request.form.get("confirm")
        
        print(confirm_code)
        if confirm_code!= "random_str":
            db.execute("DELETE * FROM Table ORDER BY ID DESC LIMIT 1")
            return apology("The code You enterd is wrong" ,403)
        else:
            flash("successfully signed in ")
            return redirect("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("email"):
            return render_template("custom.html",message = "must provide username" ,code =  403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        # print( request.form.get("email"))
        # Query database for username
        # request.form.get("email")
        rows = db.execute("SELECT * FROM users WHERE username = ?" , str(request.form.get("email")))
        # print(rows)
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("custom.html",message="invalid username and/or password", code =  403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

# def index():
#     if request.method =="GET":
#         return render_template("index.html")
#     # TODO
#     pass
@app.route("/test" , methods=["GET", "POST"])
@login_required
def testing():
    if request.method=="GET":
        return render_template("test.html")
    else:
        data =request.form.get("data")
        if data=='':
            return render_template("custom.html" , message = 'Please enter a valid product name' , code = 400)
        api_data = main_work(data , 7)
        if api_data==None:
            return render_template("custom.html" , message='The product You enterd was not available' , code = 405)
        print(api_data)
        # print(api_data)
        
        return render_template("tested.html" , API_INFOS=api_data)
@app.route("/settings" , methods=["GET", "POST"])
@login_required
def settings():
    if request.method=="GET":
        return render_template("settings.html")
@app.route("/cart" , methods=["GET", "POST"])
@login_required
def cart():
    if request.method=="GET":
        username = db.execute("SELECT username FROM users WHERE id = ?" , session["user_id"])[0]['username']
        buys = db.execute("SELECT * FROM BUYS WHERE username =?" , username)
        return render_template("cart.html" , BUYS = buys)
    else:
        return render_template("successfull.html")
@app.route("/settings/change-password" , methods=["GET", "POST"])
def change_password():
    if request.method=="GET":
        return render_template("change-password.html")
    else:
        old_password = request.form.get("old-password")
        new_password = request.form.get("new-password")
        confirm = request.form.get("confirm")
        # print(new_password)
        # print(confirm)
        print(session["user_id"])
        # print(generate_password_hash(old_password))
        if old_password=='' or new_password=='' or confirm=='':
            return render_template("custom.html" , message="please fill the form completely" , code=404)

        # print(db.execute("SELECT * FROM users WHERE hash=?" ,generate_password_hash(new_password)))
        if db.execute("SELECT * FROM users WHERE hash=?" ,generate_password_hash(old_password))==None:
            return render_template("custom.html" , message="Your password dosent exist")
        elif new_password!=confirm:
            return render_template("custom.html" , message="Please confirm your new password correctly")
        elif db.execute("SELECT * FROM users WHERE hash=?" , generate_password_hash(new_password))!=[]:
        
            return render_template("custom.html" , message="The password which ypu enterd already exists!")
        
        else :
            sql = "UPDATE users SET hash=%s WHERE id= %s"
            db.execute(sql ,generate_password_hash(new_password), session["user_id"])
            return redirect("/")
@app.route("/test/buy"  , methods = ["POST"])
def Buy():
    
    if request.method=="POST":
        product = request.values.get('title')
        print(product)
        return redirect("/cart")
# @app.route("/test/Buy" , methods=[ "POST"])
# def Buy():
#     # if request.method=="GET":
#     #     return redirect("/cart")
#     # else:






@app.route('/settings/forgot_password' , methods = ["GET" , "POST"])
def forgot_password() :
    if request.method=="GET":
        return render_template("forgot_password.html")
    else:
        email = request.form.get("email")
        print(email)
        if db.execute("SELECT * FROM users WHERE username==?" , email)==[] :
            return render_template("custom.html" , message = "Your username is invalid" , code = 404)
        password = "new_pass1234"
        msg = Message("Confirm email" , sender="ma-nazari83@hotmail.com" , recipients=[email])
        msg.body ="Use this password to login then change it asap! = {}  ".format(password)
        db.execute("UPDATE users SET hash = ? WHERE username=?" , generate_password_hash(password) , email)
        mail.send(msg)
        return redirect("/login")











@app.route('/test/ajax', methods = ['POST'])
def ajax_request():
    if request.method == 'POST':
        username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]['username']
        json_data = request.json
        a = json_data
        print( username)
        # print(a['price'] )

        # print( a['title'] )
        db.execute("INSERT INTO BUYS(username , price , product  ) VALUES(? , ? ,?)" ,username , a["price"][6:] , a['title'])
        # a2 = a['link'];
        # a1 = a['user_id'];
        # start = '<a href="../">'
        # end = '<br> LINK.COM</a>'
        # a3 = a1[a1.find(start)+len(start):a1.rfind(end)]
        # connection = sqlite3.connect("db.db")
        # cursor = connection.cursor()
        # link_id = a2
        # user_id = a3
        # params = deleted(id=None, user_id=user_id, link_id=link_id)
        # db.session.add(params)
        # db.session.commit()
        return redirect("/cart", code=302)
@app.route("/cart/remove" , methods = ['POST'])
def Remove_product():
    if  request.method=="POST":
        json_data = request.json
        a = json_data
        # print(a)
        db.execute("DELETE FROM BUYS WHERE product=? " , a)
        return render_template("cart.html")
@app.route("/success_buy" , methods = ["GET"])
def success_buy():
    if request.method=="GET" :
        return render_template("successfull.html")   





