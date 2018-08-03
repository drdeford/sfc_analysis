import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math
import itertools

#ROW SCAN ORDER
def r(size,x,y):
    order=x*size+y
    return order
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
#G SCAN ORDER
#import math
#from curves import z
def g(size,x,y,order,orientation):
    x=bin(x)
    y=bin(y)
    x=x[2:]
    y=y[2:]
    d=0
    for j in range(int(math.log(size,2))):
        if len(x)<(math.log(size,2)):
            x='0'+x
        if len(y)<(math.log(size,2)):
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
    for j in range(int(math.log(size,2))):
        if len(x)<(math.log(size,2)):
            x='0'+x
        if len(y)<(math.log(size,2)):
            y='0'+y
    
    for i in range(int(math.log(size,2))):
        order=int(bin(order)[2:]+'00',2)
        x_coord=int(x[i])
        y_coord=int(y[i])
        quad_order,orientation=directions[orientation][(x_coord,y_coord)]
        order=order+quad_order
    return order
    
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

#SELECT BIVARIATE POINTS
##import numpy as np
##import scipy as sp
##import matplotlib.pyplot as plt
##import math
##import itertools
def bipoints(center,variance,n):
    data=np.random.multivariate_normal([center,center],[[variance,0],[0,variance]],n)
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
    b=[]
    c=[]
    d=[]
    e=[]
    b.extend(point_list)
    c.extend(point_list)
    d.extend(point_list)
    e.extend(point_list)
    return b,c,d,e

#SELECT UNIFORM POINTS
##import numpy as np
##import scipy as sp
##import matplotlib.pyplot as plt
##import math
##import itertools
def upoints(low,high,n):
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
    b=[]
    c=[]
    d=[]
    e=[]
    b.extend(point_list)
    c.extend(point_list)
    d.extend(point_list)
    e.extend(point_list)
    return b,c,d,e
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
    b=[]
    c=[]
    d=[]
    e=[]
    b.extend(point_list)
    c.extend(point_list)
    d.extend(point_list)
    e.extend(point_list)
    return b,c,d,e

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
    b=[]
    c=[]
    d=[]
    e=[]
    b.extend(point_list)
    c.extend(point_list)
    d.extend(point_list)
    e.extend(point_list)
    return b,c,d,e

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
    b=[]
    c=[]
    d=[]
    e=[]
    b.extend(point_list)
    c.extend(point_list)
    d.extend(point_list)
    e.extend(point_list)
    return b,c,d,e

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
    b=[]
    c=[]
    d=[]
    e=[]
    b.extend(point_list)
    c.extend(point_list)
    d.extend(point_list)
    e.extend(point_list)
    return b,c,d,e
#POINTS IN ALL CURVES
def testcurves(b,c,d,e,size):
    
    rpoint(b,size)
    zpoint(c,size)
    gpoint(d,size)
    hpoint(e,size)
    plt.show()
    #return b,c,d,e
    

    #Select Neighborhoods 8

#import math
def nn8(point_list):
    p=[]
    for j in range(len(point_list)):
        p.append([j])
    q=[]
    for k in range(len(point_list)):
        q.append([k])
    for i in range(len(point_list)):
        x=point_list[i][0]
        y=point_list[i][1]
        a=[[x+1,y],[x+1,y+1],[x+1,y-1],[x,y+1],[x,y-1],[x-1,y],[x-1,y+1],[x-1,y-1]]
        p[i].append(a)
    for l in range(len(point_list)):
        for m in p[l][1]:
            for n in range(len(point_list)):
                if m[0]==point_list[n][0] and m[1]==point_list[n][1]:
                    q[l].append(n)
    return q

#Select Neighborhoods 12

#import math
def nn12(point_list):
    p=[]
    for j in range(len(point_list)):
        p.append([j])
    q=[]
    for k in range(len(point_list)):
        q.append([k])
    for i in range(len(point_list)):
        x=point_list[i][0]
        y=point_list[i][1]
        a=[[x+1,y],[x+1,y+1],[x+1,y-1],[x,y+1],[x,y-1],[x-1,y],[x-1,y+1],[x-1,y-1],[x+2,y],[x,y+2],[x,y-2],[x-2,y]]
        p[i].append(a)
    for l in range(len(point_list)):
        for m in p[l][1]:
            for n in range(len(point_list)):
                if m[0]==point_list[n][0] and m[1]==point_list[n][1]:
                    q[l].append(n)
    return q


#Select Neighborhoods 20

