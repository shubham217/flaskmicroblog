
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'shubham'}
    posts = [
        {
            'author': {'username': 'John Cena'},
            'body': 'New season of flash starting today!'
        },
        {
            'author': {'username': 'Iron man'},
            'body': 'I am the strongest'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

