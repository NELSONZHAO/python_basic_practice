# coding: utf-8

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
	return "Index Page"


@app.route('/hello')
def hello_world():
	return "Hello, World!"


@app.route('/user/<username>')
def profile(username):
	return 'User:%s' % username

if __name__ == "__main__":
	app.run()
