#to read file and open file
# p =open(r"C:\Users\UMER QURESHI\Desktop\abc.txt")
# print(p.read())

#create file
# r =open('azc.txt','w')
# r.write("im SYED MUHAMMAD UMER SHAKIR")
# r.close()

# #adding content in file
# r =open('azc.txt','w')
# r.write("im SYED MUHAMMAD UMER SHAKIR")
# r.close()


# w override the content of file but a append content in existing file contnt 
r =open("azc.txt", 'a' )
r.write("im  SYED MUHAMMAD UMER SHAKIR")
r.close()