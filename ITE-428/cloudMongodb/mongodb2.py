import pymongo
import dns
import csv
from datetime import datetime


# update set column=? where ...
def updateData():
    with pymongo.MongoClient(cloudDatabase) as conn:
        db = conn.get_default_database()
        # db = conn.get_database('')
        # update_one(where , set)     update_many(where , set)
        where = {'student_id': '1913110027'}
        setTo = {'$set': {'major': 'DC'}}
        res = db.students.update_one(where, setTo)
        print("{} -- {}".format(res.matched_count, res.modified_count))


def deleteData():
    with pymongo.MongoClient(cloudDatabase) as conn:
        db = conn.get_database('Tni')
        # .delete_one(where) --> ลบตัวแรกที่เจอ  , .delete_many(where) --> ลบทุกตัวที่เจอ
        where = {'student_id': '21013909091'}
        res = db.students.delete_one(where)
        print("{}".format(res.deleted_count))


# sample_airbnb
def cleaning_fee():
    with pymongo.MongoClient(cloudDatabase) as conn:
        db = conn.get_database('sample_airbnb')
        # number_of_reviews>150 และมี cleaning_fee ด้วย
        con1 = {'number_of_reviews': {'$gt': 150}}
        con2 = {'cleaning_fee': {'$exists': True}}
        where = {'$and': [con1, con2]}
        # where = {'$and': [{'number_of_reviews': {'$gt': 150}}, {'cleaning_fee': {'$exists': True}}]}
        cursor = db.listingsAndReviews.find(where)
        found = db.listingsAndReviews.count_documents(where)
        print("พบข้อมูล {:,}".format(found))
        no = 1
        for i in cursor:
            print("{}.) {} -- {}".format(no, i['name'], i['listing_url']))
            print("{}".format(i['cleaning_fee']))
            no += 1


def airbnb_no_of_reviews():
    with pymongo.MongoClient(cloudDatabase) as conn:
        db = conn.get_database('sample_airbnb')
        where = {}
        cursor = db.listingsAndReviews.find(where)

        line()
        for i in cursor:
            print("NAME = {}".format(i['name']))
            print("TOTAL COMMENT : {}".format(i['number_of_reviews']))
            # print("TOTAL COMMENT : {}".format(len(i['reviews'])))
            line()


def see_reviews():
    with pymongo.MongoClient(cloudDatabase) as conn:
        db = conn.get_database('sample_airbnb')
        name = input("Please Enter AirBnb Name : ")
        where = {'name': {"$regex": '^' + name + '$', "$options": "i"}}
        # where = {'name': name}
        cursor = db.listingsAndReviews.find(where)
        found = db.listingsAndReviews.count_documents(where)
        if found:
            line()
            print("NAME : {}".format(cursor[0]['name']))
            print("TOTAL {} COMMENT(S)".format(cursor[0]['number_of_reviews']))
            line()
            for i, v in enumerate(cursor[0]['reviews']):
                print(" {}.) {}\n".format(i + 1, v['comments']))
        else:
            print("No Data Found")


def export_air_bnb_location():
    with pymongo.MongoClient(cloudDatabase) as conn:
        db = conn.get_database('sample_airbnb')
        where = {'address.location.is_location_exact': True}
        cursor = db.listingsAndReviews.find(where)

    with (open(file="Exportdata/data_air_bnb.csv", mode='w', encoding='utf8', newline="")) as f:
        fw = csv.writer(f)
        fw.writerow(['Place', 'Country', 'Latitude', 'Longitude'])
        for i in cursor:
            country = i['address']['country']
            latitude = i['address']['location']['coordinates'][1]
            longitude = i['address']['location']['coordinates'][0]
            data = [i['name'], country, latitude, longitude]
            fw.writerow(data)

    print("Export Success")


# sample_restaurants
def show_average_Score():
    with pymongo.MongoClient(cloudDatabase) as conn:
        db = conn.get_database('sample_restaurants')
        name = input("กรอก restaurant_id ที่ต้องการดูคะแนนเฉลี่ย : ")
        where = {'restaurant_id': name}
        found = db.restaurants.count_documents(where)
        if found:
            cursor = db.restaurants.find(where)
            print("{}\n".format(cursor[0]['name']))
            sum = 0
            for i, v in enumerate(cursor[0]['grades']):
                sum += v['score']
                print("Score {:>2} = {:>3}".format(i + 1, v['score']))
            print("\nAVERAGE = {:.2f}".format(sum / (i + 1)))
        else:
            print("ไม่พบ restaurant_id")


# sample_mflix
def comment_mflix():
    movie_name = input("หนังที่ต้องการ Comment : ")
    with pymongo.MongoClient(cloudDatabase) as conn:
        db = conn.get_database('sample_mflix')
        where = {'title': {"$regex": '^' + movie_name + '$', "$options": "i"}}
        found = db.movies.count_documents(where)
        if found:
            cursor = db.movies.find(where)
            movie_id = cursor[0]['_id']
            db.comments.insert_one({'name': "{} {}".format(input("ชื่อ : "), input("นามสกุล : ")),
                                    'email': input("E-mail : "),
                                    'movie_id': movie_id,
                                    'text': input("Comment ว่า : "),
                                    'date': datetime.now()
                                    })
            print("\nComment Success")
        else:
            print("ไม่พบหนังที่ต้องการ")


def line():
    print('-' * 50)


if __name__ == '__main__':
    # cloudDatabase = "mongodb+srv://test:e8KEYpEiuQFuurV3@cluster0.hf3dm.mongodb.net/Tni?retryWrites=true&w=majority"
    cloudDatabase = "mongodb+srv://Phurit:BtBIeP0act7akXn5@cluster0.rqhdl.mongodb.net/Tni?retryWrites=true&w=majority"

    # updateData()
    # deleteData()

    # sample_airbnb
    # cleaning_fee()
    # airbnb_no_of_reviews()
    # see_reviews()
    # export_air_bnb_location()

    # sample_restaurants
    # show_average_Score()

    # sample_mflix
    comment_mflix()
