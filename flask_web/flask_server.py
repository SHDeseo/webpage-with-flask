from flask import Flask, request, render_template, redirect
from dao import sungjuk

app = Flask(__name__)
app.secret_key = 'acorn academy deeplearning school'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/table")
def table_test():
    return render_template("table.html")

@app.route("/image_map")
def image_map():
    return render_template("image_map.html")

@app.route("/acorn_academy")
def acorn_academy():
    return render_template("acorn_academy.html")

@app.route("/js_for")
def js_for():
    return render_template("js_for.html")

@app.route("/form_select")
def form_select():
    return render_template("form_select.html")


@app.route("/bootstrap1")
def bootstrap1():
    return render_template("bootstrap1.html")

@app.route("/sungjuk")
def sungjuk1():
    result = sungjuk.getSungjuk()
    return render_template("sungjuk.html",object_list=result)

@app.route("/sungjukAct", methods=["GET","POST","PUT","DELETE"])
def sungjukAct():
    if request.method == 'GET' :#데이터 수신
        return sungjuk.getSungjuk()
    elif request.method == 'POST' : #서버측 데이터 전달
        name = request.form['name1']
        kor = request.form['kor1']
        mat = request.form['mat1']
        eng = request.form['eng1']
        school = request.form['school1']
        sungData = {'name' : name, 'kor' : kor, 'mat' : mat, 'eng' : eng, 'school' : school}
        return sungjuk.setSungjuk(sungData)
    elif request.method == 'DELETE' : #삭제
        name = request.form['id']
        return sungjuk.delSungjuk(name)
    elif request.method == 'PUT': #수정시 호출
        sungdata = request.form
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print(sungdata)
        return sungjuk.putSungjuk(sungdata)

if __name__=='__main__':
    app.run(debug=True)

    