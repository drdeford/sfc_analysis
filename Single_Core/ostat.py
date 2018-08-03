import math
def dstat(p):
    parsum=0
    for i in range(10):
        parsum=parsum+p[i]
    mean1=parsum/10
    parsum=0
    for i in range(10,20):
        parsum=parsum+p[i]
    mean2=parsum/10
    parsum=0
    for i in range(20,30):
        parsum=parsum+p[i]
    mean3=parsum/10
    parsum=0
    for i in range(10):
        parsum=parsum+((p[i]-mean1)**2)
    std1=math.sqrt(parsum/9)
    parsum=0
    for i in range(10,20):
        parsum=parsum+((p[i]-mean2)**2)
    std2=math.sqrt(parsum/9)
    parsum=0
    for i in range(20,30):
        parsum=parsum+((p[i]-mean3)**2)
    std3=math.sqrt(parsum/9)
    return mean1,std1, mean2,std2,mean3,std3
