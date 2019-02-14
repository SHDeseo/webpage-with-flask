from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId

client = MongoClient('192.168.0.46', 27017)
db = client.workmanage
todos = db.todo
userdatas = db.userdata

app = Flask(__name__)
title = "Flask를 이용한 작업리스트"
heading = "작업리스트"

def redirect_url():
    return request.args.get('next') or\
    request.referrer or\
    url_for('index')

@app.route("/list")
def lists():
    todos_l = todos.find()
    a1="active"
    return render_template('index.html', a1=a1, todos=todos_l, t=title, h=heading)

@app.route("/action", methods=['POST'])
def action():
    name=request.values.get("name")
    desc=request.values.get("desc")
    date=request.values.get("date")
    pr=request.values.get("pr")
    todos.insert({"name":name, "desc":desc, "date":date, "pr":pr, "done":"no"})
    return redirect("/list")

@app.route("/done")
def done ():
    id=request.values.get("_id")
    task=todos.find({"_id":ObjectId(id)})
    if(task[0]["done"]=="yes"):
        todos.update({"_id":ObjectId(id)}, {"$set": {"done":"no"}})
    else:
        todos.update({"_id":ObjectId(id)},{"$set":{"done":"yes"}})
    redir=redirect_url()
    return redirect(redir)


@app.route("/remove")
def remove():
    key=request.values.get("_id")
    todos.remove({"_id":ObjectId(key)}) #objectId값으로 반드시 변환해줘야함.
    return redirect("/list")

@app.route("/update")
def update():
    id=request.values.get("_id")
    task=todos.find({"_id":ObjectId(id)}) 
    return render_template('update.html', tasks=task, h=heading, t=title)

@app.route("/uncompleted")
def tasks():
    todos_1 = todos.find({"done":"no"})
    a2="active"
    return render_template('index.html', a2=a2, todos=todos_1, t=title, h=heading)


@app.route("/completed")
def completed():
    todos_1 = todos.find({"done":"yes"})
    a3="active"
    return render_template('index.html', a3=a3, todos=todos_1, t=title, h=heading)

@app.route("/sorting")
def sorting():
    todos_1 = todos.find().sort("date", pymongo.DESCENDING)
    a4="active"
    return render_template('index.html', a4=a4, todos=todos_1, t=title, h=heading)

@app.route("/action3", methods=['POST'])
def action3():
    name=request.values.get("name")
    desc=request.values.get("desc")
    date=request.values.get("date")
    pr=request.values.get("pr")
    id=request.values.get("_id")
    todos.update({"_id":ObjectId(id)}, {'$set': {"name":name, "desc":desc, "date":date, "pr":pr }})
    return redirect("/list")


@app.route("/", methods=['GET','POST'])
def sign_up():
    return render_template('login.html')

@app.route("/signup", methods=['GET','POST'])
def signup():
    email=request.values.get("email")
    pwd=request.values.get("pwd")
    userdatas.insert({"email":email, "pwd":pwd})
    return redirect("/list")


@app.route("/login", methods=['GET','POST'])
def login():
    email=request.values.get("email")
    pwd=request.values.get("pwd")

    task77=userdatas.find({"email":email,"pwd":pwd})
    if(task77[0]["email"]==email):
        if(task77[0]["pwd"]==pwd):
            return redirect("/list")

    else:
        return redirect("/") 

    


# w3school html5정리 
#메일, password 로 회원가입
#로그인 화면 /list로 입장.
#검색하는 부분을 해결하시오.

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)