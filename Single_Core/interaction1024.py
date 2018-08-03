from torinntreedist import *
from l1024 import *
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
topo_list=[torus1024,grid1024,linear,cyclic,hypercube1024,quadtree1024]
embed_list=[embedh,embedg,embedz,embedr]
def interaction1024(a,center,num_proc,size,curve,embed_order,topology):
    topo=topologies[topology]
    topo=topo_list[topo]
##    distro=distributions[distribution]
##    distro=dist_list[distro]
    sfcurve=sfcurves[curve]
    sfcurve=curve_list[sfcurve]
    eorder=embed_orders[embed_order]
    eorder=embed_list[eorder]
##    a=distro(center,num_points)
    b,c=sfcurve(a,size)
    d=separate(b,num_proc)
    e=eorder(num_proc)
    length=center/16
    for i in range(len(e)):
        e[i].append(i)
    for i in e:
        i.append(set())
    for j in range(len(d)):
        x_val=math.floor(d[j][0]/length)
        y_val=math.floor(d[j][1]/length)
        quad_num= 32*y_val+x_val
        e[d[j][2]][3].add(quad_num)
    q=[]
    for i in range(1024):
        q.append([])
    for k in range(len(e)):
        for l in e[k][3]:
            q[l].append([e[k][0],e[k][1],e[k][2]])
##            for m in range(1024):
 ##               if l==m:
   ##                 q[m].append([e[k][0],e[k][1]])
    
    ns=0
    parsum=0
    for i in range(len(q)):
        if q[i]==[]:
            q[i]=[[0,0,0]]
    ##return q
    w=allpoints(32,1024)
    tree=spatial.KDTree(w)
    z=[]
    for i in range(1024):
        z.append([])
    for n in range(1024):
        r,t=tree.query([w[n]],8,0,2,1.1)
        x,s=tree.query([w[n]],36,0,2,3.1)
        t=t.tolist()
        t.append(1024)
        s=s.tolist()
        z[n]=list(set(s[0])-set(t[0]))
    ##return z
    parsum,ns,average=topo(q,z,num_proc)
    return parsum,ns,average


