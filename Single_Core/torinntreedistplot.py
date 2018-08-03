import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math
import itertools
import math
########### DISTRIBUTIONS #########################
#SELECT ALL POINTS
def allpoints(size,n):
    p=[]
    for i in range(size):
        for j in range(size):
            p.append([i,j])
    return p
#SELECT BIVARIATE POINTS
##import numpy as np
##import scipy as sp
####import matplotlib.pyplot as plt
##import math
##import itertools
def bipoints(center,n):
    data=np.random.multivariate_normal([center,center],[[.05*(center**2),0],[0,.05*(center**2)]],n)
    x=[]
    y=[]
    for i in range(n):
        x.append(int(data[i][0]))
        y.append(int(data[i][1]))
    for i in range(len(x)):
        if x[i]>2*center or x[i]<0:
            x[i]=int(np.random.randint(0,center))
        if y[i]>2*center or y[i]<0:
            y[i]=int(np.random.randint(0,center))
    plt.figure(5)
    plt.scatter(x,y)
    plt.show()
    point_list=[]
    for j in range(n):
        point_list.append((x[j],y[j]))
    point_list=list(set(point_list))
    for k in range(len(point_list)):
        point_list[k]=list(point_list[k])
    return point_list

#SELECT UNIFORM POINTS
##import numpy as np
##import scipy as sp
####import matplotlib.pyplot as plt
##import math
##import itertools
def upoints(center,n):
    low=0
    high=center*2
    x=np.random.randint(low,high,n)
    y=np.random.randint(low,high,n)
    plt.figure(5)
    plt.scatter(x,y)
    plt.show()
    point_list=[]
    for j in range(n):
        point_list.append((x[j],y[j]))
    point_list=list(set(point_list))
    for k in range(len(point_list)):
        point_list[k]=list(point_list[k])
    return point_list
#SELECT EXPONENTIAL POINTS
##import numpy as np
##import scipy as sp
####import matplotlib.pyplot as plt
##import math
##import itertools
def epoints(scale,n):
    x=np.random.exponential(scale,n)
    y=np.random.exponential(scale,n)
    
    for i in range(len(x)):
        if x[i]>2*scale or x[i]<0:
            x[i]=int(np.random.randint(0,scale))
        if y[i]>2*scale or y[i]<0:
            y[i]=int(np.random.randint(0,scale))
    x=x.astype(int)
    y=y.astype(int)
    plt.figure(5)
    plt.scatter(x,y)
    plt.show()
    point_list=[]
    for j in range(n):
        point_list.append((x[j],y[j]))
    point_list=list(set(point_list))
    for k in range(len(point_list)):
        point_list[k]=list(point_list[k])
    return point_list

#SELECT PARETO POINTS
##import numpy as np
##import scipy as sp
####import matplotlib.pyplot as plt
##import math
##import itertools
def paretopoints(scale,n):
    x=np.random.pareto(1,n)*scale
    y=np.random.pareto(1,n)*scale    
    for i in range(len(x)):
        if x[i]>2*scale or x[i]<0:
            x[i]=int(np.random.randint(0,scale))
        if y[i]>2*scale or y[i]<0:
            y[i]=int(np.random.randint(0,scale))
    x=x.astype(int)
    y=y.astype(int)
    plt.figure(5)
    plt.scatter(x,y)
    plt.show()
    point_list=[]
    for j in range(n):
        point_list.append((x[j],y[j]))
    point_list=list(set(point_list))
    for k in range(len(point_list)):
        point_list[k]=list(point_list[k])
    return point_list

#SELECT Power POINTS
##import numpy as np
##import scipy as sp
####import matplotlib.pyplot as plt
##import math
##import itertools
def powerpoints(scale,n):
    x=np.random.power(1,n)*scale
    y=np.random.power(1,n)*scale    
    for i in range(len(x)):
        if x[i]>2*scale or x[i]<0:
            x[i]=int(np.random.randint(0,scale))
        if y[i]>2*scale or y[i]<0:
            y[i]=int(np.random.randint(0,scale))
    x=x.astype(int)
    y=y.astype(int)
#    plt.figure(5)
#    plt.scatter(x,y)
#    plt.show()
    point_list=[]
    for j in range(n):
        point_list.append((x[j],y[j]))
    point_list=list(set(point_list))
    for k in range(len(point_list)):
        point_list[k]=list(point_list[k])
    return point_list

#SELECT Poisson POINTS
##import numpy as np
##import scipy as sp
####import matplotlib.pyplot as plt
##import math
##import itertools
def poissonpoints(scale,n):
    x=np.random.poisson(scale,n)
    y=np.random.poisson(scale,n)   
    for i in range(len(x)):
        if x[i]>2*scale or x[i]<0:
            x[i]=int(np.random.randint(0,scale))
        if y[i]>2*scale or y[i]<0:
            y[i]=int(np.random.randint(0,scale))
    x=x.astype(int)
    y=y.astype(int)
#    plt.figure(5)
#    plt.scatter(x,y)
#    plt.show()
    point_list=[]
    for j in range(n):
        point_list.append((x[j],y[j]))
    point_list=list(set(point_list))
    for k in range(len(point_list)):
        point_list[k]=list(point_list[k])
    return point_list

################ SFC's INDIVIDUAL################
#ROW SCAN ORDER
def r(size,x,y):
    order=x*size+y
    return order

