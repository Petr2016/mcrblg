from flask import render_template
from myapp import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Migel'}
    posts = [
            {
                'author': {'username': 'Migel'},
                'body': 'Beatiful day in Portland'
            },
            {
                'author': {'username':'Susan'},
                'body': 'The Avengers movie was so cool!'
            }
            ]
    #return "Hello, world!"
    return render_template('index.html', title='Home', user=user, posts=posts)
