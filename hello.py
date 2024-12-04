from flask import Flask
from markupsafe import escape
from flask import abort, redirect, url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

# @app.route("/hello")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
    
# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()

# url_for('static', filename='style.css')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    #abort(401)
    return render_template('hello.html', person=name)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    print(url_for('hello', person='Somebody'))