#import math
def nn20(point_list):
    p=[]
    for j in range(len(point_list)):
        p.append([j])
    q=[]
    for k in range(len(point_list)):
        q.append([k])
    for i in range(len(point_list)):
        x=point_list[i][0]
        y=point_list[i][1]
        a=[[x+1,y],[x+1,y+1],[x+1,y-1],[x,y+1],[x,y-1],[x-1,y],[x-1,y+1],[x-1,y-1],[x+2,y],[x,y+2],[x,y-2],[x-2,y],[x+1,y+2],[x+1,y-2],[x-1,y+2],[x-1,y-2],[x+2,y+1],[x-2,y+1],[x+2,y-1],[x-2,y-1]]
        p[i].append(a)
    for l in range(len(point_list)):
        for m in p[l][1]:
            for n in range(len(point_list)):
                if m[0]==point_list[n][0] and m[1]==point_list[n][1]:
                    q[l].append(n)
    return q

#Select Neighborhoods 24

#import math
def nn24(point_list):
    p=[]
    for j in range(len(point_list)):
        p.append([j])
    q=[]
    for k in range(len(point_list)):
        q.append([k])
    for i in range(len(point_list)):
        x=point_list[i][0]
        y=point_list[i][1]
        a=[[x+1,y],[x+1,y+1],[x+1,y-1],[x,y+1],[x,y-1],[x-1,y],[x-1,y+1],[x-1,y-1],[x+2,y],[x,y+2],[x,y-2],[x-2,y],[x+1,y+2],[x+1,y-2],[x-1,y+2],[x-1,y-2],[x+2,y+1],[x-2,y+1],[x+2,y-1],[x-2,y-1],[x+2,y+2],[x+2,y-2],[x-2,y-2],[x-2,y+2]]
        p[i].append(a)
    for l in range(len(point_list)):
        for m in p[l][1]:
            for n in range(len(point_list)):
                if m[0]==point_list[n][0] and m[1]==point_list[n][1]:
                    q[l].append(n)
    return q

#Select Neighborhoods 4

#import math
def nn4(point_list):
    p=[]
    for j in range(len(point_list)):
        p.append([j])
    q=[]
    for k in range(len(point_list)):
        q.append([k])
    for i in range(len(point_list)):
        x=point_list[i][0]
        y=point_list[i][1]
        a=[[x+1,y],[x,y+1],[x,y-1],[x-1,y]]
        p[i].append(a)
    for l in range(len(point_list)):
        for m in p[l][1]:
            for n in range(len(point_list)):
                if m[0]==point_list[n][0] and m[1]==point_list[n][1]:
                    q[l].append(n)
    return q
# NEIGHBOR DISTANCES
def nnd(q,point_list):
    p=[]
    for i in range(len(q)):
        p.append([i,point_list[i][-1]])
    for j in range(len(q)):
        for k in q[j][1:]:
            p[j].append(point_list[k][-1])
            
         #   for l in range(len(q)):
          #      if k==point_list[l][-1]
           # p[j].append(point_list[l][-1]
        
    
    
    return p

#AVERAGE NND LINEAR

def anndl(p):
    ns=0
    parsum=0
    for i in range(len(p)):
        ns=ns+len(p[i][2:])
    for j in range(len(p)):
        for k in p[j][2:]:
            parsum=parsum+abs(p[j][1]-k)
    average=parsum/ns
    return average

  #AVERAGE NND cyclic

def anndlc(p):
    ns=0
    parsum=0
    for i in range(len(p)):
        ns=ns+len(p[i][2:])
    for j in range(len(p)):
        for k in p[j][2:]:
            if abs(p[j][1]-k)<(len(p)/2):
                parsum=parsum+abs(p[j][1]-k)
            else:
                parsum=parsum+abs(len(p)-abs(p[j][1]-k))
    average=parsum/ns
    return average
# R Average linear
def ravgl(point_list,size):
    a=rpoint(point_list,size)
    avgr=anndl(nnd(nn8(a),a))
    return avgr
    
# Z Average linear
def zavgl(point_list,size):
    a=zpoint(point_list,size)
    avgz=anndl(nnd(nn8(a),a))
    return avgz

# G Average linear
def gavgl(point_list,size):
    a=gpoint(point_list,size)
    avgg=anndl(nnd(nn8(a),a))
    return avgg

# H Average linear
def havgl(point_list,size):
    a=hpoint(point_list,size)
    avgh=anndl(nnd(nn8(a),a))
    return avgh


# R Average cyclic
def ravgc(point_list,size):
    a=rpoint(point_list,size)
    avgr=anndlc(nnd(nn8(a),a))
    return avgr
    
# Z Average cyclic
def zavgc(point_list,size):
    a=zpoint(point_list,size)
    avgz=anndlc(nnd(nn8(a),a))
    return avgz

# G Average cyclic
def gavgc(point_list,size):
    a=gpoint(point_list,size)
    avgg=anndlc(nnd(nn8(a),a))
    return avgg

# H Average cyclic
def havgc(point_list,size):
    a=hpoint(point_list,size)
    avgh=anndlc(nnd(nn8(a),a))
    return avgh

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


    