#Z SCAN ORDER
#import math
def z(size,x,y):
    x=bin(x)
    y=bin(y)
    x=x[2:]
    y=y[2:]
    order='0'
    size=math.ceil(math.log(size,2))+1
    for j in range(size):
        if len(x)<size:
            x=order+x
        if len(y)<size:
            y=order+y
    for i in range(size):
        order=order+x[i]+y[i]
        
    order=int(order,2)
    return order

#G SCAN ORDER
#import math
#from curves import z
def g(size,x,y,order,orientation):
    x=bin(x)
    y=bin(y)
    x=x[2:]
    y=y[2:]
    d=0
    o=int(math.log(size,2))
    p=math.log(size,2)    
    for j in range(o):
        if len(x)<(p):
            x='0'+x
        if len(y)<(p):
            y='0'+y
    if size==2:
        if orientation==0:
            if x=='0' and y=='0':
                d=order
                
            
            if x=='0' and y=='1':
                d=order+1
                
              
            if x=='1' and y=='1':
                d=order+2
                
                
            if x=='1' and y=='0':
                d=order+3
                
                
        elif orientation==1: 
            if x=='1' and y=='1':
                d=order
                
                
            if x=='1' and y=='0':
               d=order+1
              
               
            if x=='0' and y=='0':
                d=order+2
                
                
            if x=='0' and y=='1':
                d=order+3
                
                
    elif size>2:
        
        if orientation==0:
            if x[0]=='0' and y[0]=='0':
                orienation=0
                d=order
                d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)
                
            elif x[0]=='0' and y[0]=='1':
                orientation=1
                d=order+((size/2)**2)
                d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)
                
            elif x[0]=='1' and y[0]=='1':
                orientation=1                           
                d=order+(2*(size/2)**2)
                d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)
                
               
            elif x[0]=='1' and y[0]=='0':
                orientation=0
                d=order+(3*(size/2)**2)
                d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)
                    
                    

        elif orientation==1: 
            if x[0]=='1' and y[0]=='1':
               #orientation=(orientation+1)%2
                orientation=1
                d=order
                d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)   
                
                
            elif x[0]=='1' and y[0]=='0':
                orientation=0
                d=order+((size/2)**2)
                d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)
               
            elif x[0]=='0' and y[0]=='0':
                orientation=0
                d=order+(2*(size/2)**2)
                d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)
                
            elif x[0]=='0' and y[0]=='1':
                #orientation=(orientation+1)%2
                orientation=1
                d=order+(3*(size/2)**2)
                d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)

    d=int(d)
    return d

#H SCAN ORDER
#import math
directions={
'u':{(0,0):(0,'r'),(0,1):(1,'u'),(1,1):(2,'u'),(1,0):(3,'l')},
'r':{(0,0):(0,'u'),(1,0):(1,'r'),(1,1):(2,'r'),(0,1):(3,'d')},
'l':{(1,1):(0,'d'),(0,1):(1,'l'),(0,0):(2,'l'),(1,0):(3,'u')},
'd':{(1,1):(0,'l'),(1,0):(1,'d'),(0,0):(2,'d'),(0,1):(3,'r')}
     }
def h(size,x,y):
    orientation='u'
    order=0
    x=bin(x)[2:]
    y=bin(y)[2:]
    o=int(math.log(size,2))
    p=math.log(size,2)
    for j in range(o):
        if len(x)<(p):
            x='0'+x
        if len(y)<(p):
            y='0'+y
    
    for i in range(o):
        order=int(bin(order)[2:]+'00',2)
        x_coord=int(x[i])
        y_coord=int(y[i])
        quad_order,orientation=directions[orientation][(x_coord,y_coord)]
        order=order+quad_order
    return order

################### SFC's ORDER LIST############
#ROW SCAN POINTS
#from curves import r
from operator import itemgetter, attrgetter
#import math
###import matplotlib.pyplot as plt
def rpoint(point_list,size):
    for i in range(len(point_list)):
        point_list[i].append(int(r(size,point_list[i][0],point_list[i][1])))
    #plt.xlim((0,size))
    #plt.ylim((0,size))
    #plt.figure(1)
    #plt.subplot(2,2,1)
    #for j in range(len(point_list)):
    #    plt.text(point_list[j][0],point_list[j][1],str(point_list[j][2]),fontsize=6)
    point_list=sorted(point_list,key=itemgetter(-1))
    for k in range(len(point_list)-1):
        plt.plot([point_list[k][0],point_list[k+1][0]],[point_list[k][1],point_list[k+1][1]])
    plt.show()
    #These next two lines return only an ordered list of points
    for m in range(len(point_list)):
        point_list[m]=point_list[m][:2]
    tree=spatial.KDTree(point_list)
    return point_list,tree
#Z SCAN POINTS
#from curves import z
#import math
from operator import itemgetter, attrgetter
##import matplotlib.pyplot as plt
def zpoint(point_list,size):
    for i in range(len(point_list)):
        point_list[i].append(z(size,point_list[i][0],point_list[i][1]))
  #  plt.xlim((0,int(math.sqrt(len(point_list)))))
  #  plt.ylim((0,int(math.sqrt(len(point_list)))))
  #  plt.figure(2)
   # plt.subplot(2,2,2)
  #  for j in range(len(point_list)):
   #     plt.text(point_list[j][0],point_list[j][1],str(point_list[j][2]),fontsize=6)
    point_list=sorted(point_list,key=itemgetter(-1))
    for k in range(len(point_list)-1):
        plt.plot([point_list[k][0],point_list[k+1][0]],[point_list[k][1],point_list[k+1][1]])
    plt.show()
    #These next two lines return only an ordered list of points
    for m in range(len(point_list)):
        point_list[m]=point_list[m][:2]
    tree=spatial.KDTree(point_list)
    return point_list,tree  
