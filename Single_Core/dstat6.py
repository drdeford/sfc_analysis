import math
def dstat6(p):
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
    for i in range(30,40):
        parsum=parsum+p[i]
    mean4=parsum/10
    
    parsum=0
    for i in range(40,50):
        parsum=parsum+p[i]
    mean5=parsum/10
    
    parsum=0
    for i in range(50,60):
        parsum=parsum+p[i]
    mean6=parsum/10

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
    
    parsum=0
    for i in range(30,40):
        parsum=parsum+((p[i]-mean4)**2)
    std4=math.sqrt(parsum/9)
    
    parsum=0
    for i in range(40,50):
        parsum=parsum+((p[i]-mean5)**2)
    std5=math.sqrt(parsum/9)
    
    parsum=0
    for i in range(50,60):
        parsum=parsum+((p[i]-mean6)**2)
    std6=math.sqrt(parsum/9)
    
    return mean1,std1, mean2,std2, mean3, std3,mean4,std4, mean5,std5, mean6, std6
