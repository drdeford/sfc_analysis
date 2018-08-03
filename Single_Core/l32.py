
import math
import os
def torus32(q,num_proc):
    parsum=0
    ns=558
    for i in range(len(q)):
        if q[i]==[]:
            q[i]=[[0,0,0]]
    
    for i in [2,3,10,11,16,17,18,19,24,25,26,27]  :
        if q[i]!=[[0,0,0]]:    
            x_dist= abs(q[0][0][0]-q[i][0][0])
            y_dist= abs(q[0][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [3,11,16,17,18,19,24,25,26,27]  :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[1][0][0]-q[i][0][0])
            y_dist= abs(q[1][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));

    for i in [4,5,8,12,13,16,17,18,19,20,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[2][0][0]-q[i][0][0])
            y_dist= abs(q[2][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [5,8,9,13,16,17,18,19,20,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[3][0][0]-q[i][0][0])
            y_dist= abs(q[3][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [6,7,10,14,15,18,19,20,21,22,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[4][0][0]-q[i][0][0])
            y_dist= abs(q[4][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [7,10,11,15,18,19,20,21,22,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[5][0][0]-q[i][0][0])
            y_dist= abs(q[5][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [12, 20,21,22,23,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[6][0][0]-q[i][0][0])
            y_dist= abs(q[6][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [12,13,20,21,22,23,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[7][0][0]-q[i][0][0])
            y_dist= abs(q[7][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [10,11,18,19,24,25,26,27] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[8][0][0]-q[i][0][0])
            y_dist= abs(q[8][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [11,19,24,25,26,27] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[9][0][0]-q[i][0][0])
            y_dist= abs(q[9][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [12,13,16,20,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[10][0][0]-q[i][0][0])
            y_dist= abs(q[10][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [13,16,17,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[11][0][0]-q[i][0][0])
            y_dist= abs(q[11][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [14,15,18,22,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[12][0][0]-q[i][0][0])
            y_dist= abs(q[12][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [15,18,19,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[13][0][0]-q[i][0][0])
            y_dist= abs(q[13][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [20,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[14][0][0]-q[i][0][0])
            y_dist= abs(q[14][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [20,21,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[15][0][0]-q[i][0][0])
            y_dist= abs(q[15][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [18,19,26,27,32,33,34,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[16][0][0]-q[i][0][0])
            y_dist= abs(q[16][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [19,27,32,33,34,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[17][0][0]-q[i][0][0])
            y_dist= abs(q[17][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [20,21,28,29,24,32,33,34,35,36,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[18][0][0]-q[i][0][0])
            y_dist= abs(q[18][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [21,24,25,29,32,33,34,35,36,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[19][0][0]-q[i][0][0])
            y_dist= abs(q[19][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [22,23,26,30,31,34,35,36,37,38,39,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[20][0][0]-q[i][0][0])
            y_dist= abs(q[20][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [23,26,27,31,34,35,36,37,38,39,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[21][0][0]-q[i][0][0])
            y_dist= abs(q[21][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [28,36,37,38,39,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[22][0][0]-q[i][0][0])
            y_dist= abs(q[22][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [28,29,36,37,38,39,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[23][0][0]-q[i][0][0])
            y_dist= abs(q[23][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [26,27,34,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[24][0][0]-q[i][0][0])
            y_dist= abs(q[24][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [27,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[25][0][0]-q[i][0][0])
            y_dist= abs(q[25][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [28,29,32,36,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[26][0][0]-q[i][0][0])
            y_dist= abs(q[26][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [29,32,33,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[27][0][0]-q[i][0][0])
            y_dist= abs(q[27][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [30,31,34,38,39,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[28][0][0]-q[i][0][0])
            y_dist= abs(q[28][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [31,34,35,37,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[29][0][0]-q[i][0][0])
            y_dist= abs(q[29][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [36,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[30][0][0]-q[i][0][0])
            y_dist= abs(q[30][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [36,37,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[31][0][0]-q[i][0][0])
            y_dist= abs(q[31][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [34,35,42,43,46,47,48,49,50,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[32][0][0]-q[i][0][0])
            y_dist= abs(q[32][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [35,43,48,49,50,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[33][0][0]-q[i][0][0])
            y_dist= abs(q[33][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [36,37,40,44,45,48,49,50,51,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[34][0][0]-q[i][0][0])
            y_dist= abs(q[34][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [37,40,41,45,48,49,50,51,52,53,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[35][0][0]-q[i][0][0])
            y_dist= abs(q[35][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [39,42,43,47,50,51,52,53,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[36][0][0]-q[i][0][0])
            y_dist= abs(q[36][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [39,42,43,47,50,51,52,53,54,55,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[37][0][0]-q[i][0][0])
            y_dist= abs(q[37][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [44,52,53,54,55,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[38][0][0]-q[i][0][0])
            y_dist= abs(q[38][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [44,45,52,53,54,55,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[39][0][0]-q[i][0][0])
            y_dist= abs(q[39][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [42,43,50,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[40][0][0]-q[i][0][0])
            y_dist= abs(q[40][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [43,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[41][0][0]-q[i][0][0])
            y_dist= abs(q[41][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [44,45,48,52,53,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[42][0][0]-q[i][0][0])
            y_dist= abs(q[42][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [45,48,49,53,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[43][0][0]-q[i][0][0])
            y_dist= abs(q[43][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [46,47,50,54,55,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[44][0][0]-q[i][0][0])
            y_dist= abs(q[44][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [47,50,51,55,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[45][0][0]-q[i][0][0])
            y_dist= abs(q[45][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [52,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[46][0][0]-q[i][0][0])
            y_dist= abs(q[46][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [52,53,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[47][0][0]-q[i][0][0])
            y_dist= abs(q[47][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [50,51,58,59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[48][0][0]-q[i][0][0])
            y_dist= abs(q[48][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [51,59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[49][0][0]-q[i][0][0])
            y_dist= abs(q[49][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [52,53,56,60,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[50][0][0]-q[i][0][0])
            y_dist= abs(q[50][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [53,56,57,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[51][0][0]-q[i][0][0])
            y_dist= abs(q[51][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [54,55,58,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[52][0][0]-q[i][0][0])
            y_dist= abs(q[52][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [56,58,59,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[53][0][0]-q[i][0][0])
            y_dist= abs(q[53][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [60] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[54][0][0]-q[i][0][0])
            y_dist= abs(q[54][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [60,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[55][0][0]-q[i][0][0])
            y_dist= abs(q[55][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [58,59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[56][0][0]-q[i][0][0])
            y_dist= abs(q[56][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[57][0][0]-q[i][0][0])
            y_dist= abs(q[57][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [60,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[58][0][0]-q[i][0][0])
            y_dist= abs(q[58][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[59][0][0]-q[i][0][0])
            y_dist= abs(q[59][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[60][0][0]-q[i][0][0])
            y_dist= abs(q[60][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));
    for i in [63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[61][0][0]-q[i][0][0])
            y_dist= abs(q[61][0][1]-q[i][0][1])
            parsum= parsum +min(x_dist,abs(num_proc-x_dist))+min(y_dist,abs(num_proc-y_dist));

    average =parsum/ns
    return parsum,ns,average

def grid32(q,num_proc):
    parsum=0
    ns=558
    for i in range(len(q)):
        if q[i]==[]:
            q[i]=[[0,0,0]]
    
    for i in [2,3,10,11,16,17,18,19,24,25,26,27]  :
        if q[i]!=[[0,0,0]]:    
            x_dist= abs(q[0][0][0]-q[i][0][0])
            y_dist= abs(q[0][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [3,11,16,17,18,19,24,25,26,27]  :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[1][0][0]-q[i][0][0])
            y_dist= abs(q[1][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist

    for i in [4,5,8,12,13,16,17,18,19,20,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[2][0][0]-q[i][0][0])
            y_dist= abs(q[2][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [5,8,9,13,16,17,18,19,20,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[3][0][0]-q[i][0][0])
            y_dist= abs(q[3][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [6,7,10,14,15,18,19,20,21,22,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[4][0][0]-q[i][0][0])
            y_dist= abs(q[4][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [7,10,11,15,18,19,20,21,22,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[5][0][0]-q[i][0][0])
            y_dist= abs(q[5][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [12, 20,21,22,23,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[6][0][0]-q[i][0][0])
            y_dist= abs(q[6][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [12,13,20,21,22,23,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[7][0][0]-q[i][0][0])
            y_dist= abs(q[7][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [10,11,18,19,24,25,26,27] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[8][0][0]-q[i][0][0])
            y_dist= abs(q[8][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [11,19,24,25,26,27] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[9][0][0]-q[i][0][0])
            y_dist= abs(q[9][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [12,13,16,20,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[10][0][0]-q[i][0][0])
            y_dist= abs(q[10][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [13,16,17,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[11][0][0]-q[i][0][0])
            y_dist= abs(q[11][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [14,15,18,22,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[12][0][0]-q[i][0][0])
            y_dist= abs(q[12][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [15,18,19,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[13][0][0]-q[i][0][0])
            y_dist= abs(q[13][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [20,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[14][0][0]-q[i][0][0])
            y_dist= abs(q[14][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [20,21,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[15][0][0]-q[i][0][0])
            y_dist= abs(q[15][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [18,19,26,27,32,33,34,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[16][0][0]-q[i][0][0])
            y_dist= abs(q[16][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [19,27,32,33,34,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[17][0][0]-q[i][0][0])
            y_dist= abs(q[17][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [20,21,28,29,24,32,33,34,35,36,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[18][0][0]-q[i][0][0])
            y_dist= abs(q[18][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [21,24,25,29,32,33,34,35,36,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[19][0][0]-q[i][0][0])
            y_dist= abs(q[19][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [22,23,26,30,31,34,35,36,37,38,39,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[20][0][0]-q[i][0][0])
            y_dist= abs(q[20][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [23,26,27,31,34,35,36,37,38,39,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[21][0][0]-q[i][0][0])
            y_dist= abs(q[21][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [28,36,37,38,39,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[22][0][0]-q[i][0][0])
            y_dist= abs(q[22][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [28,29,36,37,38,39,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[23][0][0]-q[i][0][0])
            y_dist= abs(q[23][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [26,27,34,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[24][0][0]-q[i][0][0])
            y_dist= abs(q[24][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [27,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[25][0][0]-q[i][0][0])
            y_dist= abs(q[25][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [28,29,32,36,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[26][0][0]-q[i][0][0])
            y_dist= abs(q[26][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [29,32,33,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[27][0][0]-q[i][0][0])
            y_dist= abs(q[27][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [30,31,34,38,39,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[28][0][0]-q[i][0][0])
            y_dist= abs(q[28][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [31,34,35,37,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[29][0][0]-q[i][0][0])
            y_dist= abs(q[29][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [36,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[30][0][0]-q[i][0][0])
            y_dist= abs(q[30][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [36,37,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[31][0][0]-q[i][0][0])
            y_dist= abs(q[31][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [34,35,42,43,46,47,48,49,50,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[32][0][0]-q[i][0][0])
            y_dist= abs(q[32][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [35,43,48,49,50,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[33][0][0]-q[i][0][0])
            y_dist= abs(q[33][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [36,37,40,44,45,48,49,50,51,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[34][0][0]-q[i][0][0])
            y_dist= abs(q[34][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [37,40,41,45,48,49,50,51,52,53,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[35][0][0]-q[i][0][0])
            y_dist= abs(q[35][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [39,42,43,47,50,51,52,53,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[36][0][0]-q[i][0][0])
            y_dist= abs(q[36][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [39,42,43,47,50,51,52,53,54,55,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[37][0][0]-q[i][0][0])
            y_dist= abs(q[37][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [44,52,53,54,55,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[38][0][0]-q[i][0][0])
            y_dist= abs(q[38][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [44,45,52,53,54,55,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[39][0][0]-q[i][0][0])
            y_dist= abs(q[39][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [42,43,50,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[40][0][0]-q[i][0][0])
            y_dist= abs(q[40][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [43,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[41][0][0]-q[i][0][0])
            y_dist= abs(q[41][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [44,45,48,52,53,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[42][0][0]-q[i][0][0])
            y_dist= abs(q[42][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [45,48,49,53,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[43][0][0]-q[i][0][0])
            y_dist= abs(q[43][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [46,47,50,54,55,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[44][0][0]-q[i][0][0])
            y_dist= abs(q[44][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [47,50,51,55,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[45][0][0]-q[i][0][0])
            y_dist= abs(q[45][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [52,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[46][0][0]-q[i][0][0])
            y_dist= abs(q[46][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [52,53,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[47][0][0]-q[i][0][0])
            y_dist= abs(q[47][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [50,51,58,59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[48][0][0]-q[i][0][0])
            y_dist= abs(q[48][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [51,59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[49][0][0]-q[i][0][0])
            y_dist= abs(q[49][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [52,53,56,60,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[50][0][0]-q[i][0][0])
            y_dist= abs(q[50][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [53,56,57,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[51][0][0]-q[i][0][0])
            y_dist= abs(q[51][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [54,55,58,62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[52][0][0]-q[i][0][0])
            y_dist= abs(q[52][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [56,58,59,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[53][0][0]-q[i][0][0])
            y_dist= abs(q[53][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [60] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[54][0][0]-q[i][0][0])
            y_dist= abs(q[54][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [60,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[55][0][0]-q[i][0][0])
            y_dist= abs(q[55][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [58,59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[56][0][0]-q[i][0][0])
            y_dist= abs(q[56][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [59] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[57][0][0]-q[i][0][0])
            y_dist= abs(q[57][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [60,61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[58][0][0]-q[i][0][0])
            y_dist= abs(q[58][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [61] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[59][0][0]-q[i][0][0])
            y_dist= abs(q[59][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [62,63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[60][0][0]-q[i][0][0])
            y_dist= abs(q[60][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist
    for i in [63] :
        if q[i]!=[[0,0,0]]:
            x_dist= abs(q[61][0][0]-q[i][0][0])
            y_dist= abs(q[61][0][1]-q[i][0][1])
            parsum=parsum+x_dist+y_dist

    average =parsum/ns
    return parsum,ns,average

    
def hypercube32(q,num_proc):
    parsum=0
    ns=558
    for i in range(len(q)):
        if q[i]==[]:
            q[i]=[[0,0,0]]
    
    for i in [2,3,10,11,16,17,18,19,24,25,26,27]  :
        if q[i]!=[[0,0,0]]:    
            dist = bin(q[0][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [3,11,16,17,18,19,24,25,26,27]  :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[1][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)

    for i in [4,5,8,12,13,16,17,18,19,20,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[2][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [5,8,9,13,16,17,18,19,20,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[3][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [6,7,10,14,15,18,19,20,21,22,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[4][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [7,10,11,15,18,19,20,21,22,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
           dist = bin(q[5][0][2]^q[i][0][2])[2:]
           for j in dist:
                parsum=parsum+int(j)
    for i in [12, 20,21,22,23,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[6][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [12,13,20,21,22,23,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[7][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [10,11,18,19,24,25,26,27] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[8][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [11,19,24,25,26,27] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[9][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [12,13,16,20,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[10][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [13,16,17,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[11][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [14,15,18,22,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[12][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [15,18,19,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[13][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [20,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[14][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [20,21,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[15][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [18,19,26,27,32,33,34,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[16][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [19,27,32,33,34,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[17][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [20,21,28,29,24,32,33,34,35,36,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[18][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [21,24,25,29,32,33,34,35,36,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[19][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [22,23,26,30,31,34,35,36,37,38,39,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[20][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [23,26,27,31,34,35,36,37,38,39,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[21][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [28,36,37,38,39,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[22][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [28,29,36,37,38,39,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[23][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [26,27,34,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[24][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [27,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[25][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [28,29,32,36,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
           dist = bin(q[26][0][2]^q[i][0][2])[2:]
           for j in dist:
                parsum=parsum+int(j)
    for i in [29,32,33,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
           dist = bin(q[27][0][2]^q[i][0][2])[2:]
           for j in dist:
                parsum=parsum+int(j)
    for i in [30,31,34,38,39,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[28][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [31,34,35,37,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
           dist = bin(q[29][0][2]^q[i][0][2])[2:]
           for j in dist:
                parsum=parsum+int(j)
    for i in [36,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[30][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [36,37,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[31][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [34,35,42,43,46,47,48,49,50,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[32][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [35,43,48,49,50,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[33][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [36,37,40,44,45,48,49,50,51,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[34][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [37,40,41,45,48,49,50,51,52,53,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[35][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [39,42,43,47,50,51,52,53,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[36][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [39,42,43,47,50,51,52,53,54,55,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[37][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [44,52,53,54,55,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[38][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [44,45,52,53,54,55,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[39][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [42,43,50,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[40][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [43,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[41][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [44,45,48,52,53,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[42][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [45,48,49,53,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[43][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [46,47,50,54,55,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[44][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [47,50,51,55,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[45][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [52,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[46][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [52,53,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[47][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [50,51,58,59] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[48][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [51,59] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[49][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [52,53,56,60,61] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[50][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [53,56,57,61] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[51][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [54,55,58,62,63] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[52][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [56,58,59,63] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[53][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [60] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[54][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [60,61] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[55][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [58,59] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[56][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [59] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[57][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [60,61] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[58][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [61] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[59][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [62,63] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[60][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    for i in [63] :
        if q[i]!=[[0,0,0]]:
            dist = bin(q[61][0][2]^q[i][0][2])[2:]
            for j in dist:
                parsum=parsum+int(j)
    average =parsum/ns
    return parsum,ns,average

def quadtree32(q,num_proc):
    parsum=0
    ns=558
    num_dig=math.ceil(math.log(num_proc,2))
    for i in range(len(q)):
        if q[i]==[]:
            q[i]=[[0,0,0]]
    
    for i in [2,3,10,11,16,17,18,19,24,25,26,27]  :
        if q[i]!=[[0,0,0]]:
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
            
            
                
    for i in [3,11,16,17,18,19,24,25,26,27]  :
        if q[i]!=[[0,0,0]]:
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
            
            
                

    for i in [4,5,8,12,13,16,17,18,19,20,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
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
            
            
                
    for i in [5,8,9,13,16,17,18,19,20,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
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
            
            
                
    for i in [6,7,10,14,15,18,19,20,21,22,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
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
            
            
                
    for i in [7,10,11,15,18,19,20,21,22,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
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
           
            
                
    for i in [12, 20,21,22,23,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
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
            
                
    for i in [12,13,20,21,22,23,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
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
            
                
    for i in [10,11,18,19,24,25,26,27] :
        if q[i]!=[[0,0,0]]:
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
            
                
    for i in [11,19,24,25,26,27] :
        if q[i]!=[[0,0,0]]:
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
            
                
    for i in [12,13,16,20,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
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
            
                
    for i in [13,16,17,21,24,25,26,27,28,29] :
        if q[i]!=[[0,0,0]]:
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
                
    for i in [14,15,18,22,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
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
            
                
    for i in [15,18,19,23,26,27,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
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
            
                
    for i in [20,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[14][0][2])[2:]
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
            
                
    for i in [20,21,28,29,30,31] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[15][0][2])[2:]
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
            
                
    for i in [18,19,26,27,32,33,34,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[16][0][2])[2:]
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
            
                
    for i in [19,27,32,33,34,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[17][0][2])[2:]
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
            
                
    for i in [20,21,28,29,24,32,33,34,35,36,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[18][0][2])[2:]
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
            
                
    for i in [21,24,25,29,32,33,34,35,36,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[19][0][2])[2:]
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
            
                
    for i in [22,23,26,30,31,34,35,36,37,38,39,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[20][0][2])[2:]
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
            
                
    for i in [23,26,27,31,34,35,36,37,38,39,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[21][0][2])[2:]
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
            
                
    for i in [28,36,37,38,39,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[22][0][2])[2:]
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
            
                
    for i in [28,29,36,37,38,39,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[23][0][2])[2:]
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
            
                
    for i in [26,27,34,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[24][0][2])[2:]
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
            
                
    for i in [27,35,40,41,42,43] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[25][0][2])[2:]
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
            
                
    for i in [28,29,32,36,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
           leafpos1=bin(q[26][0][2])[2:]
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
            
                
    for i in [29,32,33,37,40,41,42,43,44,45] :
        if q[i]!=[[0,0,0]]:
           leafpos1=bin(q[27][0][2])[2:]
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
            
                
    for i in [30,31,34,38,39,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[28][0][2])[2:]
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
            
                
    for i in [31,34,35,37,42,43,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
           leafpos1=bin(q[29][0][2])[2:]
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
            
                
    for i in [36,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[30][0][2])[2:]
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
            
                
    for i in [36,37,44,45,46,47] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[31][0][2])[2:]
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
            
                
    for i in [34,35,42,43,46,47,48,49,50,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[32][0][2])[2:]
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
            
                
    for i in [35,43,48,49,50,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[33][0][2])[2:]
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
            
                
    for i in [36,37,40,44,45,48,49,50,51,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[34][0][2])[2:]
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
            
                
    for i in [37,40,41,45,48,49,50,51,52,53,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[35][0][2])[2:]
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
            
                
    for i in [39,42,43,47,50,51,52,53,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[36][0][2])[2:]
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
            
                
    for i in [39,42,43,47,50,51,52,53,54,55,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[37][0][2])[2:]
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
            
                
    for i in [44,52,53,54,55,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[38][0][2])[2:]
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
            
                
    for i in [44,45,52,53,54,55,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[39][0][2])[2:]
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
            
                
    for i in [42,43,50,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[40][0][2])[2:]
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
            
                
    for i in [43,51,56,57,58,59] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[41][0][2])[2:]
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
            
                
    for i in [44,45,48,52,53,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[42][0][2])[2:]
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
            
                
    for i in [45,48,49,53,56,57,58,59,60,61] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[43][0][2])[2:]
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
            
                
    for i in [46,47,50,54,55,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[44][0][2])[2:]
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
            
                
    for i in [47,50,51,55,58,59,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[45][0][2])[2:]
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
            
                
    for i in [52,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[46][0][2])[2:]
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
            
                
    for i in [52,53,60,61,62,63] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[47][0][2])[2:]
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
            
                
    for i in [50,51,58,59] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[48][0][2])[2:]
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
            
                
    for i in [51,59] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[49][0][2])[2:]
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
            
                
    for i in [52,53,56,60,61] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[50][0][2])[2:]
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
            
                
    for i in [53,56,57,61] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[51][0][2])[2:]
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
            
                
    for i in [54,55,58,62,63] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[52][0][2])[2:]
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
            
                
    for i in [56,58,59,63] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[53][0][2])[2:]
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
            
                
    for i in [60] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[54][0][2])[2:]
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
            
                
    for i in [60,61] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[55][0][2])[2:]
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
            
                
    for i in [58,59] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[56][0][2])[2:]
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
            
                
    for i in [59] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[57][0][2])[2:]
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
            
                
    for i in [60,61] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[58][0][2])[2:]
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
            
                
    for i in [61] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[59][0][2])[2:]
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
            
                
    for i in [62,63] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[60][0][2])[2:]
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
            
                
    for i in [63] :
        if q[i]!=[[0,0,0]]:
            leafpos1=bin(q[61][0][2])[2:]
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
            
                
    average =parsum/ns
    return parsum,ns,average
    
