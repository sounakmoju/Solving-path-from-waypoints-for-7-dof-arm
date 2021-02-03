import itertools
import random
import numpy as np
import scipy.sparse as sps
f={0:[0,1,2,3],#waypoitnts are the keys and key values are the inverse kinematics solution
1:[4,5,6,7],2:[8,9,10,11]}

        
k1=[]
k=[]

for key in f:
    k=list(itertools.combinations(f[key],2))
    for i in k:
        k1.append(list(i))

j1=[]
for key in f:
    j1.append(key)
#print(j)
l=[]
l1=[]
for i in range(len(j1)-1):
    for k in f[j1[i]]:
        for h in f[j1[i+1]]:
            l.append((k,h))
for i in l:
    l1.append(list(i))    
#print(l1)
combo_list=k1+l1

x=0.7
for i in combo_list:
    k=random.uniform(0, 1)
    if k<x:
        i.append(1)
    else:
        i.append(0)
#print(combo_list)
A=np.array(combo_list)
#print(A)
#print(A.shape)
i,j,w=A[:,0],A[:,1],A[:,2]
dim=tuple(A.max(axis=0)[:2]+1)

coo = sps.coo_matrix((A[:, 2], (A[:, 0], A[:, 1])), shape=dim,
                        dtype=A.dtype)
B=(coo).todense()
print(coo)
k=(np.amax(A.shape))
k1=(np.amin(A.shape))
print(B.shape)
print(B)
x=np.array(B)
rta = np.array([0,0,0,0,0,0,0,0,0,0,0,0])
B1= np.vstack ((x,rta))
print(B1.shape)

m=(len(j1))
W=np.zeros((m,m))

for i in range(m-1):
    W[i,i+1]=1
    #W[i+1,i]=1
print(W[1,2])
v1=[]
for i in j1:
    for j in f[i]:
        v1.append((i,j))
#print(v1)
v2=[]
for i in range(len(j1)-1):
    for j in f[i+1]:
        v2.append((i,j))
#print(v2)
com_v=v1+v2
print(com_v)
v_u=[]
v_u_1=[]
print(B[10,11])
#this is a very brut way of O(n2),please do it nlogn way I just wanted to show the algo

for i in com_v:
    for j in com_v:
        if i[0]==j[0]& i[1]!=j[1]:
            if B1[i[1],j[1]]==1:
                v_u.append((i,j,1))
            else:
                v_u.append((i,j,0))
        elif i[0]!=j[0]& i[1]==j[1]:
            if W[i[0],j[0]]==1:
                v_u.append((i,j,1))
            else:
                v_u.append((i,j,0))
        elif i[0]!=j[0]& i[1]!=j[1]:
            if W[i[0],j[0]]==1 & B1[i[1],j[1]]==1:
                v_u.append((i,j,1))
            else:
                v_u.append((i,j,1))
        else:
            v_u.append((i,j,0))
#for i in com_v:
    #print(i[0])
#print(v_u)
print(v_u)
B12=[]
#B12=([v_u_1])

#for i in v_u_1:
    #B_12=list(i)
#print(B12)
    
#for i in v_u_1:
   # print(i[0])
#this v_u_1 graph information is cross product graph and cost of each node is dist(u1,Fk(v))
   #and cost of an edge is max(cost(u),cost(v))where u,v are nodes, then a bottle neck cost is determined from the sparse djshetras algorithm
    


    

        
    
