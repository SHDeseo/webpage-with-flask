import json
import pymysql

def getConnection():
    return pymysql.connect(host='192.168.0.46', port= 3306, user='root',
    password='acorn1234', use_unicode=True, db="acorn",
    charset='utf8', autocommit=True)
def getSungjuk():
    conn = getConnection()
    cur = conn.cursor()
    cur.callproc("student_select")
    if (cur.rowcount):
        result = cur.fetchall()
        #print(result)
    else:
        #print(cur.rowcount)
        result = 0

    cur.close()
    conn.close()
    return result

def setSungjuk(sungData):
    conn = getConnection()
    cur = conn.cursor()
    args = (sungData['name'], sungData['kor'], sungData['mat'], sungData['eng'], sungData['school'],0)
    cur.callproc("student_insert",args)
    result = cur.rowcount
    cur.close()
    conn.close()
    return json.dumps({'rows' : result})

def delSungjuk(in_name):
    conn = getConnection()
    cur = conn.cursor()
    args = (in_name, 0)
    cur.callproc("student_delete", args)
    cur.execute('SELECT @_student_delete_1')
    result = cur.fetchone()
    result = cur.rowcount
    cur.close()
    conn.close()
    return json.dumps({'rows' : result})


def putSungjuk(sungData):
    conn = getConnection()
    cur = conn.cursor()

    args = (sungData["id5"], sungData["name1"], sungData["kor1"], sungData["mat1"], sungData["eng1"], 0)
    cur.callproc("student_update", args)
    cur.execute('SELECT @_student_update_5')
    result = cur.fetchone()
    result = cur.rowcount
    cur.close()
    conn.close()
    return json.dumps({'rows' :result})