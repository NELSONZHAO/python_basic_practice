# coding: utf-8
# 题目:使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。

from flask import Flask
from flask import request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('0023home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
	return render_template('0023form.html')


@app.route('/signin', methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	if username == 'admin' and password == 'password':
		return render_template('0023signin-ok.html', username=username)
	return render_template('0023form.html', message='Bad username or password', username=username)

if __name__ == "__main__":
	app.run()

