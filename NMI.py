from math import log
import math


                     
#------------------------begin main--------------------------    
nodes=10
# create an array for testing_method and Refrence method
# index is node id and value is group membership
Ref_P=[None]*(nodes+1)
test_P=[None]*(nodes+1)

#input format first number is node second group

# open file and fill test_P
infile= open("partition.csv", "r")
for line in infile:
    node_assignment=line.split(",")
    test_P[int(node_assignment[0])]= int(node_assignment[1])

# open file and fill Ref_P
infile= open("truth.csv", "r")
for line in infile:
    node_assignment=line.split(",")
    Ref_P[int(node_assignment[0])]= int(node_assignment[1])

#build a list of communities in test_P
X_i=[]
for x in range(0, nodes):
    if test_P[x]!=None:
        if test_P[x] in X_i: 
            Do="nothing" 
        else:
            X_i.append(test_P[x])
            
#build a list of communities in Ref_P
Y_j=[]
for y in range(0, nodes):
    if Ref_P[y]!=None:
        if Ref_P[y] in Y_j:
            Do="nothing" 
        else:
            Y_j.append(Ref_P[y])   
 
    
    """ 
NMI=             ∑∑P_ij*log[(n*P_ij)/(n_xi*n_yj)]
             ----------------------------------------
       [∑n_xi*log((n_xi)/nodes) * ∑n_yj*log((n_yj)/nodes)]^(1/2)



In the code below this formula is divided int0 3 varables 
===>                 num
          --------------------------
            (den_a   *   den_b)^1/2

"""

#  ∑∑P_ij*log[(n*P_ij)/(n_xi*n_yj)]
num=0.0
for i in X_i:
    for j in Y_j:
        P_ij=0
        n_xi=0
        n_yj=0
        for index in range(0, nodes+1):
            if test_P[index]==i:
                n_xi+=1
                if Ref_P[index]==j:
                    P_ij+=1
            if Ref_P[index]==j:
                n_yj+=1
        if P_ij!=0:
            num+=P_ij*math.log((nodes*P_ij)/(n_xi*n_yj))
        



# ∑n_xi*log((n_xi)/nodes)
den_a=0
for k in X_i:
    n_xi=0
    for index in range(0, nodes+1):
        if test_P[index]==k:
            n_xi+=1
    den_a+= n_xi*log(n_xi/nodes)
 
    
    
# ∑n_yj*log((n_yj)/nodes)
den_b=0       
for l in Y_j:
    n_yj=0
    for index in range(0, nodes+1):
        if Ref_P[index]==l:
            n_yj+=1
    den_b+= n_xi*log(n_xi/nodes)
                
# [∑n_xi*log((n_xi)/nodes) * ∑n_yj*log((n_yj)/nodes)]^(1/2)
den=(den_a*den_b)**.5


NMI=num/den

print (NMI)


