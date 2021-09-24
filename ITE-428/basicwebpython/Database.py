import pymysql


def connectDb():
    mydatabase = pymysql.connect(host="localhost",
                                 port=3306,
                                 user="root",
                                 passwd="",
                                 cursorclass=pymysql.cursors.DictCursor,
                                 database='northwind_mysql_python'
                                 )
    return mydatabase
