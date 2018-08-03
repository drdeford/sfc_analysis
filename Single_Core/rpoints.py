from rorder import r
from operator import itemgetter, attrgetter
import math
import matplotlib.pyplot as plt
def rpoint(point_list):
    for i in range(len(point_list)):
        point_list[i].append(int(r(math.sqrt(len(point_list)),point_list[i][0],point_list[i][1])))
    for j in range(len(point_list)):
        plt.text(point_list[j][0]/math.sqrt(len(point_list)),point_list[j][1]/math.sqrt(len(point_list)),str(point_list[j][2]),fontsize=6)
    plt.show()
    point_list=sorted(point_list,key=itemgetter(2))
    return point_list
    
