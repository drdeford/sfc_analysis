import math
import os
def torus256(q,z,num_proc):
    parsum=0
    ns=0
    for n in range(256):
        for i in z[n]:
            if q[i]!=[[0,0,0]]:
                x_dist= abs(q[n][0][0]-q[i][0][0])
                y_dist= abs(q[n][0][1]-q[i][0][1])
                parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
                ns=ns+1
    average=parsum/ns
    parsum=parsum/2
    ns=ns/2
    return parsum,ns,average

def grid256(q,z,num_proc):
    parsum=0
    ns=0
    for n in range(256):
        for i in z[n]:
            if q[i]!=[[0,0,0]]:
                x_dist= abs(q[n][0][0]-q[i][0][0])
                y_dist= abs(q[n][0][1]-q[i][0][1])
                parsum= parsum +x_dist+y_dist
                ns=ns+1
    average=parsum/ns
    parsum=parsum/2
    ns=ns/2
    return parsum,ns,average

def hypercube256(q,z,num_proc):
    parsum=0
    ns=0
    for n in range(256):
        for i in z[n]:
            if q[i]!=[[0,0,0]]:
                ns=ns+1
                dist = bin(q[n][0][2]^q[i][0][2])[2:]
                for j in dist:
                    parsum=parsum+int(j)
                
    average=parsum/ns
    parsum=parsum/2
    ns=ns/2
    return parsum,ns,average

def quadtree256(q,z,num_proc):
    parsum=0
    ns=0
    num_dig=math.ceil(math.log(num_proc,2))
    for n in range(256):
        for i in z[n]:
            if q[i]!=[[0,0,0]]:
                ns=ns+1
                leafpos1=bin(q[n][0][2])[2:]
                if len(leafpos1)<num_dig:
                    for l in range(num_dig-len(leafpos1)):
                        leafpos1='0'+leafpos1
                
                leafpos2=bin(q[i][0][2])[2:]
                if len(leafpos2)<num_dig:
                    for l in range(num_dig-len(leafpos2)):
                        leafpos2='0'+leafpos2
                cp=len(os.path.commonprefix([leafpos1,leafpos2]))
                if cp%2==1:
                    cp=cp-1
                dist=math.ceil((num_dig-cp)/2)
                parsum=parsum+2*dist

    average=parsum/ns
    parsum=parsum/2
    ns=ns/2
    return parsum,ns,average
