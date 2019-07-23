import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv('startbucks.csv')
print(df)
# grouped=df.groupby('city').apply(lambda x:x.count())#各城市星巴克数量
grouped=df.groupby('city').size()#各城市星巴克数量
print(grouped.index)
print(type(grouped))
squares=[]
for x in grouped.index:
    squares.append(grouped[x])
print(squares)

plt.plot(squares, linewidth=5)  # 这里只指定了一个列表，那么就当作是输出参数，输入参数从0开始，就会发现没有正确绘制数据
plt.title("Square Numbers", fontsize=24)  # 指定标题，并设置标题字体大小
plt.xlabel("Value", fontsize=14)  # 指定X坐标轴的标签，并设置标签字体大小
plt.ylabel("Square of Value", fontsize=14)  # 指定Y坐标轴的标签，并设置标签字体大小
plt.tick_params(axis='both', labelsize=14)  # 参数axis值为both，代表要设置横纵的刻度标记，标记大小为14
plt.show()  # 打开matplotlib查看器，并显示绘制的图形