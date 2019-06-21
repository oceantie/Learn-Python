import numpy as np
from matplotlib import pyplot as plt

# x = np.arange(1, 11)
# # y = 2 * x + 5
# # plt.title("Matplotlib demo")
# # plt.xlabel("x axis caption")
# # plt.ylabel("y axis caption")
# # plt.plot(x, y)
# # plt.show()
from matplotlib import pyplot as plt
x =  [5,8,10]
y =  [12,16,6]
x2 =  [6,9,11]
y2 =  [6,15,7]
plt.bar(x, y, align =  'center')
plt.bar(x2, y2, color =  'g', align =  'center')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()