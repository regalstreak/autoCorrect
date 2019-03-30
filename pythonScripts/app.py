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


class test(db.Model):
	__tablename__ = 'test'
	column_display_pk = True
	testid = db.Column(db.Integer, primary_key=True)
	testname = db.Column(db.String(40))
	organized_by = db.Column(db.String(40))
	testdate = db.Column(db.DateTime)
	venue = db.Column(db.String(40))

class MyTestView(ModelView):
	column_display_pk = True
	can_create = True
	column_list = ('testid','testname','organized_by','testdate','venue')
	form_columns = ['testid','testname','organized_by','testdate','venue']
	column_filters = ['testid','testname','organized_by','testdate','venue']

class question(db.Model):
	__tablename__ = 'question'
	column_display_pk = True
	questionid = db.Column(db.Integer, primary_key=True)
	testid = db.Column(db.Integer)
	questionSt = db.Column(db.String(100))
	marks = db.Column(db.Integer)
	answerVec = db.Column(db.String(500))
	numOfParts = db.Column(db.Integer)

class MyQuestionView(ModelView):
	column_display_pk = True
	can_create = True
	column_list = ('questionid','testid','questionSt','marks','answerVec','numOfParts')
	form_columns = ['questionid','testid','questionSt','marks','answerVec','numOfParts']
	column_filters = ['questionid','testid','questionSt','marks','answerVec','numOfParts']


class answer(db.Model):
	__tablename__ = 'answer'
	column_display_pk = True
	answerid = db.Column(db.Integer, primary_key=True)
	testid = db.Column(db.Integer)
	questionid = db.Column(db.Integer)
	marks = db.Column(db.Integer)
	url = db.Column(db.String(100))

class MyAnswerView(ModelView):
	column_display_pk = True
	can_create = True
	column_list = ('answerid','testid','questionid','marks','url')
	form_columns = ['answerid','testid','questionid','marks','url']
	column_filters = ['answerid','testid','questionid','marks','url']
	

class MyAdminIndexView(AdminIndexView):
	def is_accessible(self):
		return True

db.create_all()
admin = Admin(app,index_view=MyAdminIndexView())
admin.add_view(MyTestView(test,db.session))
admin.add_view(MyQuestionView(question,db.session))
admin.add_view(MyAnswerView(answer,db.session))

@app.route('/')
def index():
	result = {'hello': 'world'}
	return make_response(jsonify(result), 201)


from flask import Flask, url_for, send_from_directory, request
import logging, os
from werkzeug import secure_filename

file_handler = logging.FileHandler('server.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath


@app.route('/api/test/', methods = ['POST'])
def api_test():


@app.route('/api/test/question', methods = ['POST'])
def api_question():
	



@app.route('/api/upload/', methods = ['POST'])
def api_root():
    app.logger.info(PROJECT_HOME)
    if request.method == 'POST' and request.files['image']:
    	app.logger.info(app.config['UPLOAD_FOLDER'])
    	img = request.files['image']
    	img_name = secure_filename(img.filename)
    	create_new_folder(app.config['UPLOAD_FOLDER'])
    	saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
    	app.logger.info("saving {}".format(saved_path))
    	img.save(saved_path)
    	return send_from_directory(app.config['UPLOAD_FOLDER'],img_name, as_attachment=True)




if __name__ == '__main__':
	app.debug = True
	app.secret_key = os.urandom(12)
	db.create_all()

app.run(debug = True,threaded=True, host="0.0.0.0",port=5000)