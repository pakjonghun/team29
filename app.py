from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
<<<<<<< HEAD

client = MongoClient('localhost', 27017)
app = Flask(__name__)
db = client.spartaWeb
=======


client = MongoClient('localhost', 27017)
app = Flask(__name__)
db = client.sparataWeb
>>>>>>> 9687d444f5160441618253799984b489ed84cc67


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/main")
def main():
    return render_template("main.html")


@app.route("/join")
def join():
    return render_template("join.html")


# 코드 넣는곳 입니다.
@app.route('/main', methods=['GET'])
def get_main_page():
    articles = list(db.article.find({}, {'_id': False}))
    print(articles)
    return jsonify({'all_articles': articles})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
