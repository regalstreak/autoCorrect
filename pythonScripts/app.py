import sqlite3
from datetime import datetime, date
from functools import wraps
from flask import Flask,render_template,redirect, url_for,request,session,flash
import os
import random
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy 
import json
from flask_oauth import OAuth
from flask import make_response, jsonify

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///autocorrect.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


@app.route('/')
def index():
	result = {'hello': 'world'}
	return make_response(jsonify(result), 201)


if __name__ == '__main__':
	app.debug = True
	app.secret_key = os.urandom(12)
	db.create_all()

app.run(debug = True,threaded=True, host="0.0.0.0",port=5000)