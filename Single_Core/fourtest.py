from torinntreedist import *
def fourtest():
        p=[]
        q=[]
        r=[]
        s=[]
        t=[]
        u=[]
        for j in [2,4,8,16,32,64,128,256,512]:
                for i in ['h','g','z','r']:
                        p.append(NNA('every',j,j**2,i,j,1.1,'torus',i,j))
                        q.append(NNA('every',j,j**2,i,j,1.1,'grid',i,j))
                        r.append(NNA('every',j,j**2,i,j,1.1,'linear',i,j))
                        s.append(NNA('every',j,j**2,i,j,1.1,'cyclic',i,j))
                        t.append(NNA('every',j,j**2,i,j,1.1,'hypercube',i,j))
                        u.append(NNA('every',j,j**2,i,j,1.1,'quadtree',i,j))
        return p,q,r,s,t,u

