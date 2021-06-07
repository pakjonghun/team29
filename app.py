from flask import Flask,render_template,request,jsonify

from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import hashlib
import datetime
import jwt

client = MongoClient('mongodb://127.0.0.1:27017', 27017)
app = Flask(__name__)
db = client.sparataWeb1

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

@app.route("/main")
def main():
    return render_template("main.html")


# / 로그인 get 페이지 입니다.
@app.route('/user/login', methods=['GET'])
def login():
    return render_template("login.html")

# / 로그인 post 페이지 입니다. 닉네임과 비밀번호를 처리합니다.
@app.route('/user/login', methods=['POST'])
def postLogin():
    nickName = request.form['nickName']
    password = request.form['password']
    print(nickName,password)

    # 비밀번호를 암호화 합니다.
    hashPassword = hashlib.sha256(password.encode('utf-8')).hexdigest();

    # 닉네임을 갖고있는 유저가 있는지 검색 합니다. 유저가 없으면 에러 메세지를 반환합니다.
    isUserExist = db.user.find_one({'nickName':nickName})
    if isUserExist is None:
        return jsonify({'ok':False,'err':'1'})
    else:
        # 비밀번호와 닉네임을 비교하고 결과를 반환합니다. 비밀번호가 다르면 에러 메세지를 반환합니다.
        isPasswordCorrect = isUserExist['password']==hashPassword
        if isPasswordCorrect is None:
            return jsonify({'ok':False,'err':'2'})


    # 닉네임과 비밀번호가 확인되면 메인 페이지를 jwt 토큰과 유저 정보를 반환 합니다.
    # 토큰 만료일은 하루 입니다.(60*24*60=86400)
    payload = {
        'id': nickName,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=86400)
    }
    token = jwt.encode(payload, 'secret_key', algorithm='HS256')
    return jsonify({'token':token,'user':isUserExist,'ok':True})

@app.route("/user/join")
def join():
    return render_template("join.html")

@app.route("/user/mypage")
def myPage():
    return render_template("mypage.html")









if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)



