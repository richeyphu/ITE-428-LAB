// 21-07-64 basic mongoDB
show dbs;  // ใช้แสดงฐานข้อมูลใน databse server
use tni;
db.createCollection("Students")
db.Students.insert({"sid":"201312342","name":"Adisak"})
db.Students.insert({"sid":"201312342","name":"Adisak","weight":90})
db.Students.insert({"sid":"201312342","name":"Adisak","Weight":90})  // Case-sensitive
db.Students.find();  // select * from Students;
db.dropDatabase();
