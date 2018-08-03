import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math
import itertools
def bipoints(center,variance,n):
    data=np.random.multivariate_normal([center,center],[[variance,0],[0,variance]],n)
    x=[]
    y=[]
    for i in range(n):
        x.append(int(data[i][0]))
        y.append(int(data[i][1]))
    plt.scatter(x,y)
    plt.show()
    point_list=[]
    for j in range(n):
        point_list.append((x[j],y[j]))
    point_list=list(set(point_list))
    for k in range(len(point_list)):
        point_list[k]=list(point_list[k])
    return point_list





