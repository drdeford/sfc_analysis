import linecache as lc
import numpy as np
import sys
import math
import time
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

total_time = time.time()
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
filename = str(sys.argv[1])
num_points=int(lc.getline('./point_data/'+filename,1)[:-1])
bits = int(sys.argv[2])
num_its=int(sys.argv[3])
efilename = str(sys.argv[4])

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

#print('proc', rank, 'needs to talk to', comm_procs, num_comms,'total comms')

buf_size=np.zeros(1)

comm_sizes=[]
for i in range(len(comm_list)):
        comm_sizes.append(len(comm_list[i][1]))
buf_size[0]=max(comm_sizes)
max_buf=np.zeros(1)
comm.Allreduce(buf_size,max_buf,op=MPI.MAX)

#if rank ==1:
#        print('Process:',rank,'has comm_list:',comm_list)
#        print('Process:',rank,'has comm_list:',comm_procs)
#        print('Process:',rank,'has comm_list:',point_list)
#        print('commsizes',comm_sizes,'max',buf_size[0])
#print('Process;',rank,'commsizes',comm_sizes,'max',buf_size[0],'received', max_buf[0])


temp2=[]
for x in range(bits+1):
        temp2.append(0.)
temp2=np.array(temp2)

temp=[]
for r in range(int(max_buf[0])):
        temp.append(temp2)
temp=np.array(temp)
#if rank==1:
#        print(temp)
send_time=0
receive_time=0
comp_time=0
messages_sent=0
volume_of_messages=0
#if rank ==1:
#        print(point_list)
for its in range(num_its):
        send_count=time.time()
        for j in range(num_comms):
                p_data=[]
                #num_sent=np.zeros(1)
                for k in comm_list[j][1]:
                        #p_data.append([k,point_list[k-start][-bits:]])#next three lines test
                        #p_data.append([k,x for x in point_list[k-start][-bits:]])
                        a=point_list[k-start][-bits:]
                        a.insert(0,k)
                        p_data.append(a)	
                #num_sent[0]=len(p_data)	
                p_data=np.array(p_data)
                #comm.Send(num_sent,dest= int(comm_list[j][0]))
                #print(rank,'I am sending', num_sent[0], 'to', comm_list[j][0])
                comm.Send(p_data,dest = int(comm_list[j][0]))
                #print(rank, 'I sent stuff to', comm_list[j][0])
        send_time=send_time+(time.time()-send_count)
        ans=[]
        
        receive_count=time.time()
        rec_buf=[]
        for j in range(num_comms):
                rec_buf.append(temp)
        rec_buf=np.array(rec_buf)
        for j in range(num_comms):
                #print(rec_buf)
                comm.Recv(rec_buf[j],source=comm_list[j][0])
        receive_time=receive_time+(time.time()-receive_count)
        #if rank==1:
        #       print(rec_buf)
        rec_buf=list(rec_buf)
        for i in range(num_comms):
                rec_buf[i]=list(rec_buf[i])
        for k in range(num_comms):
                count=0
                for d in range(int(max_buf[0])):
                        rec_buf[k][d]=list(rec_buf[k][d])
                        rec_buf[k][d][0]=int(rec_buf[k][d][0])
                        if rec_buf[k][d][1]==0.:
                                count=count+1
                        else:
                                1+1
                for i in range(count):
                        rec_buf[k].pop(-1)
        in_dat=[]
        for i in range(num_comms):
                for k in rec_buf[i]:
                        in_dat.append(k)
        #if rank ==1:
        #        print(rec_buf)

        
        comp_count=time.time()
       # if rank==1:
       #         print(in_dat)
       #         print(comm_list)
       #         for i in range(start,end+1):
       #                 print(i)
       #         print(point_list)
        for i in range(len(point_list)):
                num_comps=len(point_list[i])-bits-3
                if num_comps !=0:
                        for j in range(num_comps):
                                #print(rank, i+start,point_list[i][3+j])
                                        
                                if int(point_list[i][3+j]) not in range(start,end+1):
                                      #  if rank ==1:
                                      #          print(13+i,j,point_list[i][3+j])

                                        #print(rank,start+i,point_list[i][3+j])
                                        place=[(k,h.index(int(point_list[i][3+j]))) for k, h in enumerate(in_dat) if int(point_list[i][3+j]) in h]
                                        #print(place)
                                        if place != []:
                                                point=place[0][0]
                                                for m in range(bits):
                                                        point_list[i][-(m+1)]=point_list[i][-(m+1)]+(in_dat[point][m+1]*(1/num_its))
                                                #if (its%2)==0:
                                                #        point_list[i][-(m+1)]=point_list[i][-(m+1)]*in_dat[point][m+1]
                                                #else:       
                                                #        point_list[i][-(m+1)]=point_list[i][-(m+1)]+in_dat[point][m+1]
                                

      #  if rank ==1:
       #         print(point_list)
        



        comp_time=comp_time+(time.time()-comp_count)

