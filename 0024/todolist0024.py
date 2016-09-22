# coding: utf-8
# 题目: 使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用。
# 思路: 1.登录页面,主页面;2.主页面需要从数据库加载内容;3.每提交或删除一次都要重新加载页面

from flask import Flask, request, session, flash, render_template, redirect, url_for, g
import MySQLdb as mysql

# config
USERNAME = 'admin'
PASSWORD = '940720'
SECRET_KEY = 'zhaoyeyu'

app = Flask(__name__)
app.config.from_object(__name__)

# 连接数据库
@app.before_request
def connect_db():
	g.db = mysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='940720', db='python_practice', charset='utf8')


# 主界面
@app.route('/')
def home():
	return render_template('index.html')


# 登录页面
@app.route('/login', methods=['POST', 'GET'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin':
			error = 'Invalid username!'
		elif request.form['password'] != '940720':
			error = 'Invalid password!'
		else:
			session['logged_in'] = True
			flash('Successfully logged.')
			return redirect(url_for('show_tasks'))
	return render_template('login.html', error=error)


# 主界面
@app.route('/show_tasks')
def show_tasks():
	sql = 'SELECT task from tasks'
	cursor = g.db.cursor()
	result = cursor.execute(sql)
	tasks = cursor.fetchall()
	return render_template('show_tasks.html', tasks=tasks)


# 添加条目
@app.route('/add', methods=['GET', 'POST'])
def add_task():
	if request.method == 'POST':
		sql = 'INSERT tasks (task) VALUES (%s)'
		g.db.cursor().execute(sql, request.form['content'])
		g.db.commit()
		flash('New entry was successfully posted.')
		return redirect(url_for('show_tasks'))
	# 重定向的主页面
	# return redirect(url_for('show_entries'))
	return render_template('add.html')

if __name__ == "__main__":
	app.run(debug=True)
