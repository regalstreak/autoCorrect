from flask import Flask
from flask_mongoalchemy import MongoAlchemy

app = Flask(__name__)

app.config['MONGOALCHEMY_DATABASE'] = 'autocorrect'
app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://sai:Anksbro1@ds147125.mlab.com:47125/autocorrect'

db = MongoAlchemy(app)

class Test(db.Document):
	testid = db.IntField()
	testname = db.StringField()
	organized_by = db.StringField()
	testdate = db.StringField()
	venue = db.StringField()

class Question(db.Document):
	questionid = db.IntField()
	testid = db.IntField()
	questionSt = db.StringField()
	marks = db.IntField()
	answerVec = db.StringField()
	numOfParts = db.IntField()

class Answer(db.Document):
	answerid =  db.IntField()
	testid =  db.IntField()
	questionid =  db.IntField()
	marks =  db.IntField()
	url =  db.StringField()