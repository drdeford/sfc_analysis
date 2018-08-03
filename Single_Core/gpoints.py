from gorder import g
import math
from operator import itemgetter, attrgetter
import matplotlib.pyplot as plt
def gpoint(point_list):
    for i in range(len(point_list)):
        point_list[i].append(g(math.sqrt(len(point_list)),point_list[i][0],point_list[i][1],0,0))
    plt.xlim((0,int(math.sqrt(len(point_list)))))
    plt.ylim((0,int(math.sqrt(len(point_list)))))
    for j in range(len(point_list)):
        plt.text(point_list[j][0],point_list[j][1],str(point_list[j][2]),fontsize=3)
    plt.show()
    point_list=sorted(point_list,key=itemgetter(2))
    return point_list
