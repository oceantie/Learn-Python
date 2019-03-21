
import pymysql

conn=pymysql.connect(host='localhost',user='root',password='123456',database='demo_python',port=3306)
cursor=conn.cursor()

# sql="""
# insert into user(id,username,age) values (1,'lilly',20)
#
# """
# cursor.execute(sql)
# conn.commit()
# # cursor.execute("SELECT VERSION()")
# # data=cursor.fetchone()
# # print(data)
# cursor.close()

sql="""
insert into student(id,username,age) values (null,%s,%s)

"""
sq2="""
insert into user(id,username,age) values (%s,%s,%s)

"""

username='spider'
age=12
cursor.execute(sql,(username,age))
conn.commit()
cursor.close()