
l = ['AGGAAAAGAG','CGAGGCCAAC','GACAAAACCG','GCGACGCAGA','AACAGCGCAG','GCC']
import numpy as np


def cmsublen(x,y):
    result = 0
    l= np.zeros([len(x)+1,len(y)+1],dtype='int64')
    
    for i in range(0,len(x)+1):
        for j in range(0,len(y)+1):
            if i==0 or j==0:
                l[i][j] = 0
            elif x[i-1]==y[j-1]:
                l[i][j] = l[i-1][j-1] + 1
                result = max(result,l[i][j])
            else:
                l[i][j]=0

    return result
                
prob = []    
for i in range(0,len(l)-1):
    cm  = cmsublen(l[i],l[len(l)-1])
    print("Comm-len",cm,l[i],l[len(l)-1])
    prob.append(cm/len(l[len(l)-1]))

rank =1
for i,j in enumerate(prob):
    if i==0:
        print("Person #0:"+str(rank))
    elif j==prob[i-1]:
        print("Person #"+str(i)+":"+str(rank))
    else:
        print("Person #"+str(i)+":"+str(rank+1))
        rank = rank + 1

        