#G SCAN POINTS
#from curves import g
#import math
from operator import itemgetter, attrgetter
##import matplotlib.pyplot as plt
def gpoint(point_list,size):
    for i in range(len(point_list)):
        point_list[i].append(g(size,point_list[i][0],point_list[i][1],0,0))
 #   plt.xlim((0,int(math.sqrt(len(point_list)))))
 #   plt.ylim((0,int(math.sqrt(len(point_list)))))
 #   plt.figure(3)
 #   plt.subplot(2,2,3)
   # for j in range(len(point_list)):
   #     plt.text(point_list[j][0],point_list[j][1],str(point_list[j][2]),fontsize=6)
    point_list=sorted(point_list,key=itemgetter(-1))
    for k in range(len(point_list)-1):
        plt.plot([point_list[k][0],point_list[k+1][0]],[point_list[k][1],point_list[k+1][1]])
    plt.show()
    #These next two lines return only an ordered list of points
    for m in range(len(point_list)):
        point_list[m]=point_list[m][:2]
    tree=spatial.KDTree(point_list)
    return point_list,tree
    
# H SCAN POINTS
#from curves import h
#import math
from operator import itemgetter, attrgetter
##import matplotlib.pyplot as plt
def hpoint(point_list,size):
    for i in range(len(point_list)):
        point_list[i].append(h(size,point_list[i][0],point_list[i][1]))
 #   plt.xlim((0,int(math.sqrt(len(point_list)))))
  #  plt.ylim((0,int(math.sqrt(len(point_list)))))
   # plt.figure(4)
    #plt.subplot(2,2,4)
  #  for j in range(len(point_list)):
   #     plt.text(point_list[j][0],point_list[j][1],str(point_list[j][2]),fontsize=6)
    point_list=sorted(point_list,key=itemgetter(-1))
    for k in range(len(point_list)-1):
        plt.plot([point_list[k][0],point_list[k+1][0]],[point_list[k][1],point_list[k+1][1]])
    plt.show()
    #These next two lines return only an ordered list of points
    for m in range(len(point_list)):
        point_list[m]=point_list[m][:2]
    tree=spatial.KDTree(point_list)
    return point_list,tree


######################SPLIT POINTS ONTO PROCESSORS #########
#POINT SEPARATOR
#import math
def separate(point_list,num_pro):
    num_pro=num_pro**2
    #  while len(point_list)/num_pro != math.floor(len(point_list)/num_pro):
    ppp=math.floor(len(point_list)/(num_pro)) 
    extras=len(point_list)-((num_pro)*ppp)
    count=0
    for i in range(extras):
        for j in range(ppp+1):
            point_list[count].append(i)
            count=count+1
            
            #point_list[(ppp+1)*i+j].append(i)
    for k in range(extras,num_pro):
        for l in range(ppp):
            point_list[count].append(k)
            count=count+1
           # point_list[ppp*k+l].append(k)
    #for i in range(num_pro):
     #   for j in range(ppp):
    #        point_list[ppp*i+j].append(i)
   
    #for k in range(extras):
    #    point_list[-(k+1)].append(num_pro-1)        
    return point_list

######## FIND NN ##########
####SELECT NEIGHBORHOODS MORE EFFICIENTLY######
from scipy import spatial
def nndsmart(tree,point_list3,dist):
    l=len(point_list3)
    qdist=(2*dist+1)**2
    #b=point_list[:]
    a=[]
    for o in range(l):
        a.append(point_list3[o][:-1])
    #tree=spatial.KDTree(point_list2)
    query=tree.query(a,qdist,0,2,dist)[1]
    point_list3.append([0,0,-1])
    for i in range(l):
        #for k in tree.query([point_list2[i][0],point_list2[i][1]],qdist,0,1,dist)[1][0]:
        for k in query[i][1:]:
            #if k in range(l):
            point_list3[i].append(point_list3[k][2])
            
   # for j in range(l):
    #    for k in range(j+1,l):
           # if point_list[k][0] in range(point_list[j][0]-dist,point_list[j][0]+dist+1):
     #       if abs(point_list[j][0]-point_list[k][0])<=dist and abs(point_list[j][1]-point_list[k][1])<=dist:
      #          point_list[j].append(point_list[k][2])
       #         point_list[k].append(point_list[j][2])
    #for m in range(l):
    #    point_list[m]=point_list[m][2:]
    for i in range(l+1):
        point_list3[i][:] = (value for value in point_list3[i] if value != -1)
    point_list3.pop()
    return point_list3
    
