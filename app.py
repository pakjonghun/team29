from flask import Flask, render_template, jsonify

from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests


client = MongoClient('localhost', 27017)
app = Flask(__name__)
db = client.sparataWeb

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/join")
def join():
    return render_template("join.html")

<<<<<<< HEAD
@app.route("/user/mypage", methods=['GET'])
def show_column():
    columns = list(db.spartaWeb1.find({'like' : {'$gt':0}}, {'_id': False}))
    return jsonify({'my_columns' : columns})
=======
@app.route("/user/mypage")
def myPage():
    return render_template("mypage.html")
>>>>>>> 475dfdb (에러 해결)



# 코드 넣는곳 입니다.






if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)


