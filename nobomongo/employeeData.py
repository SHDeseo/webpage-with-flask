from pymongo import MongoClient
client = MongoClient('192.168.0.46', 27017)
db = client.EmployeeData
def main():
    while(1):
        selection = input("\n 선택 1)삽입 2)수정 3)출력 4)삭제 9)종료 \n")
        if selection == '1':    insert();      continue;
        elif selection == '2':    update();    continue;
        elif selection == '3':    read();      continue;
        elif selection == '4':    delete();    continue;
        elif selection == '9': break;
        else: print("잘못된 선택입니다.")                    

def insert():
    try:
        employeeId = input("input ID")
        employeeName = input("input name")
        employeeAge = input("input Age")
        employeeCountry = input("input Country")
        db.Employee.insert_one(
        { 'id' :employeeId, 'name' : employeeName, 'age': employeeAge,
        'country' : employeeCountry
        })
        print("데이터가 성공적으로 입력되었습니다. ")
    except Exception as e:
        print(e)

def update():
    try:
        criteria = input("input id")
        name = input("input name to update")
        age = input("input age to update")
        country = input("input country to update")
        db.Employee.update_one(
            {"id": criteria},
            { '$set':{'name': name, 'age':age, 'country':country }
            })
        print("데이터가 성공적으로 입력되었습니다.")
    except Exception as e:
        print(e)

def read():
    try:
        empCol = db.Employee.find()
        print("데이터를 출력합니다.")
        for emp in empCol:
            print(emp)
    except Exception as e:
        print(e)


def delete():
    try:
        criteria = input("input id to delete")
        db.Employee.delete_many({"id":criteria})
        print("데이터가 성공적으로 삭제 되었습니다.")
    except Exception as e:
        print(e)
main()