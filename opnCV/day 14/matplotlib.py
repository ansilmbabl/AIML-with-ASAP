
# 1 matplotlib

from matplotlib import pyplot as plt

x1=[4,3,8]
y1=[3,4,6]
x2=[4,2,6]
y2=[9,3,6]

plt.plot(x1,y1,color="r",label="first set",linewidth=4)
plt.plot(x2,y2,color="b",label="first set",linewidth=4)

plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.title("Plotting values")
plt.legend()
plt.show()

# 2 matplotlib
from matplotlib import pyplot as plt
plt.title("plot 2")
plt.plot([1,2,3],[4,5,6],color="g",label="abcd",linewidth=1)
plt.legend()
plt.show()
