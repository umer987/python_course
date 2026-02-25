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

#find the gratest element from list
l=[20,22,24,26,28,30,1000]
greatest =0
for i in range(0,len(l),1):
    if l[i]>greatest:
        greatest = l[i]

print("THE GRATEST ELEMENT IS:- ",greatest)