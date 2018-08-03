from torinntreedist import *
from l16 import *
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
topo_list=[torus16,grid16,linear,cyclic,hypercube16,quadtree16]
embed_list=[embedh,embedg,embedz,embedr]
def interaction16(a,center,num_proc,size,curve,embed_order,topology):
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
    
    for i in range(len(e)):
        e[i].append(i)
    for i in e:
        i.append(set())
    for j in range(len(d)):
        if 0<=d[j][0]<=center/2 and 0<=d[j][1]<=center/2:
            e[d[j][2]][3].add(0)
        elif center/2<=d[j][0]<=center and 0<=d[j][1]<=center/2:
            e[d[j][2]][3].add(1)
        elif center<=d[j][0]<=3*center/2 and 0<=d[j][1]<=center/2:
            e[d[j][2]][3].add(2)
        elif 3*center/2<=d[j][0]<=2*center and 0<=d[j][1]<=center/2:
            e[d[j][2]][3].add(3)
        elif 0<=d[j][0]<=center/2 and center/2<=d[j][1]<=center:
            e[d[j][2]][3].add(4)
        elif center/2<=d[j][0]<=center and center/2<=d[j][1]<=center:
            e[d[j][2]][3].add(5)
        elif center<=d[j][0]<=3*center/2 and center/2<=d[j][1]<=center:
            e[d[j][2]][3].add(6)
        elif 3*center/2<=d[j][0]<=2*center and center/2<=d[j][1]<=center:
            e[d[j][2]][3].add(7)
        elif 0<=d[j][0]<=center/2 and center<=d[j][1]<=3*center/2:
            e[d[j][2]][3].add(8)
        elif center/2<=d[j][0]<=center and center<=d[j][1]<=3*center/2:
            e[d[j][2]][3].add(9)
        elif center<=d[j][0]<=3*center/2 and center<=d[j][1]<=3*center/2:
            e[d[j][2]][3].add(10)
        elif 3*center/2<=d[j][0]<=2*center and center<=d[j][1]<=3*center/2:
            e[d[j][2]][3].add(11)
        elif 0<=d[j][0]<=center/2 and 3*center/2<=d[j][1]<=2*center:
            e[d[j][2]][3].add(12)
        elif center/2<=d[j][0]<=center and 3*center/2<=d[j][1]<=2*center:
            e[d[j][2]][3].add(13)
        elif center<=d[j][0]<=3*center/2 and 3*center/2<=d[j][1]<=2*center:
            e[d[j][2]][3].add(14)
        elif 3*center/2<=d[j][0]<=2*center and 3*center/2<=d[j][1]<=2*center:
            e[d[j][2]][3].add(15)
            
    q0=[]
    q1=[]
    q2=[]
    q3=[]
    q4=[]
    q5=[]
    q6=[]
    q7=[]
    q8=[]
    q9=[]
    q10=[]
    q11=[]
    q12=[]
    q13=[]
    q14=[]
    q15=[]

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
            elif l==4:
                q4.append([e[k][0],e[k][1],e[k][2]])
            elif l==5:
                q5.append([e[k][0],e[k][1],e[k][2]])
            elif l==6:
                q6.append([e[k][0],e[k][1],e[k][2]])
            elif l==7:
                q7.append([e[k][0],e[k][1],e[k][2]])
            elif l==8:
                q8.append([e[k][0],e[k][1],e[k][2]])
            elif l==9:
                q9.append([e[k][0],e[k][1],e[k][2]])
            elif l==10:
                q10.append([e[k][0],e[k][1],e[k][2]])
            elif l==11:
                q11.append([e[k][0],e[k][1],e[k][2]])
            elif l==12:
                q12.append([e[k][0],e[k][1],e[k][2]])
            elif l==13:
                q13.append([e[k][0],e[k][1],e[k][2]])
            elif l==14:
                q14.append([e[k][0],e[k][1],e[k][2]])
            elif l==15:
                q15.append([e[k][0],e[k][1],e[k][2]])
    
    for k in range(len(e)):
        e[k].pop()
    q=[]
    q.append(q0)
    q.append(q1)
    q.append(q2)
    q.append(q3)
    q.append(q4)
    q.append(q5)
    q.append(q6)
    q.append(q7)
    q.append(q8)
    q.append(q9)
    q.append(q10)
    q.append(q11)
    q.append(q12)
    q.append(q13)
    q.append(q14)
    q.append(q15)
    
    parsum,ns,average = topo(q,num_proc)
    return parsum,ns,average
