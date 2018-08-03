from lri import *
def fourlri():
	p=[]
	q=[]
	r=[]
	s=[]

	for i in [16,32,64,128,256,512]:
		for j in range(10):
			p.append(lri('normal',1024,1000000,'h',2048,6,'torus','h',i))
			q.append(lri('normal',1024,1000000,'g',2048,6,'torus','g',i))
			r.append(lri('normal',1024,1000000,'z',2048,6,'torus','z',i))
			s.append(lri('normal',1024,1000000,'r',2048,6,'torus','r',i))
	return p,q,r,s

