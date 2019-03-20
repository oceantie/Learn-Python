import json

persons=[
    {
        'username':"张三",
        'age': 11
    },
    {
        'username': "李四",
        'age': 11
    },
]
#dumps把Python对象转化为字符串
#Python里只有基本类型即int，float，dic，str，tuple，list等才能转化为json
json_str=json.dumps(persons)
print(type(json_str))
print(json_str)
#json数据直接dump到文件中，关闭ensureasc码存入中文字符
with open('person.json','w',encoding='utf-8') as fp:
    json.dump(persons,fp,ensure_ascii=False)

#从文件中读取json，load

js_str='[{"username": "mike", "age": 11}, {"username": "mike", "age": 11}]'
persons=json.loads(js_str)
print(type(persons))
for person in persons:
    print(person)