###Select Neighborhoods 4
##
###import math
##def nn4(point_list):
##    p=[]
##    for j in range(len(point_list)):
##        p.append([j])
##    q=[]
##    for k in range(len(point_list)):
##        q.append([k])
##    for i in range(len(point_list)):
##        x=point_list[i][0]
##        y=point_list[i][1]
##        a=[[x+1,y],[x,y+1],[x,y-1],[x-1,y]]
##        p[i].append(a)
##    for l in range(len(point_list)):
##        for m in p[l][1]:
##            for n in range(len(point_list)):
##                if m[0]==point_list[n][0] and m[1]==point_list[n][1]:
##                    q[l].append(n)
##    return q
##    #Select Neighborhoods 8
##
###import math
##def nn8(point_list):
##    p=[]
##    for j in range(len(point_list)):
##        p.append([j])
##    q=[]
##    for k in range(len(point_list)):
##        q.append([k])
##    for i in range(len(point_list)):
##        x=point_list[i][0]
##        y=point_list[i][1]
##        a=[[x+1,y],[x+1,y+1],[x+1,y-1],[x,y+1],[x,y-1],[x-1,y],[x-1,y+1],[x-1,y-1]]
##        p[i].append(a)
##    for l in range(len(point_list)):
##        for m in p[l][1]:
##            for n in range(len(point_list)):
##                if m[0]==point_list[n][0] and m[1]==point_list[n][1]:
##                    q[l].append(n)
##    return q
##
###Select Neighborhoods 12
##
###import math
##def nn12(point_list):
##    p=[]
##    for j in range(len(point_list)):
##        p.append([j])
##    q=[]
##    for k in range(len(point_list)):
##        q.append([k])
##    for i in range(len(point_list)):
##        x=point_list[i][0]
##        y=point_list[i][1]
##        a=[[x+1,y],[x+1,y+1],[x+1,y-1],[x,y+1],[x,y-1],[x-1,y],[x-1,y+1],[x-1,y-1],[x+2,y],[x,y+2],[x,y-2],[x-2,y]]
##        p[i].append(a)
##    for l in range(len(point_list)):
##        for m in p[l][1]:
##            for n in range(len(point_list)):
##                if m[0]==point_list[n][0] and m[1]==point_list[n][1]:
##                    q[l].append(n)
##    return q
##
##
###Select Neighborhoods 20
##
###import math
##def nn20(point_list):
##    p=[]
##    for j in range(len(point_list)):
##        p.append([j])
##    q=[]
##    for k in range(len(point_list)):
##        q.append([k])
##    for i in range(len(point_list)):
##        x=point_list[i][0]
##        y=point_list[i][1]
##        a=[[x+1,y],[x+1,y+1],[x+1,y-1],[x,y+1],[x,y-1],[x-1,y],[x-1,y+1],[x-1,y-1],[x+2,y],[x,y+2],[x,y-2],[x-2,y],[x+1,y+2],[x+1,y-2],[x-1,y+2],[x-1,y-2],[x+2,y+1],[x-2,y+1],[x+2,y-1],[x-2,y-1]]
##        p[i].append(a)
##    for l in range(len(point_list)):
##        for m in p[l][1]:
##            for n in range(len(point_list)):
##                if m[0]==point_list[n][0] and m[1]==point_list[n][1]:
##                    q[l].append(n)
##    return q
##
###Select Neighborhoods 24
##
###import math
##def nn24(point_list):
##    p=[]
##    for j in range(len(point_list)):
##        p.append([j])
##    q=[]
##    for k in range(len(point_list)):
##        q.append([k])
##    for i in range(len(point_list)):
##        x=point_list[i][0]
##        y=point_list[i][1]
##        a=[[x+1,y],[x+1,y+1],[x+1,y-1],[x,y+1],[x,y-1],[x-1,y],[x-1,y+1],[x-1,y-1],[x+2,y],[x,y+2],[x,y-2],[x-2,y],[x+1,y+2],[x+1,y-2],[x-1,y+2],[x-1,y-2],[x+2,y+1],[x-2,y+1],[x+2,y-1],[x-2,y-1],[x+2,y+2],[x+2,y-2],[x-2,y-2],[x-2,y+2]]
##        p[i].append(a)
##    for l in range(len(point_list)):
##        for m in p[l][1]:
##            for n in range(len(point_list)):
##                if m[0]==point_list[n][0] and m[1]==point_list[n][1]:
##                    q[l].append(n)
##    return q
##
#############NEIGHBOR PROCCESSOR POSITIONS########
# NEIGHBOR DISTANCES
##def nnd(q,point_list):
##    NND_list=[]
##    for i in range(len(q)):
##        NND_list.append([i,point_list[i][-1]])
##    for j in range(len(q)):
##        for k in q[j][1:]:
##            NND_list[j].append(point_list[k][-1])
##            
##         #   for l in range(len(q)):
##          #      if k==point_list[l][-1]
##           # p[j].append(point_list[l][-1]
##        
##    
##    
##    return NND_list

################PROCESSOR TORII EMBEDDING######
#PROCESSOR EMBEDDING
#R order
def embedr(size):
    e=[]
    for i in range(size):
        for j in range(size):
            e.append([i,j])
    proc_list,tree=rpoint(e,size)
    return proc_list
#Z order
def embedz(size):
    e=[]
    for i in range(size):
        for j in range(size):
            e.append([i,j])
    proc_list,tree=zpoint(e,size)
    return proc_list
#G order
def embedg(size):
    e=[]
    for i in range(size):
        for j in range(size):
            e.append([i,j])
    proc_list,tree=gpoint(e,size)
    return proc_list

#H order
def embedh(size):
    e=[]
    for i in range(size):
        for j in range(size):
            e.append([i,j])
    proc_list,tree=hpoint(e,size)
    return proc_list

############Compute AVG.NN DISTANCE ########
def torus(proc_list,NND_list):
    ns=0
    parsum=0
    size=math.sqrt(len(proc_list))
    for i in range(len(NND_list)):
        ns=ns+len(NND_list[i][3:])
    for j in range(len(NND_list)):
        for k in NND_list[j][3:]:
            x_dist=abs(proc_list[NND_list[j][2]][0]-proc_list[k][0])
            y_dist=abs(proc_list[NND_list[j][2]][1]-proc_list[k][1])
            parsum=parsum+min(x_dist,abs(size-x_dist))+min(y_dist,abs(size-y_dist))
    average=parsum/ns
    return average

