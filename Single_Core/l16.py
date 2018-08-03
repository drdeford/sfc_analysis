
import math
import os
def torus16(q,num_proc):

    ns = 77
    parsum=0    
        
    for i in [2,3,6,7,8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[0][0][0]-q[i][0][0])
            y_dist= abs(q[0][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    

    for i in [3,7,8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[1][0][0]-q[i][0][0])
            y_dist= abs(q[1][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    

    for i in [8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[2][0][0]-q[i][0][0])
            y_dist= abs(q[2][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    
          
    for i in [4,5,8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[3][0][0]-q[i][0][0])
            y_dist= abs(q[3][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    

    for i in [6,7,10,11,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[4][0][0]-q[i][0][0])
            y_dist= abs(q[4][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    

    for i in [7,11,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[5][0][0]-q[i][0][0])
            y_dist= abs(q[5][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    

    for i in [8,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[6][0][0]-q[i][0][0])
            y_dist= abs(q[6][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    

    for i in [8,9,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[7][0][0]-q[i][0][0])
            y_dist= abs(q[7][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    

    for i in [10,11,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[8][0][0]-q[i][0][0])
            y_dist= abs(q[8][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    

    for i in [11,15] :
        if q[i]!=[]:
            x_dist= abs(q[9][0][0]-q[i][0][0])
            y_dist= abs(q[9][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    

    for i in [12] :
        if q[i]!=[]:
            x_dist= abs(q[10][0][0]-q[i][0][0])
            y_dist= abs(q[10][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    

    for i in [12,13] :
        if q[i]!=[]:
            x_dist= abs(q[11][0][0]-q[i][0][0])
            y_dist= abs(q[11][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    

    for i in [14,15] :
        if q[i]!=[]:
            x_dist= abs(q[12][0][0]-q[i][0][0])
            y_dist= abs(q[12][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    

    for i in [15] :
        if q[i]!=[]:
            x_dist= abs(q[13][0][0]-q[i][0][0])
            y_dist= abs(q[13][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    

    average = parsum/ns
    return parsum,ns,average 

def grid16(q,num_proc):

    ns = 77
    parsum=0    
        
    for i in [2,3,6,7,8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[0][0][0]-q[i][0][0])
            y_dist= abs(q[0][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist

    for i in [3,7,8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[1][0][0]-q[i][0][0])
            y_dist= abs(q[1][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist

    for i in [8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[2][0][0]-q[i][0][0])
            y_dist= abs(q[2][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
          
    for i in [4,5,8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[3][0][0]-q[i][0][0])
            y_dist= abs(q[3][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist

    for i in [6,7,10,11,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[4][0][0]-q[i][0][0])
            y_dist= abs(q[4][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist

    for i in [7,11,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[5][0][0]-q[i][0][0])
            y_dist= abs(q[5][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist

    for i in [8,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[6][0][0]-q[i][0][0])
            y_dist= abs(q[6][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist

    for i in [8,9,12,13,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[7][0][0]-q[i][0][0])
            y_dist= abs(q[7][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist

    for i in [10,11,14,15] :
        if q[i]!=[]:
            x_dist= abs(q[8][0][0]-q[i][0][0])
            y_dist= abs(q[8][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist

    for i in [11,15] :
        if q[i]!=[]:
            x_dist= abs(q[9][0][0]-q[i][0][0])
            y_dist= abs(q[9][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist

    for i in [12] :
        if q[i]!=[]:
            x_dist= abs(q[10][0][0]-q[i][0][0])
            y_dist= abs(q[10][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist

    for i in [12,13] :
        if q[i]!=[]:
            x_dist= abs(q[11][0][0]-q[i][0][0])
            y_dist= abs(q[11][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist

    for i in [14,15] :
        if q[i]!=[]:
            x_dist= abs(q[12][0][0]-q[i][0][0])
            y_dist= abs(q[12][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist

    for i in [15] :
        if q[i]!=[]:
            x_dist= abs(q[13][0][0]-q[i][0][0])
            y_dist= abs(q[13][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist

    average = parsum/ns
    return parsum,ns,average

def hypercube16(q,num_proc):

    ns = 77
    parsum=0    
        
    for i in [2,3,6,7,8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            dist = bin(q[0][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)

    for i in [3,7,8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            dist = bin(q[1][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)

           

    for i in [8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            dist = bin(q[2][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)

            
          
    for i in [4,5,8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            dist = bin(q[3][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)

            

    for i in [6,7,10,11,12,13,14,15] :
        if q[i]!=[]:
            dist = bin(q[4][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)

            

    for i in [7,11,12,13,14,15] :
        if q[i]!=[]:
            dist = bin(q[5][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)

            

    for i in [8,12,13,14,15] :
        if q[i]!=[]:
            dist = bin(q[6][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)

            

    for i in [8,9,12,13,14,15] :
        if q[i]!=[]:
            dist = bin(q[7][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)

            

    for i in [10,11,14,15] :
        if q[i]!=[]:
            dist = bin(q[8][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)

           

    for i in [11,15] :
        if q[i]!=[]:
            dist = bin(q[9][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)

            

    for i in [12] :
        if q[i]!=[]:
            dist = bin(q[10][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)

            

    for i in [12,13] :
        if q[i]!=[]:
            dist = bin(q[11][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)

            

    for i in [14,15] :
        if q[i]!=[]:
            dist = bin(q[12][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)

            

    for i in [15] :
        if q[i]!=[]:
            dist = bin(q[13][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)

            

    average = parsum/ns
    return parsum,ns,average         

def quadtree16(q,num_proc):

    ns = 77
    parsum=0    
    num_dig=math.ceil(math.log(num_proc,2))
    for i in [2,3,6,7,8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            leafpos1=bin(q[0][0][2])[2:]
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

    for i in [3,7,8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            leafpos1=bin(q[1][0][2])[2:]
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
           

    for i in [8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            leafpos1=bin(q[2][0][2])[2:]
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
            
          
    for i in [4,5,8,9,10,11,12,13,14,15] :
        if q[i]!=[]:
            leafpos1=bin(q[3][0][2])[2:]
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
            

    for i in [6,7,10,11,12,13,14,15] :
        if q[i]!=[]:
            leafpos1=bin(q[4][0][2])[2:]
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
            

    for i in [7,11,12,13,14,15] :
        if q[i]!=[]:
            leafpos1=bin(q[5][0][2])[2:]
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
            

    for i in [8,12,13,14,15] :
        if q[i]!=[]:
            leafpos1=bin(q[6][0][2])[2:]
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

            

    for i in [8,9,12,13,14,15] :
        if q[i]!=[]:
            leafpos1=bin(q[7][0][2])[2:]
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
            

    for i in [10,11,14,15] :
        if q[i]!=[]:
            leafpos1=bin(q[8][0][2])[2:]
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
           

    for i in [11,15] :
        if q[i]!=[]:
            leafpos1=bin(q[9][0][2])[2:]
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
            

    for i in [12] :
        if q[i]!=[]:
            leafpos1=bin(q[10][0][2])[2:]
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
            

    for i in [12,13] :
        if q[i]!=[]:
            leafpos1=bin(q[11][0][2])[2:]
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
            

    for i in [14,15] :
        if q[i]!=[]:
            leafpos1=bin(q[12][0][2])[2:]
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
            

    for i in [15] :
        if q[i]!=[]:
            leafpos1=bin(q[13][0][2])[2:]
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
            

    average = parsum/ns
    return parsum,ns,average        

def linear16():
    a=2
    return a

def cyclic16():
    a=3
    return a




