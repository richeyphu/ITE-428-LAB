import pymongo
from datetime import datetime
import socket
import dns
import csv


def insertData():
    with pymongo.MongoClient(cloudDatabase) as conn:
        db = conn.get_database('Tni')
        # db.students.insert_one({})
        # db.students.insert_many([{},{},...])

        stu_id = "1913110027"
        name = "Phurit"
        lastname = "D."
        phy_data = {'weight': 70, 'height': 170}
        major = "IT"
        year = 3
        gpax = 3.97
        ip_addr = socket.gethostbyname(socket.gethostname())
        db.students.insert_one({'student_id': stu_id,
                                'name': name,
                                'lastname': lastname,
                                'physical_data': phy_data,
                                'major': major,
                                'year': year,
                                'gpax': gpax,
                                'from': ip_addr,
                                'updated': datetime.now()
                                })

        print("Insert Success")


def bmi():
    with pymongo.MongoClient(cloudDatabase) as conn:
        db = conn.get_default_database()
        condition = {}
        cursor = db.students.find(condition)
        found = db.students.count_documents(condition)
        print("พบ = {} รายการ\n".format(found))
        for i in cursor:
            bmi = getBMI(i['physical_data']['weight'], i['physical_data']['height'])
            print("{} {} (BMI={:.2f})".format(i['name'], i['lastname'], bmi))


def getBMI(w, h):
    return float(w) / (float(h) / 100) ** 2


def useStudents():
    with pymongo.MongoClient(cloudDatabase) as conn:
        db = conn.get_default_database()
        condition = {'major': 'IT'}
        cursor = db.students.find(condition)
        found = db.students.count_documents(condition)
        print("พบ = {} รายการ\n".format(found))
        for i in cursor:
            # print("{}".format(i))
            print("NAME : {}".format(i['name']))


def export_students():
    currentdate = str(datetime.now())
    currentdate = currentdate.split('.')[0]
    currentdate = currentdate.replace(':', '-')
    with (open(file="Exportdata/students_{}.csv".format(currentdate), mode='w', encoding='utf8', newline="")) as f:
        fw = csv.writer(f)
        fw.writerow(['ID', 'NAME', 'LASTNAME', 'GPAX', 'BMI'])
        fw.writerows(getQueryList())
    print("Export Success on {}".format(currentdate))


def getQueryList():
    with pymongo.MongoClient(cloudDatabase) as conn:
        db = conn.get_default_database()
        condition = {}
        cursor = db.students.find(condition)
        data = []
        for i in cursor:
            bmi = getBMI(i['physical_data']['weight'], i['physical_data']['height'])
            data.append([i['student_id'], i['name'], i['lastname'], i['gpax'], round(bmi, 2)])
        return data


if __name__ == '__main__':
    # cloudDatabase = "mongodb+srv://test:<password>@cluster0.hf3dm.mongodb.net/Tni?retryWrites=true&w=majority"
    cloudDatabase = "mongodb+srv://Phurit:<password>@cluster0.rqhdl.mongodb.net/Tni?retryWrites=true&w=majority"

    # hostname = socket.gethostname()
    # ip_address = socket.gethostbyname(hostname)
    # ip_address = socket.gethostbyname_ex(hostname)
    # print("{} -- {}".format(hostname, ip_address))
    # print("{}".format(datetime.now()))

    # insertData()
    # useStudents()
    bmi()
    # export_students()