def grid(proc_list,NND_list):
    ns=0
    parsum=0
    size=math.sqrt(len(proc_list))
    for i in range(len(NND_list)):
        ns=ns+len(NND_list[i][3:])
    for j in range(len(NND_list)):
        for k in NND_list[j][3:]:
            x_dist=abs(proc_list[NND_list[j][2]][0]-proc_list[k][0])
            y_dist=abs(proc_list[NND_list[j][2]][1]-proc_list[k][1])
            parsum=parsum+x_dist+y_dist
    average=parsum/ns
    return average

def linear(proc_list,NND_list):
    ns=0
    parsum=0
    for i in range(len(NND_list)):
        ns=ns+len(NND_list[i][3:])
    for j in range(len(NND_list)):
        for k in NND_list[j][3:]:
            parsum=parsum+abs(NND_list[j][2]-k)
    average=parsum/ns
    return average

def cyclic(proc_list,NND_list):
    ns=0
    parsum=0
    for i in range(len(NND_list)):
        ns=ns+len(NND_list[i][3:])
    for j in range(len(NND_list)):
        for k in NND_list[j][3:]:
            parsum=parsum+min(abs(NND_list[j][2]-k),abs(len(NND_list)-abs(NND_list[j][2]-k)))
    average=parsum/ns
    return average
def hypercube(proc_list,NND_list):
    ns=0
    parsum=0
    distsum=0
    for i in range(len(NND_list)):
        ns=ns+len(NND_list[i][3:])
    for j in range(len(NND_list)):
        for k in NND_list[j][3:]:
            dist=bin(k^NND_list[j][2])[2:]
            for l in dist:
                parsum=parsum+int(l)
    average=parsum/ns
    return average
import os
def quadtree(proc_list,NND_list):
    ns=0
    parsum=0
    num_proc=len(proc_list)
    num_dig=math.ceil(math.log(num_proc,2))
    for i in range(len(NND_list)):
        ns=ns+len(NND_list[i][3:])
    for j in range(len(NND_list)):
        leafpos1=bin(NND_list[j][2])[2:]
        if len(leafpos1)<num_dig:
            for l in range(num_dig-len(leafpos1)):
                leafpos1='0'+leafpos1
        for k in NND_list[j][3:]:
            leafpos2=bin(k)[2:]
            if len(leafpos2)<num_dig:
                for l in range(num_dig-len(leafpos2)):
                    leafpos2='0'+leafpos2
            cp=len(os.path.commonprefix([leafpos1,leafpos2]))
            if cp%2==1:
                cp=cp-1
            dist=math.ceil((num_dig-cp)/2)
            parsum=parsum+2*dist
    average=parsum/ns
    return average
    
#######FINAL PRODUCT###########
distributions={
'normal':0,
'uniform':1,
'pareto':2,
'power':3,
'poisson':4,
'exponential':5,
'every':6
     }
