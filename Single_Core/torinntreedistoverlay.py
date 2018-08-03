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

#SELECT PLOT POINTS

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
   # plt.show()
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
   # plt.show()
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
  #  plt.show()
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
#    plt.show()
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
    plt.figure(5)
    plt.scatter(x,y)
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
    plt.figure(5)
    plt.scatter(x,y)
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
 #   plt.show()
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
 #   plt.show()
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
 #   plt.show()
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
   #plt.show()
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
    
    a=[[62, 64], [59, 78], [88, 48], [56, 25], [85, 63], [66, 57], [60, 39], [71, 57], [67, 36], [72, 34], [53, 64], [69, 38], [67, 74], [63, 48], [80, 34], [55, 78], [49, 78], [66, 66], [67, 80], [56, 75], [84, 113], [44, 86], [83, 85], [46, 75], [70, 68], [71, 78], [36, 68], [60, 81], [26, 54], [53, 62], [59, 71], [57, 59], [82, 92], [36, 67], [85, 56], [83, 40], [66, 48], [72, 67], [39, 85], [86, 55], [60, 62], [67, 45], [63, 83], [61, 63], [68, 46], [40, 73], [62, 60], [86, 41], [67, 51], [94, 52], [37, 54], [70, 44], [68, 52], [48, 50], [55, 72], [103, 39], [77, 48], [82, 61], [46, 52], [70, 81], [45, 59], [51, 43], [57, 60], [54, 52], [55, 49], [70, 107], [62, 84], [40, 42], [54, 46], [51, 88], [65, 38], [55, 47], [47, 72], [43, 45], [49, 82], [76, 78], [68, 51], [42, 74], [81, 29], [45, 47], [49, 52], [63, 66], [80, 54], [62, 69], [57, 44], [47, 73], [71, 60], [77, 41], [45, 64], [99, 51], [46, 63], [70, 72], [72, 61], [81, 64], [82, 78], [78, 56], [84, 75], [79, 61], [53, 42], [73, 69], [84, 49], [58, 44], [50, 65], [63, 65], [89, 42], [61, 49], [75, 75], [65, 78], [49, 75], [79, 65], [90, 75], [62, 48], [45, 40], [60, 58], [43, 56], [49, 45], [64, 67], [50, 42], [66, 87], [69, 69], [75, 62], [91, 60], [80, 67], [48, 59], [70, 67], [51, 57], [57, 78], [52, 50], [56, 53], [62, 73], [59, 64], [83, 63], [47, 45], [64, 53], [37, 80], [52, 88], [58, 55], [55, 61], [61, 74], [85, 61], [33, 47], [64, 43], [86, 50], [49, 76], [63, 84], [91, 69], [67, 76], [77, 42], [48, 61], [76, 54], [69, 78], [66, 64], [56, 77], [50, 63], [81, 59], [71, 72], [45, 76], [52, 57], [46, 51], [62, 55], [53, 60], [86, 70], [51, 36], [57, 57], [88, 57], [58, 62], [32, 37], [61, 67], [62, 83], [72, 69], [73, 89], [60, 56], [49, 69], [72, 71], [35, 54], [64, 70], [72, 43], [64, 81], [65, 69], [87, 46], [44, 49], [68, 54], [64, 54], [72, 49], [45, 52], [66, 91], [49, 49], [37, 30], [44, 79], [50, 54], [81, 60], [71, 65], [68, 69], [57, 88], [95, 79], [46, 58], [51, 45], [75, 24], [47, 51], [84, 78], [58, 57], [31, 78], [59, 52], [83, 51], [60, 55], [84, 52], [50, 68], [55, 41], [79, 92], [90, 59], [72, 82], [53, 80], [60, 45], [49, 80], [78, 72], [76, 72], [69, 59], [45, 45], [67, 64], [64, 78], [70, 63], [44, 70], [50, 49], [42, 82], [37, 93], [71, 62], [69, 90], [75, 59], [73, 31], [65, 106], [76, 60], [74, 28], [46, 61], [71, 84], [68, 106], [63, 59], [52, 53], [85, 65], [96, 43], [68, 40], [53, 65], [84, 51], [58, 42], [55, 38], [92, 51], [66, 58], [88, 83], [81, 41], [103, 46], [63, 41], [61, 41], [76, 31], [72, 63], [96, 44], [69, 57], [73, 62], [76, 93], [41, 69], [74, 61], [89, 67], [69, 67], [66, 71], [80, 69], [60, 66], [48, 30], [70, 65], [71, 77], [68, 81], [57, 76], [58, 66], [45, 81], [84, 92], [62, 68], [60, 76], [57, 54], [54, 62], [36, 36], [55, 63], [61, 72], [24, 70], [66, 53], [54, 80], [52, 64], [67, 40], [79, 64], [66, 47], [72, 38], [43, 51], [80, 38], [29, 58], [49, 62], [80, 60], [50, 61], [47, 71], [77, 51], [57, 85], [58, 77], [80, 82], [35, 69], [46, 49], [62, 79], [51, 38], [81, 74], [64, 59], [55, 52], [67, 67], [59, 49], [62, 53], [62, 51], [40, 39], [51, 87], [52, 79], [50, 75], [61, 59], [77, 65], [74, 69], [75, 81], [72, 45], [17, 61], [76, 83], [55, 71], [55, 67], [69, 53], [66, 89], [49, 55], [39, 60], [70, 58], [68, 62], [68, 71], [63, 69], [93, 73], [59, 80], [57, 66], [57, 64], [47, 61], [78, 53], [85, 70], [50, 64], [79, 48], [33, 63], [57, 42], [38, 68], [73, 64], [91, 53], [63, 68], [69, 44], [51, 66], [75, 63], [79, 68], [68, 63], [74, 86], [72, 58], [49, 40], [73, 59], [70, 61], [39, 67], [50, 47], [47, 85], [71, 56], [66, 74], [56, 67], [96, 64], [60, 53], [68, 84], [81, 68], [82, 74], [45, 86], [78, 60], [52, 55], [85, 79], [79, 57], [62, 67], [33, 48], [65, 55], [82, 100], [63, 77], [85, 48], [75, 79], [48, 51], [86, 63], [77, 61], [41, 58], [79, 77], [85, 26], [77, 77], [72, 33], [62, 52], [43, 60], [73, 60], [41, 41], [55, 69], [74, 59], [48, 58], [71, 49], [53, 59], [75, 50], [49, 59], [56, 74], [80, 71], [71, 79], [68, 83], [58, 64], [52, 62], [56, 57], [70, 89], [59, 68], [60, 78], [57, 52], [47, 41], [86, 92], [58, 51], [97, 84], [37, 73], [61, 70], [33, 35], [72, 66], [36, 74], [60, 61], [49, 64], [50, 78], [63, 80], [40, 72], [54, 72], [99, 80], [65, 64], [78, 66], [85, 13], [41, 76], [55, 68], [81, 37], [71, 46], [49, 60], [43, 66], [48, 68], [81, 63], [71, 68], [36, 69], [39, 31], [70, 80], [57, 61], [81, 72], [58, 58], [64, 72], [59, 51], [63, 79], [61, 57], [88, 36], [75, 83], [36, 61], [69, 41], [64, 85], [87, 42], [68, 50], [74, 45], [48, 40], [65, 63], [75, 32], [49, 53], [39, 62], [80, 53], [55, 75], [74, 55], [71, 61], [68, 65], [83, 70], [46, 62], [70, 75], [57, 70], [78, 59], [52, 42], [35, 82], [53, 43], [78, 67], [47, 55], [41, 45], [61, 50], [59, 46], [86, 58], [105, 48], [67, 62], [63, 44], [53, 54], [68, 57], [42, 52], [55, 90], [72, 60], [53, 70], [45, 41], [43, 57], [63, 58], [64, 66], [80, 44], [70, 51], [44, 66], [50, 45], [74, 62], [59, 42], [71, 58], [68, 72], [69, 70], [66, 72], [82, 50], [36, 80], [73, 73], [56, 65], [46, 65], [47, 77], [83, 55], [68, 86], [57, 79], [58, 71], [84, 81], [79, 59], [53, 52], [59, 65], [57, 49], [54, 59], [58, 54], [65, 49], [48, 87], [26, 95], [33, 40], [90, 43], [65, 77], [78, 87], [77, 75], [92, 37], [53, 79], [69, 37], [43, 62], [63, 51], [41, 73], [55, 73], [67, 83], [82, 41], [56, 76], [50, 62], [46, 72], [71, 73], [58, 78], [52, 56], [78, 62], [62, 72], [59, 70], [60, 72], [48, 78], [68, 66], [62, 82], [67, 71], [57, 56], [72, 68], [65, 44], [87, 49], [68, 47], [66, 43], [72, 42], [62, 61], [54, 78], [67, 50], [64, 80], [65, 70], [78, 64], [76, 80], [68, 53], [76, 65], [77, 68], [38, 58], [45, 53], [44, 78], [47, 67], [38, 71], [70, 86], [57, 67], [72, 101], [81, 61], [88, 63], [49, 101], [79, 55], [72, 75], [73, 67], [86, 79], [60, 54], [65, 37], [64, 71], [74, 65], [78, 61], [90, 66], [76, 79], [68, 60], [73, 54], [80, 55], [74, 53], [81, 54], [71, 63], [68, 67], [56, 64], [64, 74], [70, 73], [96, 96], [57, 68], [78, 57], [35, 84], [56, 47], [59, 74], [83, 57], [69, 65], [65, 62], [66, 69], [26, 82], [72, 88], [53, 90], [54, 88], [65, 80], [78, 82], [29, 74], [76, 70], [33, 53], [62, 49], [61, 87], [69, 58], [71, 66], [64, 68], [97, 42], [74, 60], [66, 70], [56, 71], [46, 71], [70, 64], [77, 59], [58, 69], [38, 53], [55, 59], [56, 54], [46, 41], [53, 67], [59, 67], [33, 52], [81, 82], [73, 77], [77, 56], [63, 73], [55, 60], [61, 73], [75, 67], [73, 87], [50, 83], [77, 73], [75, 89], [60, 24], [50, 34], [48, 62], [95, 48], [66, 65], [76, 49], [50, 60], [55, 97], [77, 52], [95, 65], [80, 81], [52, 58], [26, 53], [55, 77], [46, 48], [62, 78], [60, 74], [75, 98], [36, 78], [87, 66], [34, 74], [58, 63], [55, 53], [62, 80], [59, 62], [60, 42], [90, 48], [54, 42], [60, 57], [52, 78], [61, 60], [68, 41], [79, 30], [72, 44], [66, 77], [60, 23], [67, 52], [65, 68], [70, 35], [68, 55], [74, 46], [55, 64], [88, 68], [44, 72], [91, 64], [67, 58], [73, 51], [81, 51], [71, 64], [68, 70], [58, 87], [45, 68], [60, 65], [81, 76], [82, 82], [37, 65], [73, 71], [56, 42], [55, 50], [79, 49], [53, 46], [83, 50], [72, 77], [65, 59], [55, 40], [59, 45], [72, 83], [51, 67], [67, 61], [41, 50], [63, 35], [55, 70], [42, 73], [72, 57], [69, 63], [49, 41], [78, 115], [76, 39], [95, 63], [51, 80], [75, 58], [56, 66], [59, 47], [76, 61], [27, 54], [52, 54], [85, 64], [53, 55], [83, 59], [23, 34], [52, 92], [65, 60], [66, 59], [31, 72], [79, 66], [53, 66], [95, 47], [69, 56], [73, 61], [74, 58], [55, 76], [71, 54], [36, 64], [69, 66], [66, 68], [58, 89], [82, 42], [70, 70], [71, 76], [92, 62], [52, 61], [53, 48], [98, 56], [81, 67], [57, 53], [82, 94], [78, 40], [48, 74], [65, 53], [37, 55], [70, 66], [75, 69], [33, 57], [52, 65], [63, 81], [67, 94], [72, 39], [54, 75], [64, 64], [67, 49], [39, 40], [63, 63], [70, 46], [92, 95], [89, 75], [40, 84], [45, 56], [93, 85], [50, 58], [47, 70], [69, 85], [58, 74], [93, 79], [62, 76], [60, 68], [42, 81], [54, 54], [78, 51], [32, 56], [90, 62], [60, 59], [31, 62], [48, 88], [61, 58], [77, 64], [74, 66], [64, 84], [76, 76], [38, 62], [69, 52], [73, 49], [73, 78], [74, 54], [53, 24], [68, 64], [45, 66], [93, 72], [68, 90], [70, 74], [103, 56], [57, 71], [84, 73], [74, 41], [62, 89], [59, 73], [89, 70], [64, 60], [60, 50], [34, 61], [58, 46], [79, 89], [35, 32], [54, 47], [66, 62], [53, 93], [51, 69], [80, 21], [61, 45], [76, 75], [51, 55], [50, 56], [48, 46], [72, 59], [69, 61], [67, 69], [64, 65], [74, 49], [69, 71], [80, 65], [83, 76], [46, 64], [77, 62], [60, 90], [58, 70], [94, 73], [80, 103]]

    a=distro(center,num_points)
    b,c=sfcurve(a,size)
    plt.figure(4)
    d=separate(b,num_proc)
    e=nndsmart(c,d,nnd)
    average=topo(eorder(num_proc),e)
    plt.show()
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
