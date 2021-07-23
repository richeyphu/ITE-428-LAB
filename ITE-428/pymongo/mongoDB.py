import pymongo


# insert_one() , insert_many()
def InsertOne(db):
    with (pymongo.MongoClient('localhost', 27017)) as conn:  # (ip, port)
        database = conn.get_database(db)  # = use .....
        data = {'id': '1913110027', 'name': 'Phurit', 'weight': 70, 'height': 170}
        currentID = database.students.insert_one(data)
        print("_id = {}".format(currentID.inserted_id))
        print("Insert Success")


def InsertMany(db):
    with (pymongo.MongoClient('localhost', 27017)) as conn:  # (ip, port)
        database = conn.get_database(db)  # = use .....
        data1 = {'id': '201317832-2', 'name': 'Adisak', 'weight': 90, 'height': 170}
        data2 = {'id': '201317847-2', 'name': 'Sansanee', 'weight': 90, 'height': 170}
        data = [data1, data2]

        currentID = database.students.insert_many(data)  # data --> list of dictionary
        print("_id = {}".format(currentID.inserted_ids))
        print("Insert Success")


def finddata(db):
    with (pymongo.MongoClient('localhost', 27017)) as conn:
        DB = conn.get_database(db)
        # cursor = DB.Products.find({})
        # ราคามากกว่า 10000 บาท , และเรียงตามราคาจากมากไปน้อย
        condition = {'pprice': {'$gt': 10000}}
        orderby = [('pprice', -1), ('pname', 1)]  # list of tuple
        cursor = DB.Products.find(condition).sort(orderby)
        found = DB.Products.count_documents(condition)
        print("Found {} Records\n".format(found))
        for i in cursor:
            print("Phone ID    : {}".format(i['pid']))
            print("Phone name  : {}".format(i['pname']))
            print("Phone price : {}".format(i['pprice']))
            print('-' * 50)


def StadiumInLiverpool(db):  # City --> Liverpool
    with (pymongo.MongoClient('localhost', 27017)) as conn:
        DB = conn.get_database(db)
        condition = {'City': 'Liverpool'}
        orderby = [('Capacity', -1), ('Stadium_Name', 1)]
        cursor = DB.Clubs.find(condition).sort(orderby)
        found = DB.Clubs.count_documents(condition)
        print("Found {} Records\n".format(found))
        for i in cursor:
            print("Stadium Name : {}".format(i['Stadium_Name']))
            print("City         : {}".format(i['City']))
            print("Capacity     : {}".format(i['Capacity']))
            print('-' * 50)


if __name__ == '__main__':
    databasename1 = "tni_new"
    databasename2 = "mobileShop"
    databasename3 = "Stadium"

    # InsertOne(databasename1)
    # InsertMany(databasename1)

    # finddata(databasename2)
    StadiumInLiverpool(databasename3)
