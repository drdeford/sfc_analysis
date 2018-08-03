import math
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
