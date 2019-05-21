import pandas as pd
import numpy as np

def tax(s):
    ss = s - 3500
    if ss <= 0:
        return 0
    elif ss < 1500:
        return ss * 0.03
    elif ss < 4500:
        return ss * 0.1 - 105
    elif ss < 9000:
        return ss * 0.2 - 555
    elif ss < 35000:
        return ss * 0.25 - 1005
    elif ss < 55000:
        return ss * 0.3 - 2755
    elif ss < 80000:
        return ss * 0.35 - 5505
    else:
        return ss * 0.45 - 13505

df = pd.read_excel('salary.xlsx', sheet_name = 0)
ts = []
for s in df['工资']:
    ts.append(tax(s))
print(ts)
df['税'] = ts
# df1 = pd.DataFrame(data={'col1':[1,1], 'col2':[2,2]})
out = pd.ExcelWriter('salary_and_tax.xls')
df.to_excel(out)
out.save()




#读取excel
# df = pd.DataFrame(pd.read_excel('F:\\name.xlsx'))
# print (df)
#
# dft = pd.DataFrame([["王五",21],
#                     ["赵六",32]],columns=['name','age'])
# df = pd.concat([df,dft],ignore_index=True)
# print(df)
#
# #写入excel
# df.to_excel('E:\\excel_to_python.xlsx', sheet_name='bluewhale_cc')
#
# #写入Excel
# writer = pd.ExcelWriter('F:\\output.xlsx')
# df1 = pd.DataFrame(data={'col1':[1,1], 'col2':[2,2]})
# print(df1)
# df1.to_excel(writer,'Sheet12')
# writer.save()