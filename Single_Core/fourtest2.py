from torinntreedist import *
def fourtest2():
        p=[]
        q=[]
        r=[]
        s=[]
        t=[]
        u=[]
        for j in [2,4,8,16,32,64,128,256,512]:
                for i in ['h','g','z','r']:
                        p.append(NNA('every',j,j**2,i,j,2,'torus',i,j))
                        q.append(NNA('every',j,j**2,i,j,2,'grid',i,j))
                        r.append(NNA('every',j,j**2,i,j,2,'linear',i,j))
                        s.append(NNA('every',j,j**2,i,j,2,'cyclic',i,j))
                        t.append(NNA('every',j,j**2,i,j,2,'hypercube',i,j))
                        u.append(NNA('every',j,j**2,i,j,2,'quadtree',i,j))
        return p,q,r,s,t,u