sfcurves={
'h':0,
'g':1,
'z':2,
'r':3
}
topologies={
'torus':0,
'grid':1,
'linear':2,
'cyclic':3,
'hypercube':4,
'quadtree':5
}
embed_orders={
'h':0,
'g':1,
'z':2,
'r':3
}    
dist_list=[bipoints,upoints,paretopoints,powerpoints,poissonpoints,epoints,allpoints]
curve_list=[hpoint,gpoint,zpoint,rpoint]
topo_list=[torus,grid,linear,cyclic,hypercube,quadtree]
embed_list=[embedh,embedg,embedz,embedr]
def NNA(distribution,center,num_points,curve,size,nnd,topology,embed_order,num_proc):
  #  average=topo_list[topologies][topology](embed_list[embed_orders][embedded_order](num_proc),nndsmart(separate(curve_list[sfcurves][curve](dist_list[distributions][distribution](center,num_points),size),num_proc),nnd))
    topo=topologies[topology]
    topo=topo_list[topo]
    distro=distributions[distribution]
    distro=dist_list[distro]
    sfcurve=sfcurves[curve]
    sfcurve=curve_list[sfcurve]
    eorder=embed_orders[embed_order]
    eorder=embed_list[eorder]
    #a=distro(center,num_points)
    a=[[85, 107], [175, 87], [39, 282], [42, 10], [296, 163], [105, 232], [509, 235], [230, 1], [449, 296], [8, 168], [38, 86], [201, 101], [0, 98], [133, 30], [35, 15], [9, 0], [318, 26], [276, 131], [71, 26], [69, 89], [341, 278], [26, 157], [178, 123], [202, 204], [20, 75], [130, 170], [254, 107], [190, 194], [211, 34], [46, 79], [24, 290], [261, 154], [224, 286], [225, 75], [150, 131], [330, 70], [320, 53], [25, 49], [22, 187], [372, 33], [63, 5], [22, 48], [229, 47], [30, 16], [185, 501], [0, 67], [7, 25], [48, 77], [47, 143], [200, 420], [132, 301], [12, 156], [86, 55], [170, 170], [174, 65], [250, 44], [120, 472], [125, 194], [103, 450], [469, 38], [203, 384], [436, 337], [193, 129], [56, 201], [130, 70], [218, 187], [244, 90], [20, 501], [409, 133], [422, 1], [166, 32], [109, 144], [114, 93], [350, 138], [52, 6], [72, 263], [170, 64], [29, 107], [440, 171], [287, 61], [262, 200], [31, 18], [265, 15], [109, 196], [390, 10], [193, 334], [68, 315], [51, 485], [196, 205], [14, 332], [126, 241], [294, 130], [192, 229], [215, 335], [94, 30], [132, 162], [16, 51], [71, 8], [205, 43], [217, 10], [58, 148], [41, 360], [86, 26], [370, 91], [125, 53], [14, 172], [111, 137], [124, 40], [226, 162], [264, 47], [39, 68], [100, 7], [124, 4], [43, 260], [289, 57], [173, 46], [13, 250], [193, 113], [151, 213], [233, 49], [6, 146], [59, 86], [29, 183], [11, 290], [22, 30], [26, 85], [250, 430], [132, 169], [113, 156], [71, 1], [120, 49], [84, 31], [50, 91], [241, 188], [72, 61], [219, 190], [0, 387], [300, 92], [383, 128], [125, 228], [85, 120], [24, 9], [281, 282], [20, 292], [117, 123], [73, 2], [315, 178], [284, 464], [26, 3], [32, 82], [371, 293], [46, 253], [274, 159], [102, 12], [266, 310], [327, 109], [281, 119], [118, 99], [424, 14], [122, 110], [134, 231], [83, 275], [482, 208], [8, 33], [308, 450], [509, 96], [331, 330], [293, 101], [209, 184], [341, 255], [41, 63], [72, 368], [80, 135], [85, 11], [128, 246], [95, 353], [142, 351], [256, 52], [50, 37], [222, 317], [347, 327], [13, 18], [152, 226], [315, 382], [415, 51], [0, 9], [442, 208], [119, 133], [65, 9], [83, 306], [149, 251], [145, 224], [392, 85], [446, 220], [256, 427], [317, 231], [135, 95], [78, 181], [391, 11], [200, 17], [27, 54], [200, 154], [88, 95], [94, 183], [163, 66], [323, 185], [251, 280], [52, 226], [237, 218], [8, 472], [243, 2], [368, 213], [136, 338], [387, 93], [194, 15], [52, 145], [302, 168], [223, 289], [98, 304], [163, 57], [236, 128], [70, 298], [125, 92], [206, 70], [452, 429], [12, 274], [147, 382], [145, 217], [337, 108], [97, 263], [407, 294], [439, 25], [84, 282], [382, 146], [254, 175], [36, 20], [183, 241], [7, 234], [205, 281], [318, 169], [249, 115], [171, 256], [68, 23], [25, 91], [156, 161], [427, 250], [264, 124], [37, 131], [211, 171], [176, 71], [9, 26], [242, 151], [158, 32], [178, 281], [160, 19], [47, 192], [5, 324], [92, 182], [159, 172], [18, 70], [248, 45], [321, 137], [28, 26], [188, 498], [287, 222], [207, 247], [53, 14], [58, 443], [301, 238], [16, 413], [428, 31], [3, 62], [39, 281], [437, 165], [149, 209], [107, 114], [69, 131], [468, 55], [48, 392], [229, 138], [73, 468], [178, 98], [207, 62], [143, 309], [359, 88], [280, 143], [73, 183], [307, 0], [263, 446], [58, 126], [126, 262], [76, 93], [209, 452], [158, 390], [197, 30], [64, 500], [173, 174], [28, 234], [366, 185], [125, 12], [51, 139], [136, 105], [332, 242], [12, 175], [57, 219], [230, 215], [252, 32], [77, 229], [224, 357], [173, 63], [98, 507], [3, 174], [427, 109], [292, 170], [174, 50], [13, 66], [75, 459], [455, 486], [52, 40], [97, 356], [39, 327], [130, 55], [11, 229], [87, 53], [183, 0], [76, 126], [312, 193], [260, 29], [168, 27], [80, 38], [213, 169], [83, 115], [133, 171], [105, 34], [478, 78], [150, 64], [258, 290], [26, 8], [262, 153], [24, 248], [324, 121], [113, 217], [394, 97], [505, 3], [52, 59], [130, 44], [114, 471], [137, 3], [118, 439], [268, 219], [79, 148], [369, 509], [291, 138], [43, 487], [87, 212], [98, 175], [215, 102], [17, 27], [450, 187], [2, 401], [76, 5], [351, 61], [11, 59], [114, 236], [124, 208], [117, 82], [241, 20], [114, 282], [1, 146], [189, 300], [248, 66], [16, 79], [62, 212], [82, 31], [124, 410], [78, 105], [270, 87], [185, 184], [19, 213], [10, 126], [157, 253], [0, 431], [455, 204], [172, 217], [189, 20], [390, 127], [202, 44], [31, 379], [405, 68], [385, 134], [34, 66], [223, 350], [168, 75], [240, 71], [164, 224], [72, 78], [271, 472], [81, 476], [178, 240], [19, 135], [142, 89], [127, 112], [323, 95], [254, 16], [120, 183], [131, 58], [119, 173], [99, 34], [303, 277], [106, 43], [43, 491], [41, 66], [119, 360], [57, 472], [181, 93], [319, 241], [174, 283], [150, 114], [205, 83], [85, 433], [110, 87], [27, 475], [281, 215], [87, 83], [16, 235], [184, 231], [254, 259], [32, 206], [74, 109], [75, 105], [197, 206], [281, 320], [396, 503], [189, 120], [124, 109], [351, 35], [20, 80], [86, 63], [69, 29], [109, 118], [54, 212], [252, 255], [233, 67], [239, 88], [155, 46], [52, 97], [39, 50], [463, 65], [46, 219], [56, 193], [155, 223], [481, 43], [345, 50], [8, 249], [40, 201], [272, 10], [209, 128], [473, 101], [89, 134], [231, 217], [501, 366], [64, 357], [142, 142], [353, 75], [334, 87], [398, 72], [48, 76], [393, 90], [251, 10], [1, 195], [96, 207], [58, 29], [56, 236], [478, 8], [219, 74], [136, 189], [92, 8], [308, 18], [85, 13], [283, 0], [119, 80], [397, 56], [14, 126], [112, 114], [86, 91], [119, 78], [178, 169], [19, 45], [497, 116], [309, 39], [89, 22], [227, 142], [32, 220], [300, 373], [353, 181], [250, 43], [74, 102], [119, 432], [457, 321], [489, 104], [207, 437], [313, 6], [118, 16], [206, 134], [85, 286], [63, 214], [243, 238], [72, 166], [241, 48], [302, 317], [155, 379], [215, 94], [113, 71], [35, 0], [123, 147], [82, 4], [12, 211], [180, 74], [192, 176], [203, 219], [103, 93], [16, 103], [221, 59], [54, 20], [460, 47], [49, 134], [77, 141], [37, 73], [144, 189], [125, 10], [39, 114], [33, 422], [206, 256], [80, 339], [298, 150], [222, 487], [395, 211], [10, 41], [29, 157], [175, 347], [40, 258], [129, 58], [10, 18], [441, 137], [27, 504], [241, 3], [81, 290], [250, 169], [136, 177], [210, 467], [157, 218], [139, 39], [2, 222], [153, 113], [127, 402], [152, 239], [391, 219], [227, 65], [0, 111], [3, 89], [3, 28], [312, 244], [229, 91], [481, 10], [173, 95], [6, 296], [23, 420], [203, 62], [35, 178], [54, 59], [55, 171], [73, 502], [191, 310], [170, 121], [95, 319], [218, 149], [6, 34], [377, 21], [358, 129], [49, 196], [31, 183], [38, 41], [186, 174], [33, 153], [216, 37], [285, 21], [77, 165], [201, 306], [209, 205], [196, 140], [28, 321], [261, 20], [35, 300], [75, 44], [215, 263], [58, 313], [33, 213], [179, 114], [96, 245], [419, 118], [150, 4], [26, 55], [95, 0], [200, 18], [386, 490], [229, 46], [166, 14], [254, 433], [135, 229], [284, 91], [41, 31], [45, 66], [199, 72], [122, 82], [432, 465], [135, 131], [300, 271], [185, 115], [162, 83], [38, 171], [109, 228], [23, 8], [159, 6], [219, 141], [5, 201], [293, 20], [26, 106], [74, 32], [443, 169], [21, 210], [377, 106], [115, 114], [324, 252], [507, 180], [126, 32], [103, 378], [287, 292], [64, 147], [1, 14], [311, 453], [180, 107], [175, 202], [234, 24], [357, 232], [83, 53], [424, 283], [89, 58], [13, 192], [274, 170], [170, 107], [259, 175], [314, 3], [32, 91], [49, 214], [176, 316], [63, 91], [246, 34], [9, 49], [63, 67], [73, 74], [30, 196], [246, 202], [106, 2], [127, 93], [19, 243], [244, 9], [13, 142], [110, 4], [506, 197], [263, 114], [203, 221], [155, 248], [51, 130], [396, 4], [199, 10], [33, 231], [241, 205], [37, 98], [238, 168], [287, 331], [233, 46], [6, 6], [3, 128], [150, 81], [172, 70], [29, 54], [492, 84], [177, 12], [219, 287], [247, 364], [5, 257], [395, 76], [260, 510], [203, 230], [58, 178], [223, 112], [405, 20], [495, 183], [119, 10], [66, 178], [270, 179], [7, 59], [226, 107], [36, 158], [383, 44], [304, 65], [48, 346], [284, 236], [7, 72], [153, 312], [321, 308], [280, 180], [52, 116], [78, 30], [371, 16], [85, 130], [73, 392], [248, 144], [153, 153], [96, 103], [9, 119], [205, 198], [353, 197], [114, 38], [130, 449], [454, 76], [82, 235], [28, 280], [478, 372], [60, 415], [140, 105], [76, 103], [346, 86], [92, 9], [367, 385], [34, 45], [57, 87], [23, 13], [313, 105], [51, 117], [98, 327], [30, 65], [75, 260], [25, 389], [10, 181], [155, 211], [207, 193], [21, 94], [52, 28], [84, 328], [94, 371], [404, 409], [327, 221], [217, 68], [41, 303], [18, 111], [249, 248], [226, 190], [238, 134], [277, 356], [301, 192], [103, 426], [305, 91], [24, 213], [416, 19], [157, 176], [453, 355], [356, 42], [59, 20], [1, 249], [14, 485], [323, 93], [509, 202], [155, 178], [112, 392], [447, 80], [224, 306], [219, 6], [202, 242], [18, 61], [51, 153], [258, 185], [141, 361], [36, 48], [423, 449], [16, 199], [137, 13], [241, 339], [299, 132], [68, 70], [57, 95], [99, 0], [109, 35], [125, 170], [148, 94], [101, 134], [144, 466], [66, 108], [38, 109], [372, 136], [271, 68], [75, 335], [312, 11], [85, 71], [55, 50], [142, 54], [179, 9], [153, 62], [106, 330], [198, 220], [12, 327], [237, 47], [19, 132], [171, 163], [155, 48], [139, 346], [3, 73], [155, 324], [205, 189], [425, 36], [35, 157], [222, 115], [282, 16], [396, 183], [9, 25], [124, 51], [442, 276], [65, 248], [147, 252], [49, 41], [223, 475], [244, 162], [157, 84], [29, 83], [78, 248], [421, 147], [205, 241], [66, 77], [7, 272], [44, 93], [80, 184], [67, 260], [134, 80], [100, 139], [75, 16], [61, 241], [3, 130], [409, 243], [125, 220], [273, 138], [112, 190], [38, 193], [11, 34], [404, 87], [292, 59], [29, 187], [30, 43], [198, 215], [323, 166], [98, 216], [17, 314], [40, 262], [194, 100], [186, 185], [413, 219], [210, 407], [66, 176], [239, 214], [74, 150], [88, 221], [44, 332], [381, 42], [84, 0], [230, 99], [21, 105], [364, 159], [33, 103], [195, 186], [106, 182], [16, 82], [62, 134], [31, 124], [46, 369], [40, 12], [98, 9], [296, 22], [204, 144], [384, 49], [231, 81], [203, 50], [16, 508], [40, 91], [175, 364], [114, 254], [125, 83], [21, 1], [4, 79], [47, 235], [328, 8], [4, 313], [247, 111], [6, 77], [24, 257], [36, 450], [49, 91], [119, 327], [275, 277], [32, 118], [242, 301], [45, 239], [149, 0], [10, 106], [106, 38], [23, 328], [125, 181], [389, 83], [205, 70], [211, 62], [380, 256], [162, 359], [209, 37], [227, 322], [506, 142], [307, 83], [154, 22], [225, 145], [41, 32], [123, 205], [156, 143], [171, 481], [73, 94], [36, 75], [150, 202], [133, 2], [276, 191], [18, 33], [408, 66], [179, 182], [104, 233], [17, 55], [3, 436], [151, 41], [175, 324], [223, 118], [80, 256], [336, 85], [199, 287], [156, 72], [365, 51], [11, 24], [424, 179], [188, 18], [284, 63], [471, 5], [120, 125], [152, 327], [76, 0], [315, 50], [118, 22], [158, 401], [365, 315], [298, 143], [435, 143], [306, 70], [129, 230], [35, 83], [204, 43], [105, 231], [10, 260], [26, 410], [278, 178], [281, 79], [136, 170], [155, 141], [29, 289], [299, 442], [61, 184], [184, 45], [94, 464], [59, 5], [126, 313], [304, 188], [167, 72], [138, 41], [10, 148], [72, 400], [150, 150], [29, 254], [369, 160], [70, 166], [66, 75], [122, 293], [360, 284], [163, 176], [110, 37], [76, 156], [3, 132], [105, 465]]
    b,c=sfcurve(a,size)
    d=separate(b,num_proc)
    e=nndsmart(c,d,nnd)
    average=topo(eorder(num_proc),e)
    
