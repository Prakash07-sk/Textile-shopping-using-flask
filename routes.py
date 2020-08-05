from flask import Blueprint, render_template,  redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from database.db import Products,db,User

routes=Blueprint("routes", __name__, static_folder="static", template_folder="templates")

@routes.route("/")
def index():
	
	found_mens=Products.query.filter_by(product_catagory="mens")
	found_womens=Products.query.filter_by(product_catagory="womens")
	found_kids=Products.query.filter_by(product_catagory="kids/children")
	todaysdeal=Products.query.all()
	uname=""
	if 'username' in session:
		uname=session['username']
		found_fname=User.query.filter_by(username=uname).first()
		if found_fname:
			uname=found_fname.fname
			session['fname']=uname
	return render_template("index.html",
							kids=found_kids,
							womens=found_womens,
							mens=found_mens,
							todays=todaysdeal,uname=uname)


@routes.route("/<name>")
def illigalentry(name):
	return render_template("404error.html")


@routes.route('/login',methods=['GET', 'POST'])
def login():
	session.clear()
	if request.method== 'POST':
		username=str(request.form['username']).lower()
		password=request.form['password']
		found_user = User.query.filter_by(username=username).first()
		if found_user:
			if found_user.password==password:
				session['username']=username
				return redirect(url_for('routes.index'))
			else:
				return render_template("login.html",message="password doesn't match")

		else:
			return render_template("login.html",message="No Emailid found")

	return render_template("login.html")

@routes.route('/registration',methods=['GET', 'POST'])
def registration():
	if request.method== 'POST':
		username=str(request.form['username']).lower()
		fname=str(request.form['fname']).lower()
		lname=str(request.form['lname']).lower()
		password=request.form['password']
		found_user=User.query.filter_by(username=username).first()
		if found_user:
			return render_template("registration.html",message="Email id already exits",
									uname=username)
		else:
			connect=User(username=username,fname=fname,lname=lname,password=password)
			db.session.add(connect)
			db.session.commit()
			return render_template("registration.html",message="Registration success")

	return render_template("registration.html")

@routes.route("/userlogout")
def userlogout():
	session.clear()
	return redirect(url_for("routes.index"))


@routes.route("/kids")
def kids():
	if 'fname' in session and 'username' in session:
		found_kids=Products.query.filter_by(product_catagory="kids/children")
		catagory=[]
		for i in found_kids:
			catagory.append(i.product_type)
		catagory=set(catagory)
		return render_template("kids.html",uname=session['fname'],
								kids=found_kids,catagory=catagory)
	else:
		return redirect(url_for("routes.login"))

@routes.route("/todaysdeal")
def todaysdeal():
	if 'fname' in session and 'username' in session:
		return render_template("todaysdeal.html",uname=session['fname'],
								todaysdeal=Products.query.all())
	else:
		return redirect(url_for("routes.login"))

@routes.route("/mens")
def mens():
	if 'fname' in session and 'username' in session:
		found_mens=Products.query.filter_by(product_catagory="mens")
		catagory=[]
		for i in found_mens:
			catagory.append(i.product_type)
		catagory=set(catagory)
		return render_template("mens.html",uname=session['fname'],
								mens=found_mens,catagory=catagory)
	else:
		return redirect(url_for("routes.login"))


@routes.route("/womens")
def womens():
	if 'fname' in session and 'username' in session:
		found_womens=Products.query.filter_by(product_catagory="womens")
		catagory=[]
		for i in found_womens:
			catagory.append(i.product_type)
		catagory=set(catagory)
		return render_template("womens.html",uname=session['fname'],
								womens=found_womens,catagory=catagory)
	else:
		return redirect(url_for("routes.login"))


