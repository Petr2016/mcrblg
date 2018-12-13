from flask import render_template, flash, redirect
from myapp import app
from myapp.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Migel'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beatiful day in Protland!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The Avengers movie was so cool'
		}

	]
	return render_template('index.html', 
		title='Home', 
		user=user,
		posts=posts)
	#return "Hello, world!"

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(form.username.data,
			form.remember_me.data))
		return redirect(url_for('/index'))
	return render_template('login.html', title='Sign In', form=form)



