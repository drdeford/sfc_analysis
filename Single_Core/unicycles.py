from torinnsearch import NNA as NNAS
from torinntreedist import NNA as NNAT
import math
def unisearch(size):
    p=[]
    for i in ['h','g','z','r']:
        p.append(NNAS('every',size,size**2,i,size,1,'linear',i,size))
    return p
def unitree(size):
    p=[]
    for i in ['h','g','z','r']:
        for j in ['h','g','z','r']:
            for k in [int(math.sqrt((size**2)/100))+1,int(math.sqrt((size**2)/10))+1,size,size**2]:
                p.append(NNAT('every',size,size**2,i,size,2,'torus',j,k))
    return p