#    average=topo(eorder(num_proc),nndsmart(separate(sfcurve(distro(center,num_points),size),num_proc),nnd))
    return average
##
def testit(n,size):
    a=bipoints(size,n)
    b,c=hpoint(a,2*size)
    r=c.query(b,9,0,1)[1]
    return r


def ltorus(e,qn,size):
	ns=0
	parsum=0
    #size=math.sqrt(len(proc_list)
	for q in range(len(qn)):
		ns=ns+len(qn[q][3:])
		for r in qn[q][3:]:
			x_dist=abs(e[r][0]-e[qn[q][2]][0])
			y_dist=abs(e[r][1]-e[qn[q][2]][1])
			parsum=parsum+min(x_dist,abs(size-x_dist))+min(y_dist,abs(size-y_dist))
	return parsum,ns
	
def lgrid(e,qn,size):
	ns=0
	parsum=0
    #size=math.sqrt(len(proc_list)
	for q in range(len(qn)):
		ns=ns+len(qn[q][3:])
		for r in qn[q][3:]:
			x_dist=abs(e[r][0]-e[qn[q][2]][0])
			y_dist=abs(e[r][1]-e[qn[q][2]][1])
			parsum=parsum+x_dist+y_dist
	return parsum,ns
	
def llinear(e,qn,size):
    ns=0
    parsum=0
    for q in range(len(qn)):
        ns=ns+len(qn[q][3:])
        for r in qn[q][3:]:
            parsum=parsum+abs(qn[q][2]-r)
    return parsum,ns
    
