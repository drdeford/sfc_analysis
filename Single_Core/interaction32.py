from torinntreedist import *
from l32 import *
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
topo_list=[torus32,grid32,linear,cyclic,hypercube32,quadtree32]
embed_list=[embedh,embedg,embedz,embedr]
def interaction32(a,center,num_proc,size,curve,embed_order,topology):
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
        if 0<=d[j][0]<=center/4 and 0<=d[j][1]<=center/4:
            e[d[j][2]][3].add(0)
        elif center/4<=d[j][0]<=center/2 and 0<=d[j][1]<=center/4:
            e[d[j][2]][3].add(1)
        elif center/2<=d[j][0]<=3*center/4 and 0<=d[j][1]<=center/4:
            e[d[j][2]][3].add(2)
        elif 3*center/4<=d[j][0]<=center and 0<=d[j][1]<=center/4:
            e[d[j][2]][3].add(3)
        elif center<=d[j][0]<=5*center/4 and 0<=d[j][1]<=center/4:
            e[d[j][2]][3].add(4)
        elif 5*center/4<=d[j][0]<=3*center/2 and 0<=d[j][1]<=center/4:
            e[d[j][2]][3].add(5)
        elif 3*center/2<=d[j][0]<=7*center/4 and 0<=d[j][1]<=center/4:
            e[d[j][2]][3].add(6)
        elif 7*center/4<=d[j][0]<=2*center and 0<=d[j][1]<=center/4:
            e[d[j][2]][3].add(7)
        elif 0<=d[j][0]<=center/4 and center/4<=d[j][1]<=center/2:
            e[d[j][2]][3].add(8)
        elif center/4<=d[j][0]<=center/2 and center/4<=d[j][1]<=center/2:
            e[d[j][2]][3].add(9)
        elif center/2<=d[j][0]<=3*center/4 and center/4<=d[j][1]<=center/2:
            e[d[j][2]][3].add(10)
        elif 3*center/4<=d[j][0]<=center and center/4<=d[j][1]<=center/2:
            e[d[j][2]][3].add(11)
        elif center<=d[j][0]<=5*center/4 and center/4<=d[j][1]<=center/2:
            e[d[j][2]][3].add(12)
        elif 5*center/4<=d[j][0]<=3*center/2 and center/4<=d[j][1]<=center/2:
            e[d[j][2]][3].add(13)
        elif 3*center/2<=d[j][0]<=7*center/4 and center/4<=d[j][1]<=center/2:
            e[d[j][2]][3].add(14)
        elif 7*center/4<=d[j][0]<=2*center and center/4<=d[j][1]<=center/2:
            e[d[j][2]][3].add(15)
        elif 0<=d[j][0]<=center/4 and center/2<=d[j][1]<=3*center/4:
            e[d[j][2]][3].add(16)
        elif center/4<=d[j][0]<=center/2 and center/2<=d[j][1]<=3*center/4:
            e[d[j][2]][3].add(17)
        elif center/2<=d[j][0]<=3*center/4 and center/2<=d[j][1]<=3*center/4:
            e[d[j][2]][3].add(18)
        elif 3*center/4<=d[j][0]<=center and center/2<=d[j][1]<=3*center/4:
            e[d[j][2]][3].add(19)
        elif center<=d[j][0]<=5*center/4 and center/2<=d[j][1]<=3*center/4:
            e[d[j][2]][3].add(20)
        elif 5*center/4<=d[j][0]<=3*center/2 and center/2<=d[j][1]<=3*center/4:
            e[d[j][2]][3].add(21)
        elif 3*center/2<=d[j][0]<=7*center/4 and center/2<=d[j][1]<=3*center/4:
            e[d[j][2]][3].add(22)
        elif 7*center/4<=d[j][0]<=2*center and center/2<=d[j][1]<=3*center/4:
            e[d[j][2]][3].add(23)
        elif 0<=d[j][0]<=center/4 and 3*center/4<=d[j][1]<=center:
            e[d[j][2]][3].add(24)
        elif center/4<=d[j][0]<=center/2 and 3*center/4<=d[j][1]<=center:
            e[d[j][2]][3].add(25)
        elif center/2<=d[j][0]<=3*center/4 and 3*center/4<=d[j][1]<=center:
            e[d[j][2]][3].add(26)
        elif 3*center/4<=d[j][0]<=center and 3*center/4<=d[j][1]<=center:
            e[d[j][2]][3].add(27)
        elif center<=d[j][0]<=5*center/4 and 3*center/4<=d[j][1]<=center:
            e[d[j][2]][3].add(28)
        elif 5*center/4<=d[j][0]<=3*center/2 and 3*center/4<=d[j][1]<=center:
            e[d[j][2]][3].add(29)
        elif 3*center/2<=d[j][0]<=7*center/4 and 3*center/4<=d[j][1]<=center:
            e[d[j][2]][3].add(30)
        elif 7*center/4<=d[j][0]<=2*center and 3*center/4<=d[j][1]<=center:
            e[d[j][2]][3].add(31)
        elif 0<=d[j][0]<=center/4 and center<=d[j][1]<=center+center/4:
            e[d[j][2]][3].add(32)
        elif center/4<=d[j][0]<=center/2 and center<=d[j][1]<=center+center/4:
            e[d[j][2]][3].add(33)
        elif center/2<=d[j][0]<=3*center/4 and center<=d[j][1]<=center+center/4:
            e[d[j][2]][3].add(34)
        elif 3*center/4<=d[j][0]<=center and center<=d[j][1]<=center+center/4:
            e[d[j][2]][3].add(35)
        elif center<=d[j][0]<=5*center/4 and center<=d[j][1]<=center+center/4:
            e[d[j][2]][3].add(36)
        elif 5*center/4<=d[j][0]<=3*center/2 and center<=d[j][1]<=center+center/4:
            e[d[j][2]][3].add(37)
        elif 3*center/2<=d[j][0]<=7*center/4 and center<=d[j][1]<=center+center/4:
            e[d[j][2]][3].add(38)
        elif 7*center/4<=d[j][0]<=2*center and center<=d[j][1]<=center+center/4:
            e[d[j][2]][3].add(39)
        elif 0<=d[j][0]<=center/4 and center+center/4<=d[j][1]<=center+center/2:
            e[d[j][2]][3].add(40)
        elif center/4<=d[j][0]<=center/2 and center+center/4<=d[j][1]<=center+center/2:
            e[d[j][2]][3].add(41)
        elif center/2<=d[j][0]<=3*center/4 and center+center/4<=d[j][1]<=center+center/2:
            e[d[j][2]][3].add(42)
        elif 3*center/4<=d[j][0]<=center and center+center/4<=d[j][1]<=center+center/2:
            e[d[j][2]][3].add(43)
        elif center<=d[j][0]<=5*center/4 and center+center/4<=d[j][1]<=center+center/2:
            e[d[j][2]][3].add(44)
        elif 5*center/4<=d[j][0]<=3*center/2 and center+center/4<=d[j][1]<=center+center/2:
            e[d[j][2]][3].add(45)
        elif 3*center/2<=d[j][0]<=7*center/4 and center+center/4<=d[j][1]<=center+center/2:
            e[d[j][2]][3].add(46)
        elif 7*center/4<=d[j][0]<=2*center and center+center/4<=d[j][1]<=center+center/2:
            e[d[j][2]][3].add(47)
        elif 0<=d[j][0]<=center/4 and center+center/2<=d[j][1]<=center+3*center/4:
            e[d[j][2]][3].add(48)
        elif center/4<=d[j][0]<=center/2 and center+center/2<=d[j][1]<=center+3*center/4:
            e[d[j][2]][3].add(49)
        elif center/2<=d[j][0]<=3*center/4 and center+center/2<=d[j][1]<=center+3*center/4:
            e[d[j][2]][3].add(50)
        elif 3*center/4<=d[j][0]<=center and center+center/2<=d[j][1]<=center+3*center/4:
            e[d[j][2]][3].add(51)
        elif center<=d[j][0]<=5*center/4 and center+center/2<=d[j][1]<=center+3*center/4:
            e[d[j][2]][3].add(52)
        elif 5*center/4<=d[j][0]<=3*center/2 and center+center/2<=d[j][1]<=center+3*center/4:
            e[d[j][2]][3].add(53)
        elif 3*center/2<=d[j][0]<=7*center/4 and center+center/2<=d[j][1]<=center+3*center/4:
            e[d[j][2]][3].add(54)
        elif 7*center/4<=d[j][0]<=2*center and center+center/2<=d[j][1]<=center+3*center/4:
            e[d[j][2]][3].add(55)
        elif 0<=d[j][0]<=center/4 and center+center/2<=d[j][1]<=center+3*center/4:
            e[d[j][2]][3].add(56)
        elif center/4<=d[j][0]<=center/2 and center+3*center/4<=d[j][1]<=center+center:
            e[d[j][2]][3].add(57)
        elif center/2<=d[j][0]<=3*center/4 and center+3*center/4<=d[j][1]<=center+center:
            e[d[j][2]][3].add(58)
        elif 3*center/4<=d[j][0]<=center and center+3*center/4<=d[j][1]<=center+center:
            e[d[j][2]][3].add(59)
        elif center<=d[j][0]<=5*center/4 and center+3*center/4<=d[j][1]<=center+center:
            e[d[j][2]][3].add(60)
        elif 5*center/4<=d[j][0]<=3*center/2 and center+3*center/4<=d[j][1]<=center+center:
            e[d[j][2]][3].add(61)
        elif 3*center/2<=d[j][0]<=7*center/4 and center+3*center/4<=d[j][1]<=center+center:
            e[d[j][2]][3].add(62)
        elif 7*center/4<=d[j][0]<=2*center and center+3*center/4<=d[j][1]<=center+center:
            e[d[j][2]][3].add(63)
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
    q16=[]
    q17=[]
    q18=[]
    q19=[]
    q20=[]
    q21=[]
    q22=[]
    q23=[]
    q24=[]
    q25=[]
    q26=[]
    q27=[]
    q28=[]
    q29=[]
    q30=[]
    q31=[]
    q32=[]
    q33=[]
    q34=[]
    q35=[]
    q36=[]
    q37=[]
    q38=[]
    q39=[]
    q40=[]
    q41=[]
    q42=[]
    q43=[]
    q44=[]
    q45=[]
    q46=[]
    q47=[]
    q48=[]
    q49=[]
    q50=[]
    q51=[]
    q52=[]
    q53=[]
    q54=[]
    q55=[]
    q56=[]
    q57=[]
    q58=[]
    q59=[]
    q60=[]
    q61=[]
    q62=[]
    q63=[]
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
            elif l==16:
                q16.append([e[k][0],e[k][1],e[k][2]])
            elif l==17:
                q17.append([e[k][0],e[k][1],e[k][2]])
            elif l==18:
                q18.append([e[k][0],e[k][1],e[k][2]])
            elif l==19:
                q19.append([e[k][0],e[k][1],e[k][2]])
            elif l==20:
                q20.append([e[k][0],e[k][1],e[k][2]])
            elif l==21:
                q21.append([e[k][0],e[k][1],e[k][2]])
            elif l==22:
                q22.append([e[k][0],e[k][1],e[k][2]])
            elif l==23:
                q23.append([e[k][0],e[k][1],e[k][2]])
            elif l==24:
                q24.append([e[k][0],e[k][1],e[k][2]])
            elif l==25:
                q25.append([e[k][0],e[k][1],e[k][2]])
            elif l==26:
                q26.append([e[k][0],e[k][1],e[k][2]])
            elif l==27:
                q27.append([e[k][0],e[k][1],e[k][2]])
            elif l==28:
                q28.append([e[k][0],e[k][1],e[k][2]])
            elif l==29:
                q29.append([e[k][0],e[k][1],e[k][2]])
            elif l==30:
                q30.append([e[k][0],e[k][1],e[k][2]])
            elif l==31:
                q31.append([e[k][0],e[k][1],e[k][2]])
            elif l==32:
                q32.append([e[k][0],e[k][1],e[k][2]])
            elif l==33:
                q33.append([e[k][0],e[k][1],e[k][2]])
            elif l==34:
                q34.append([e[k][0],e[k][1],e[k][2]])
            elif l==35:
                q35.append([e[k][0],e[k][1],e[k][2]])
            elif l==36:
                q36.append([e[k][0],e[k][1],e[k][2]])
            elif l==37:
                q37.append([e[k][0],e[k][1],e[k][2]])
            elif l==38:
                q38.append([e[k][0],e[k][1],e[k][2]])
            elif l==39:
                q39.append([e[k][0],e[k][1],e[k][2]])
            elif l==40:
                q40.append([e[k][0],e[k][1],e[k][2]])
            elif l==41:
                q41.append([e[k][0],e[k][1],e[k][2]])
            elif l==42:
                q42.append([e[k][0],e[k][1],e[k][2]])
            elif l==43:
                q43.append([e[k][0],e[k][1],e[k][2]])
            elif l==44:
                q44.append([e[k][0],e[k][1],e[k][2]])
            elif l==45:
                q45.append([e[k][0],e[k][1],e[k][2]])
            elif l==46:
                q46.append([e[k][0],e[k][1],e[k][2]])
            elif l==47:
                q47.append([e[k][0],e[k][1],e[k][2]])
            elif l==48:
                q48.append([e[k][0],e[k][1],e[k][2]])
            elif l==49:
                q49.append([e[k][0],e[k][1],e[k][2]])
            elif l==50:
                q50.append([e[k][0],e[k][1],e[k][2]])
            elif l==51:
                q51.append([e[k][0],e[k][1],e[k][2]])
            elif l==52:
                q52.append([e[k][0],e[k][1],e[k][2]])
            elif l==53:
                q53.append([e[k][0],e[k][1],e[k][2]])
            elif l==54:
                q54.append([e[k][0],e[k][1],e[k][2]])
            elif l==55:
                q55.append([e[k][0],e[k][1],e[k][2]])
            elif l==56:
                q56.append([e[k][0],e[k][1],e[k][2]])
            elif l==57:
                q57.append([e[k][0],e[k][1],e[k][2]])
            elif l==58:
                q58.append([e[k][0],e[k][1],e[k][2]])
            elif l==59:
                q59.append([e[k][0],e[k][1],e[k][2]])
            elif l==60:
                q60.append([e[k][0],e[k][1],e[k][2]])
            elif l==61:
                q61.append([e[k][0],e[k][1],e[k][2]])
            elif l==62:
                q62.append([e[k][0],e[k][1],e[k][2]])
            elif l==63:
                q63.append([e[k][0],e[k][1],e[k][2]])
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
    q.append(q16)
    q.append(q17)
    q.append(q18)
    q.append(q19)
    q.append(q20)
    q.append(q21)
    q.append(q22)
    q.append(q23)
    q.append(q24)
    q.append(q25)
    q.append(q26)
    q.append(q27)
    q.append(q28)
    q.append(q29)
    q.append(q30)
    q.append(q31)
    q.append(q32)
    q.append(q33)
    q.append(q34)
    q.append(q35)
    q.append(q36)
    q.append(q37)
    q.append(q38)
    q.append(q39)
    q.append(q40)
    q.append(q41)
    q.append(q42)
    q.append(q43)
    q.append(q44)
    q.append(q45)
    q.append(q46)
    q.append(q47)
    q.append(q48)
    q.append(q49)
    q.append(q50)
    q.append(q51)
    q.append(q52)
    q.append(q53)
    q.append(q54)
    q.append(q55)
    q.append(q56)
    q.append(q57)
    q.append(q58)
    q.append(q59)
    q.append(q60)
    q.append(q61)
    q.append(q62)
    q.append(q63)
    ns=558
    parsum=0

    parsum,ns,average = topo(q,num_proc)
    return parsum,ns,average
