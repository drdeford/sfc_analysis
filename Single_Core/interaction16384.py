from torinntreedist import *
from l16384 import *
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
topo_list=[torus16384,grid16384,linear,cyclic,hypercube16384,quadtree16384]
embed_list=[embedh,embedg,embedz,embedr]
def interaction16384(a,center,num_proc,size,curve,embed_order,topology):
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
    length=center/64
    for i in range(len(e)):
        e[i].append(i)
    for i in e:
        i.append(set())
    for j in range(len(d)):
        x_val=math.floor(d[j][0]/length)
        y_val=math.floor(d[j][1]/length)
        quad_num= 128*y_val+x_val
        e[d[j][2]][3].add(quad_num)
    q=[]
    for i in range(16384):
        q.append([])
    for k in range(len(e)):
        for l in e[k][3]:
            q[l].append([e[k][0],e[k][1],e[k][2]])
##            for m in range(16384):
  ##              if l==m:
    ##                q[m].append([e[k][0],e[k][1]])
    
    ns=0
    parsum=0
    for i in range(len(q)):
        if q[i]==[]:
            q[i]=[[0,0,0]]
    ##return q
    w=allpoints(128,16384)
    tree=spatial.KDTree(w)
    z=[]
    for i in range(16384):
        z.append([])
    for n in range(16384):
        r,t=tree.query([w[n]],8,0,2,1.1)
        x,s=tree.query([w[n]],36,0,2,3.1)
        t=t.tolist()
        t.append(16384)
        s=s.tolist()
        z[n]=list(set(s[0])-set(t[0]))
    ##return z
    parsum,ns,average=topo(q,z,num_proc)
    return parsum,ns,average