def lcyclic(e,qn,size):
    ns=0
    parsum=0
    for q in range(len(qn)):
        ns=ns+len(qn[q][3:])
        for r in qn[q][3:]:
            parsum=parsum+min(abs(qn[q][2]-r),abs(len(qn)-abs(qn[q][2]-r)))
    return parsum,ns
    
def lhypercube(e,qn,size):
    ns=0
    parsum=0
    for q in range(len(qn)):
        ns=ns+len(qn[q][3:])
        for r in qn[q][3:]:
            dist=bin(r^qn[q][2])[2:]
            for s in dist:
                parsum=parsum+int(s)
    return parsum,ns
    
def lquadtree(e,qn,size):
    ns=0
    parsum=0
    num_proc=len(e)
    num_dig=math.ceil(math.log(num_proc,2))
    for q in range(len(qn)):
        ns=ns+len(qn[q][3:])
        leafpos1=bin(qn[q][2])[2:]
        if len(leafpos1)<num_dig:
            for l in range(num_dig-len(leafpos1)):
                leafpos1='0'+leafpos1
        for r in qn[q][3:]:
            leafpos2=bin(r)[2:]
            if len(leafpos2)<num_dig:
                for l in range(num_dig-len(leafpos2)):
                    leafpos2='0'+leafpos2
            cp=len(os.path.commonprefix([leafpos1,leafpos2]))
            if cp%2==1:
                cp=cp-1
            dist=math.ceil((num_dig-cp)/2)
            parsum=parsum+2*dist
    return parsum,ns
