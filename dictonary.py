#dictonary simple syntax it is like table in sql
# student = {1:"umer",2:"b",3:"c"}
# print(student)

#make student record 
# student={"name":"umer", "father_name":"muhammad shakir", "age":"21"}
# print(student["name"])

#traverse dictonary through loop
# student = {1:"umer",2:"b",3:"c"}

# for i in range(1,len(student)+1,1):
#     print(student[i])

#crud on dictonary
# student = {1:"umer",2:"b",3:"c"}
#student[2]="abc" #updating
#del student[3] #deleting
#print(student[2]) #reading
#student[4] ="cba" # creating if you [56] anonymus index python will accept this and and make this index in new index into dictonary
# print(student)

#traverse through loop advance

# d ={10:1,20:2,30:3,40:4}
# for i in d:
#     #print(i) #it will only print key but we want values
#     print(d[i])

#write a python script to merger 2 python dictonary
# student={1:"umer",2:"abc",3:"dbc",4:"poi"}
# student2 = {5:"umer_Shakir",6:"abcnnn",7:"dbcnnn",8:"iopoi"}
# new=student.copy()
# new.update(student2)
# print(new)


#Write a Python program to sum all the values in a dictionary
# d ={10:1,20:2,30:3,40:4}
# sum=0
# for i in d:
#     sum += d[i]
# print(sum)

#Count the frequency of each element
d ={1:1,2:2,3:3,4:4,5:4,6:4,7:4,8:4,9:4,10:2}
number = int(input("ENTER THE NUMBER"))
