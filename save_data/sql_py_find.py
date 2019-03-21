
import pymysql

conn=pymysql.connect(host='localhost',user='root',password='123456',database='demo_python',port=3306)
cursor=conn.cursor()

#

sql="""
select username,age from student where id=2

"""

sql2="""
select * from student 

"""
cursor.execute(sql2)
#fetchone每次获得一条数据
while True:
    result=cursor.fetchone()
    if result:
        print(result)
    else:
        break

# result=cursor.fetchone()
# print(result)
conn.close()