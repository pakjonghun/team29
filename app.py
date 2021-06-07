from flask import Flask,render_template

from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)
app = Flask(__name__)
db = client.DBNAME

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

data = {"name":"a"}

@app.route("/main")
def home():
    return render_template("main.html")

@app.route("/login")
def home():
    return render_template("login.html")

@app.route("/join")
def home():
    return render_template("join.html")

@app.route("/user/mypage")
def home():
    return render_template("mypage.html")



# 코드 넣는곳 입니다.






if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)


