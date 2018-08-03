import linecache as lc
import numpy as np
import sys
import math
import time
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

start_time = time.time()
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
filename = str(sys.argv[1])
num_points=int(lc.getline('./point_data/'+filename,1)[:-1])
bits = int(sys.argv[2])
ppp=math.floor(num_points/size)
extra_points=num_points-(ppp*size)

point_list=[]
point_ind=[]

if rank < extra_points:#used to be equal
	start = (ppp+1)*rank
	end = start+ppp#+1
	point_ind=range(start+2,end+3)
else:
	start = (ppp+1)*extra_points+(ppp)*(rank-extra_points)
	end = start + ppp-1
	point_ind=range(start+2,end+3)

#print(num_points,rank, start, end)
#print(filename, num_points)

for index in point_ind:
	point_list.append([float(x) for x in lc.getline('./point_data/'+filename,index)[1:-2].split(',')])
holds=[]
for i in point_list:#next four test linesand one above
	holds.append(i[2])
#print('Processor', rank, 'has these points\n',holds,'\n out of ', num_points, 'total points')
#print(point_list, 'belongs to', rank)
comm_list=[]
comm_to_send=[]
ptt=[]
for k in range(size):
	comm_list.append([k,[]])
for i in range(len(point_list)):
	for j in point_list[i][3:(-bits)]:
		ptt.append(j)
ptt=list(set(ptt))
		#comm_list[int(j)].append(int(i))#Wrong, this is the number of the point not the number of the holding process :(
#print(rank,'has',comm_list)
point_data=[]
home_proc=0
proc_dict=[]
for k in ptt:
	close_int=0 
	less_p=0
	if k < (ppp+1)*extra_points:
		
		home_proc=int(math.floor((k)/(ppp+1)))
	else:
		less_p=k-((ppp+1)*extra_points)
		home_proc=int(extra_points+math.floor(less_p/ppp))
	proc_dict.append((k,home_proc))

proc_dict=dict(proc_dict)

#print('proc',rank,'s dict',proc_dict)
	
for i in range(len(point_list)):
	for j in point_list[i][3:(-bits)]:
		comm_list[proc_dict[j]][1].append(int(point_list[i][2]))

#print('Process',rank,'comm_list',comm_list)

del_list=[]
comm_list.pop(rank)
for m in range(len(comm_list)):
	if comm_list[m][1]==[]:
		del_list.append(m)
	else:
		1+1
#print(rank ,'delllist',del_list)

if len(del_list) > 1:
	del_list.reverse()
	for m in del_list:
		comm_list.pop(m)
else:
	for i in del_list:
		comm_list.pop(i)
num_comms = len(comm_list)
comm_procs=[]
for i in range(num_comms):
	comm_list[i][1]=list(set(comm_list[i][1]))
	comm_procs.append(comm_list[i][0])
#print('proc',rank,'post deletion comm list', comm_list,num_comms)
#if rank ==1:
#	time.sleep(5)
print('proc', rank, 'needs to talk to', comm_procs, num_comms)

ans=[]
#temp=np.zeros(1)
#temp2=np.array([0.,0.,0.])
temp2=[]
for x in range(bits+1):
	temp2.append(0.)
temp2=np.array(temp2)

for j in range(num_comms):
	temp=[]
	p_data=[]
	num_sent=np.zeros(1)
	temp1=np.zeros(1)
	for k in comm_list[j][1]:
		#p_data.append([k,point_list[k-start][-bits:]])#next three lines test
		#p_data.append([k,x for x in point_list[k-start][-bits:]])
		a=point_list[k-start][-bits:]
		a.insert(0,k)
		p_data.append(a)	
	num_sent[0]=len(p_data)	
	p_data=np.array(p_data)
	comm.Send(num_sent,dest= int(comm_list[j][0]))
	comm.Recv(temp1,source=comm_list[j][0])
	#print(rank,'I am sending', num_sent[0], 'to', comm_list[j][0])
	var=int(temp1[0])
	for r in range(var):
		temp.append(temp2)
	temp=np.array(temp)
	comm.Send(p_data,dest = int(comm_list[j][0]))
	#print(rank, 'I sent stuff to', comm_list[j][0])
	
	comm.Recv(temp,source=comm_list[j][0])
	ans.append(temp)
#	print('Process', rank,'is sending', p_data,'to process', comm_list[j][0])

#for j in range(num_comms):
#	temp=[]
	
	#for rec in range(2):
	#print(rank, 'waiting on', comm_list[j][0])
	
	#print(rank,'I recvd',temp1[0],'from', comm_list[j][0])
	
	
#if rank == 2:
#	print('Process',rank, 'holds',ans)
#else:
#	1+1
print('Process',rank, 'finished in', time.time() - start_time, 'seconds')
#print('\n Process',rank,'has final', ans,'\n')









	
		
