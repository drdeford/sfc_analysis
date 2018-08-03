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
##import matplotlib.pyplot as plt
##import math
##import itertools
def bipoints(center,n):
    data=np.random.multivariate_normal([center,center],[[.05*(center**2),0],[0,.05*(center**2)]],n)
    x=[]
    y=[]
    for i in range(n):
        x.append(int(data[i][0]))
        y.append(int(data[i][1]))
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
##import matplotlib.pyplot as plt
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
##import matplotlib.pyplot as plt
##import math
##import itertools
def epoints(scale,n):
    x=np.random.exponential(scale,n)
    y=np.random.exponential(scale,n)
    
    for i in range(len(x)):
        if x[i]>2*scale:
            x[i]=int(np.random.randint(0,scale))
        if y[i]>2*scale:
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
##import matplotlib.pyplot as plt
##import math
##import itertools
def paretopoints(scale,n):
    x=np.random.pareto(1,n)*scale
    y=np.random.pareto(1,n)*scale    
    for i in range(len(x)):
        if x[i]>2*scale:
            x[i]=int(np.random.randint(0,scale))
        if y[i]>2*scale:
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
##import matplotlib.pyplot as plt
##import math
##import itertools
def powerpoints(scale,n):
    x=np.random.power(1,n)*scale
    y=np.random.power(1,n)*scale    
    for i in range(len(x)):
        if x[i]>2*scale:
            x[i]=int(np.random.randint(0,scale))
        if y[i]>2*scale:
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

#SELECT Poisson POINTS
##import numpy as np
##import scipy as sp
##import matplotlib.pyplot as plt
##import math
##import itertools
def poissonpoints(scale,n):
    x=np.random.poisson(scale,n)
    y=np.random.poisson(scale,n)   
    for i in range(len(x)):
        if x[i]>2*scale:
            x[i]=int(np.random.randint(0,scale))
        if y[i]>2*scale:
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
#import matplotlib.pyplot as plt
def rpoint(point_list,size):
    for i in range(len(point_list)):
        point_list[i].append(int(r(size,point_list[i][0],point_list[i][1])))
   # plt.xlim((0,size))
   # plt.ylim((0,size))
    plt.figure(1)
   # plt.subplot(2,2,1)
 #   for j in range(len(point_list)):
  #      plt.text(point_list[j][0],point_list[j][1],str(point_list[j][2]),fontsize=6)
    point_list=sorted(point_list,key=itemgetter(-1))
    for k in range(len(point_list)-1):
        plt.plot([point_list[k][0],point_list[k+1][0]],[point_list[k][1],point_list[k+1][1]])
    plt.show()
    #These next two lines return only an ordered list of points
    for m in range(len(point_list)):
        point_list[m]=point_list[m][:2]
    return point_list
#Z SCAN POINTS
#from curves import z
#import math
from operator import itemgetter, attrgetter
import matplotlib.pyplot as plt
def zpoint(point_list,size):
    for i in range(len(point_list)):
        point_list[i].append(z(size,point_list[i][0],point_list[i][1]))
  #  plt.xlim((0,int(math.sqrt(len(point_list)))))
  #  plt.ylim((0,int(math.sqrt(len(point_list)))))
    plt.figure(2)
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
    return point_list  
#G SCAN POINTS
#from curves import g
#import math
from operator import itemgetter, attrgetter
import matplotlib.pyplot as plt
def gpoint(point_list,size):
    for i in range(len(point_list)):
        point_list[i].append(g(size,point_list[i][0],point_list[i][1],0,0))
 #   plt.xlim((0,int(math.sqrt(len(point_list)))))
 #   plt.ylim((0,int(math.sqrt(len(point_list)))))
    plt.figure(3)
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
    return point_list
    
# H SCAN POINTS
#from curves import h
#import math
from operator import itemgetter, attrgetter
import matplotlib.pyplot as plt
def hpoint(point_list,size):
    for i in range(len(point_list)):
        point_list[i].append(h(size,point_list[i][0],point_list[i][1]))
 #   plt.xlim((0,int(math.sqrt(len(point_list)))))
  #  plt.ylim((0,int(math.sqrt(len(point_list)))))
    plt.figure(4)
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
    return point_list


######################SPLIT POINTS ONTO PROCESSORS #########
#POINT SEPARATOR
#import math
def separate(point_list,num_pro):
  #  while len(point_list)/num_pro != math.floor(len(point_list)/num_pro):
    ppp=math.floor(len(point_list)/(num_pro)) 
    for i in range(num_pro):
        for j in range(ppp):
            point_list[ppp*i+j].append(i)
    extras=len(point_list)-((num_pro)*ppp)
    for k in range(extras):
        point_list[-(k+1)].append(num_pro-1)        
    return point_list

######## FIND NN ##########
####SELECT NEIGHBORHOODS MORE EFFICIENTLY######

def nndsmart(point_list,dist):
    l=len(point_list)
    #qdist=(2*dist+1)**@
    #tree=sp.spatial.KDTree(point_list)
    #for i in range(l):
    #    for k in tree.query([point_list[i][0],point_list[i][1]],qdist,0,1,dist)[1]:
    #        point_list[i].append(point_list[k][2])
    for j in range(l):
        for k in range(j+1,l):
           # if point_list[k][0] in range(point_list[j][0]-dist,point_list[j][0]+dist+1):
            if abs(point_list[j][0]-point_list[k][0])<=dist and abs(point_list[j][1]-point_list[k][1])<=dist:
                point_list[j].append(point_list[k][2])
                point_list[k].append(point_list[j][2])
    #for m in range(l):
    #    point_list[m]=point_list[m][2:]
    return point_list
    
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
def nnd(q,point_list):
    NND_list=[]
    for i in range(len(q)):
        NND_list.append([i,point_list[i][-1]])
    for j in range(len(q)):
        for k in q[j][1:]:
            NND_list[j].append(point_list[k][-1])
            
         #   for l in range(len(q)):
          #      if k==point_list[l][-1]
           # p[j].append(point_list[l][-1]
        
    
    
    return NND_list

################PROCESSOR TORII EMBEDDING######
#PROCESSOR EMBEDDING
#R order
def embedr(size):
    e=[]
    for i in range(size):
        for j in range(size):
            e.append([i,j])
    proc_list=rpoint(e,size)
    return proc_list
#Z order
def embedz(size):
    e=[]
    for i in range(size):
        for j in range(size):
            e.append([i,j])
    proc_list=zpoint(e,size)
    return proc_list
#G order
def embedg(size):
    e=[]
    for i in range(size):
        for j in range(size):
            e.append([i,j])
    proc_list=gpoint(e,size)
    return proc_list

#H order
def embedh(size):
    e=[]
    for i in range(size):
        for j in range(size):
            e.append([i,j])
    proc_list=hpoint(e,size)
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
'torus':1,
'grid':2,
'linear':3,
'cyclic':4
}
embed_orders={
'h':0,
'g':1,
'z':2,
'r':3
}    
dist_list=[bipoints,upoints,paretopoints,powerpoints,poissonpoints,epoints,allpoints]
curve_list=[hpoint,gpoint,zpoint,rpoint]
topo_list=[torus,grid,linear,cyclic]
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
    average=topo(eorder(num_proc),nndsmart(separate(sfcurve(distro(center,num_points),size),num_proc),nnd))
    return average
    
