import math
def fivestat(p):
    parsum=0
    for i in range(5):
        parsum=parsum+p[i]
    mean1=parsum/5
    parsum=0
    for i in range(5,10):
        parsum=parsum+p[i]
    mean2=parsum/5
    parsum=0
    for i in range(10,15):
        parsum=parsum+p[i]
    mean3=parsum/5
    parsum=0
    for i in range(5):
        parsum=parsum+((p[i]-mean1)**2)
    std1=math.sqrt(parsum/4)
    parsum=0
    for i in range(5,10):
        parsum=parsum+((p[i]-mean2)**2)
    std2=math.sqrt(parsum/4)
    parsum=0
    for i in range(10,15):
        parsum=parsum+((p[i]-mean3)**2)
    std3=math.sqrt(parsum/4)
    return mean1,std1, mean2,std2,mean3,std3
