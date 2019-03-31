from datetime import datetime, date
from functools import wraps
from flask import Flask,render_template,redirect, url_for,request,session,flash
import os
import random
import json
from flask import make_response, jsonify
from models import *
from flask_ngrok import run_with_ngrok
from flask_marshmallow import Marshmallow

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///autocorrect.sqlite3'
app.config['SECRET_KEY'] = "random string"
ma = Marshmallow(app)

# run_with_ngrok(app)



class TestSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("testid", "testname", "organized_by","testdate","venue")

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("test_detail", id="<id>"), "collection": ma.URLFor("tests")}
    )


test_schema = TestSchema()
tests_schema = TestSchema(many=True)


@app.route('/')
def index():
	# result = {'hello': 'world'}
	return jsonify({"result": {'hello': 'world'}})


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

@app.route('/api/test/', methods = ['POST', 'GET'])
def api_test():
	if request.method == 'POST':
		test = Test(testid=request.form['testid'], testname=request.form['testname'],	
							organized=request.form['organized'], testdate=request.form['testdate'],venue=request.form['venue'])
		test.save()

	data = Test.query.all()
	return tests_schema.jsonify(data)

@app.route('/api/test/question', methods = ['POST'])
def api_question():
	if request.method == 'POST':
		question = Question(questionid=request.form['questionid'], testid=request.form['test_id'],
							questionSt=request.form['question_st'], marks=random.randint(1,5), answerVec=request.form['answerVec'],
							numOfParts=request.form['numofparts'])
		question.save()



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


from flask import send_file
@app.route('/api/get_image.png')
def get_image():
    filename = '/home/sai/Desktop/GooglePay.png'
    return send_file(filename, mimetype='image/png')


if __name__ == '__main__':
	app.debug = True
	app.secret_key = os.urandom(12)
	app.run()