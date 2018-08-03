from torinnsearch import NNA as NNAS
from torinntreedist import NNA as NNAT
def unisearch(size):
    p=[]
    for i in ['h','g','z','r']:
        p.append(NNAS('every',size,size**2,i,size,1,'linear',i,size))
    return p
def unitree(size):
    p=[]
    for i in ['h','g','z','r']:
        p.append(NNAT('every',size,size**2,i,size,6,'torus',i,size))
    return p
