# WAP to read n lines from one file and copy to another file

f=open("D:\\AIML\\pyhton\\programs\\day 9\\file handling\\new file.txt","r")
s=f.readlines()
print(s)
f.close()


n=int(input("number of lines : "))
if n > len(s):
    print("limit exceeds")
else:
    g=open("D:\\AIML\\pyhton\\programs\\day 9\\file handling\\new file2.txt","w")
    for i in range(n):
        g.write(s[i])
g.close()
        
##s2=g.readlines()
##print(s2)
##
##f.close()
##g.close()
