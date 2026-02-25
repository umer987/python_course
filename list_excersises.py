#question is find the positive and negative element in list
l = [-1,2,-9,5,-12,6,-22]
n=[]
p=[]
for i in range(0,len(l),1):
    if l[i]<0:
        n.append(l[i])
    else:
        p.append(l[i])
print("NEGATIVE ELEMENTS ARE:- ",n)
print("POSITVE ELEMENTS ARE:- ", p)

