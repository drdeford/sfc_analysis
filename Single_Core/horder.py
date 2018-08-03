import math
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
    
