#question is find the positive and negative element in list
# l = [-1,2,-9,5,-12,6,-22]
# n=[]
# p=[]
# for i in range(0,len(l),1):
#     if l[i]<0:
#         n.append(l[i])
#     else:
#         p.append(l[i])
# print("NEGATIVE ELEMENTS ARE:- ",n)
# print("POSITVE ELEMENTS ARE:- ", p)


# #solve mean for an givin list
# l=[20,22,24,26,28,30]
# total=0
# for i in range(0,len(l),1):
#     total+=l[i]
# mean= total/len(l)
# print("THE MEAN OF THE GIVIN LIST IS:- ", mean)

#find the gratest element from list also index 
# l=[20,22,24,26,28,30]
# greatest =l[0]

# for i in range(0,len(l),1):
#     if l[i]>greatest:
#         greatest = l[i]
# index = l.index(greatest)
# print("THE GRATEST ELEMENT AT THE IS:- ",greatest," AT THE INDEX OF:- ",index)


#find the 2nd gratest element from list also index 
l=[20,22,24,26,28,30]
greatest2 =l[0]
great=0
for i in range(0,len(l),1):
    if l[i]>greatest2:
        greatest2 = l[i]

l.remove(greatest2)
for i in range(0,len(l),1):
    if l[i]>great:
        great = l[i]


