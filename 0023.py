# coding: utf-8
# 题目:使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', )
def home():
	return render_template()


@app.route('/', methods=['POST'])
def writenote():
	return render_template('0023book.html')

if __name__ == "__main__":
	app.run()

