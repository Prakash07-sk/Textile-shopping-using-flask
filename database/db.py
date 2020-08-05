from flask import Flask,render_template, redirect, url_for
from datetime import timedelta,datetime
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///textileshopping.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app) 

class User(db.Model):
	username=db.Column(db.String(100),primary_key=True)
	fname=db.Column(db.String(100))
	lname=db.Column(db.String(100))
	datetime=db.Column(db.DateTime,default=datetime.now)
	password=db.Column(db.String(100))

#product details
class Products(db.Model):
	product_id=db.Column(db.Integer,primary_key=True)
	product_name=db.Column(db.String(100))
	product_catagory=db.Column(db.String(100))#it is men,women,kids
	product_type=db.Column(db.String(100)) # it is shirts, pants that type
	product_price=db.Column(db.Integer)
	product_image=db.Column(db.String)



db.create_all()