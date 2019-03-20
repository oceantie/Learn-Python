import csv
headers={'username','age','height'}
value=[
    {'王强',12,123},
    {'lily',16,155},
    {'carl',18,190}
]
values=[
    {'username':'王强','age':11,'height':22},
    {'username':'李四','age':11,'height':21},
    {'username':'张四','age':41,'height':21}
]
# with open('classroom.csv','w',newline="") as fp:
#     writer=csv.writer(fp)
#     writer.writerow(headers)
#     writer.writerows(value)

with open('classroom.csv','w',newline='') as fp:
    writer = csv.DictWriter(fp,headers)
    #写入表头数据需要调writeheader
    writer.writeheader()
    writer.writerows(values)