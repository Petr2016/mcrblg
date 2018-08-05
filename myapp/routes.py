from flask import render_template
from myapp import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Migel'}
	return render_template('index.html', 
		title='Home', 
		user=user)
	#return "Hello, world!"