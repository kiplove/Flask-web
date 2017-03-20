from flask import Flask,url_for,flash
from flask import render_template,session,redirect
from flask_script import Manager,Shell
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
import os

basedir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'+ os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
migrate=Migrate(app,db)

class NameForm(FlaskForm):
	name=StringField('What is your name?',validators=[Required()])
	sumit=SubmitField('Sumbit')

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	users = db.relationship('User',backref='role', lazy='dynamic')

	def __repr__(self):
		return '<Role %r>' % self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

	def __repr__(self):
		return '<User %r>' % self.username

#app=Flask(__name__)
bootstrap=Bootstrap(app)
manager=Manager(app)

def make_shell_context():
	return dict(app=app,db=db,User=User,Role=Role)
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username = form.name.data)
			db.session.add(user)
			session['known'] = False
		else:
			session['known'] = True
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('index'))
	return render_template('index.html',form = form, name = session.get('name'),known = session.get('known', False))

@app.route('/')
def html():
	return '<h1>Hello World</h1>'

@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html',name=name)

@app.route('/user',methods=['POST','GET'])
def user(name=None):
	form=NameForm()
	if form.validate_on_submit():
		old_name=session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you change your name!')
		session['name']=form.name.data
		return redirect(url_for('user'))
	return render_template('index.html',form=form,name=session.get('name'))

@app.route('/login',methods=['POST','GET'])
def login():
	error=None
	if request.method=='POST':
		if volid_login(request.form['username'],request.form['password']):
			return log_the_user_in(request.form['username'])
		else:
			error='Invalid username/password'
	return render_template('login.html',error=error)

with app.test_request_context():
	print url_for('static',filename='style')

if __name__=='__main__':
	manager.run()

