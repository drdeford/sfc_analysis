import math
from zorder import z
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
                
                
        else: 
            if x=='1' and y=='1':
                d=order
                
                
            if x=='1' and y=='0':
               d=order+1
              
               
            if x=='0' and y=='0':
                d=order+2
                
                
            if x=='0' and y=='1':
                d=order+3
                
                
    else:
        
        if orientation==0:
            if x[0]=='0' and y[0]=='0':
                orienation=orientation
                d=order
                d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)
                
            if x[0]=='0' and y[0]=='1':
                orientation=(orientation+1)%2
                d=order+((size/2)**2)
                d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)
                
            if x[0]=='1' and y[0]=='1':
                orientation=(orientation+1)%2                           
                d=order+(2*(size/2)**2)
                d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)
                
               
            if x[0]=='1' and y[0]=='0':
                orientation=orientation
                d=order+(3*(size/2)**2)
                d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)
                    
                    

        else: 
            if x[0]=='1' and y[0]=='1':
                orientation=(orientation+1)%2
                d=order
                d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)   
                
                
            if x[0]=='1' and y[0]=='0':
               d=order+((size/2)**2)
               d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)
               
            if x[0]=='0' and y[0]=='0':
                d=order+(2*(size/2)**2)
                d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)
                
            if x[0]=='0' and y[0]=='1':
                orientation=(orientation+1)%2
                d=order+(3*(size/2)**2)
                d=g(size/2,int(x[1:],2),int(y[1:],2),d,orientation)

    d=int(d)
    return d



    
                    
            
        
    