#if rank ==1:
#       print(comm_list,ans)


num_con=0
for i in range(num_comms):
		num_con=num_con+len(comm_list[i][1])
final_time=time.time()-total_time
if rank==0:
        m=np.zeros(1)
        print('\nProcess',rank, 'finished in:', final_time, 'seconds\n\nsend time: ',send_time,'seconds\nreceive time: ', receive_time,'seconds\ncomputation time: ',comp_time,'seconds','\nmessages sent: ',num_comms*num_its,' communicated with: ',comm_procs,'\nvolume sent: ', num_con*(bits+1)*num_its)
        comm.Send(m,dest=1)
        comm.Recv(m,source=size-1)
else:
        m=np.zeros(1)
        comm.Recv(m,source=rank-1)
        print('\nProcess',rank, 'finished in:', final_time, 'seconds\n\nsend time: ',send_time,'seconds\nreceive time: ', receive_time,'seconds\ncomputation time: ',comp_time,'seconds','\nmessages sent: ',num_comms*num_its,' communicated with: ',comm_procs,'\nvolume sent: ', num_con*(bits+1)*num_its)
        comm.Send(m,dest=((rank+1)%size))


aloc_send=np.array([send_time],dtype='float')
aloc_rec=np.array([receive_time],dtype='float')
aloc_com=np.array([comp_time],dtype='float')
aloc_comms=np.array([num_comms*num_its],dtype='float')
aloc_vol=np.array([num_con*(bits+1)*num_its],dtype='float')



aovr_send=np.zeros(1)
aovr_rec=np.zeros(1)
aovr_com=np.zeros(1)
aovr_comms=np.zeros(1)
aovr_vol=np.zeros(1)

iovr_send=np.zeros(1)
iovr_rec=np.zeros(1)
iovr_com=np.zeros(1)
iovr_comms=np.zeros(1)
iovr_vol=np.zeros(1)

comm.Reduce(aloc_send,aovr_send,op=MPI.MAX,root=0)
comm.Reduce(aloc_rec,aovr_rec,op=MPI.MAX,root=0)
comm.Reduce(aloc_com,aovr_com,op=MPI.MAX,root=0)
comm.Reduce(aloc_comms,aovr_comms,op=MPI.MAX,root=0)
comm.Reduce(aloc_vol,aovr_vol,op=MPI.MAX,root=0)

comm.Reduce(aloc_send,iovr_send,op=MPI.MIN,root=0)
comm.Reduce(aloc_rec,iovr_rec,op=MPI.MIN,root=0)
comm.Reduce(aloc_com,iovr_com,op=MPI.MIN,root=0)
comm.Reduce(aloc_comms,iovr_comms,op=MPI.MIN,root=0)
comm.Reduce(aloc_vol,iovr_vol,op=MPI.MIN,root=0)

if rank ==0:
	print('\n\nOverall:\n\nThe slowest send time was: ', aovr_send[0], 'seconds','\nThe slowest receive time was: ', aovr_rec[0], 'seconds', '\nThe slowest computation time was: ', aovr_com[0], 'seconds','\nThe largest number of messages was: ', int(aovr_comms[0]),'\nThe largest volume of messages was: ', int(aovr_vol[0]))

	print('The fastest send time was: ', iovr_send[0], 'seconds','\nThe fastest receive time was: ', iovr_rec[0], 'seconds', '\nThe fastest computation time was: ', iovr_com[0], 'seconds','\nThe smallest number of messages was: ',int(iovr_comms[0]),'\nThe smallest volume of messages was: ', int(iovr_vol[0]))
	afile=open('./experiment_data/'+efilename,'a')
	afile.write('\n\n***************'+filename+'_'+str(num_points)+'_Points_'+str(num_its)+'_Iterations'+'***************\n')
	afile.write('\nOverall:\n\nThe slowest send time was: '+str( aovr_send[0])+ 'seconds'+'\nThe slowest receive time was: '+ str(aovr_rec[0])+ 'seconds'+ '\nThe slowest computation time was: '+ str( aovr_com[0])+ 'seconds'+'\nThe largest number of messages was: '+str( int(aovr_comms[0]))+'\nThe largest volume of messages was: '+str( int(aovr_vol[0]))+ '\nThe fastest send time was: '+str( iovr_send[0])+ 'seconds'+'\nThe fastest receive time was: '+str( iovr_rec[0])+ 'seconds'+ '\nThe fastest computation time was: '+str( iovr_com[0])+ 'seconds'+'\nThe smallest number of messages was: '+str(int(iovr_comms[0]))+'\nThe smallest volume of messages was: '+str( int(iovr_vol[0])))




	afile.close()
	

