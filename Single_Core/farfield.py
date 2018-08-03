from torinntreedist import *
from interaction16 import *
from interaction32 import *
from interaction256 import *
from interaction1024 import *
from interaction4096 import *
from interaction16384 import *
#from interaction65536 import *
#from interaction262144 import *

from lri import *
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
def farfield(distribution,center,num_points,curve,size,nnd,topology,embed_order,num_proc):
##    topo=topologies[topology]
##    topo=topo_list[topo]
    distro=distributions[distribution]
    distro=dist_list[distro]
    sfcurve=sfcurves[curve]
    sfcurve=curve_list[sfcurve]
    eorder=embed_orders[embed_order]
    eorder=embed_list[eorder]
    a=distro(center,num_points)
##    a2=list(a)
##    a3=list(a)
##    
##    b,c=sfcurve(a,size)
##    b2,c2=sfcurve(a2,size)
##    b3,c3=sfcurve(a3,size)
##    d2=separate(b2,num_proc)
##    d3=separate(b3,num_proc)
##    d1=separate(b,num_proc)
##    e1=eorder(num_proc)
##    e2=eorder(num_proc)
##    e3=eorder(num_proc)
##    
    sum1,ns1,avg1 =lri(a,center,num_proc,size,curve,embed_order)
    sum2,ns2,avg2 =interaction16(a,center,num_proc,size,curve,embed_order,topology)
    sum3,ns3,avg3 =interaction32(a,center,num_proc,size,curve,embed_order,topology)
    sum4,ns4,avg4 =interaction256(a,center,num_proc,size,curve,embed_order,topology)
    sum5,ns5,avg5 =interaction1024(a,center,num_proc,size,curve,embed_order,topology)
    sum6,ns6,avg6 =interaction4096(a,center,num_proc,size,curve,embed_order,topology)    
    sum7,ns7,avg7 =interaction16384(a,center,num_proc,size,curve,embed_order,topology)
    #sum8,ns8,avg8 =interaction65536(a,center,num_proc,size,curve,embed_order,torus)
    #sum9,ns9,avg9 =interaction262144(a,center,num_proc,size,curve,embed_order,torus)
    totalsum=sum1+sum2+sum3+sum4+sum5+sum6+sum7#+sum8+sum9
    totalns=ns1+ns2+ns3+ns4+ns5+ns6+ns7#+ns8+ns9
    totalavg=totalsum/totalns
    return totalavg#,avg1,avg2,avg3,avg4,avg5,avg6,avg7,totalavg,ns1,ns2,ns3,ns4,ns5,ns6,ns7
