# coding: utf-8
# 题目:使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。

# coding: utf-8

from __future__ import with_statement
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
# 类似open
from contextlib import closing


# configuration/整个文件是一个项目配置基础文件,包括数据库路径,管理员名称及密码
DATABASE = '/Users/apple/PycharmProjects/python_exercise/practice/0023/0023.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'nelson'
PASSWORD = '940720'

# create our little application
app = Flask(__name__)
app.config.from_object(__name__)


# 连接数据库
def connect_db():
	# 打开一个数据库文件,返回数据库连接后的对象
	return sqlite3.connect(app.config['DATABASE'])


# 初始化数据库
def init_db():
	# 打开数据库(并在结束后退出)
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql') as f:
			# 执行创建数据库表的语句
			db.cursor().executescript(f.read())
		db.commit()


@app.before_request
def before_request():
	# g对象是一个线程安全的全局变量
	g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
	g.db.close()


# 展示首页
@app.route('/')
def show_entries():
	cur = g.db.execute('select title, text from entries order by id desc')
	entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
	return render_template('show_entries.html', entries=entries)


# 发布评论界面
@app.route('/add', methods=['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	g.db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'], request.form['text']])
	g.db.commit()
	flash('New entry was successfully posted.')
	# 重定向的主页面
	return redirect(url_for('show_entries'))


# 登录界面
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			# 设置session字典中logged_in属性为True
			session['logged_in'] = True
			flash('You were logged in')
			return redirect(url_for('show_entries'))
	return render_template('login.html', error=error)


@app.route('/logout')
def logout():
	# D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
	# If key is not found, d is returned if given, otherwise KeyError is raised
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))

if __name__ == "__main__":
	app.run(debug=True)
