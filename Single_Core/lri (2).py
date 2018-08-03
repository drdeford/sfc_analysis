from torinntreedist import *

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
topo_list=[ltorus,lgrid,llinear,lcyclic,lhypercube,lquadtree]
embed_list=[embedh,embedg,embedz,embedr]
def lri(distribution,center,num_points,curve,size,nnd,topology,embed_order,num_proc):
  #  average=topo_list[topologies][topology](embed_list[embed_orders][embedded_order](num_proc),nndsmart(separate(curve_list[sfcurves][curve](dist_list[distributions][distribution](center,num_points),size),num_proc),nnd))
    topo=topologies[topology]
    topo=topo_list[topo]
    distro=distributions[distribution]
    distro=dist_list[distro]
    sfcurve=sfcurves[curve]
    sfcurve=curve_list[sfcurve]
    eorder=embed_orders[embed_order]
    eorder=embed_list[eorder]
    a=distro(center,num_points)
    b,c=sfcurve(a,size)
    d=separate(b,num_proc)
    e=eorder(num_proc)
    #dim=size**2
    for i in range(len(e)):
        e[i].append(i)
    for i in e:
        i.append(set())
    for j in range(len(d)):
        if d[j][0]<=center and d[j][1]<=center:
            e[d[j][2]][3].add(0)
        elif d[j][0]<=center and d[j][1]>=center:
            e[d[j][2]][3].add(1)
        elif d[j][0]>=center and d[j][1]<=center:
            e[d[j][2]][3].add(2)
        elif d[j][0]>=center and d[j][1]>=center:
            e[d[j][2]][3].add(3)
    q0=[]
    q1=[]
    q2=[]
    q3=[]
    
    for k in range(len(e)):
        for l in e[k][3]:
            if l==0:
                q0.append([e[k][0],e[k][1],e[k][2]])
            elif l==1:
                q1.append([e[k][0],e[k][1],e[k][2]])
            elif l==2:
                q2.append([e[k][0],e[k][1],e[k][2]])
            elif l==3:
                q3.append([e[k][0],e[k][1],e[k][2]])               
    for k in range(len(e)):
        e[k].pop()
       
    log0=math.ceil(math.log(len(q0),2))
    log1=math.ceil(math.log(len(q1),2))
    log2=math.ceil(math.log(len(q2),2))
    log3=math.ceil(math.log(len(q3),2))
    for o in range(len(q0)):
        for n in range(log0):
            if o%(2**(n+1))==0 and o<len(q0)-(2**n):
                q0[o].append(q0[o+(2**n)][2])
    for o in range(len(q1)):
        for n in range(log1):
            if o%(2**(n+1))==0 and o<len(q1)-(2**n):
                q1[o].append(q1[o+(2**n)][2])
    for o in range(len(q2)):
        for n in range(log2):
            if o%(2**(n+1))==0 and o<len(q2)-(2**n):
                q2[o].append(q2[o+(2**n)][2])
    for o in range(len(q3)):
        for n in range(log3):
            if o%(2**(n+1))==0 and o<len(q3)-(2**n):
                q3[o].append(q3[o+(2**n)][2])
    parns=0
    paravg=0
    for quad in [q0,q1,q2,q3]:
        a,b=topo(e,quad,size)
        paravg=paravg+a
        parns=parns+b

    average=paravg/parns
    return average

   
 #   average=parsum/ns
    #return d,e,q0,q1,q2,q3,parsum,ns,average
   # return average
            
        
            

    
