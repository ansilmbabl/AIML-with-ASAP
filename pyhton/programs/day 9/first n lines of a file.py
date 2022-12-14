#WAP to print first n lines of a file.


##import os
##os.chdir("D:\\AIML\\pyhton\\programs\\day 9\\file handling")
##f=open("D:\\AIML\\pyhton\\programs\\day 9\\file handling\\new file.txt","r")
##
##s=f.readlines()
##print(s)

# WAP to read n lines from one file and copy to another file

f=open("D:\\AIML\\pyhton\\programs\\day 9\\file handling\\new file.txt","r")
s=f.readlines()
print(s)

n=int(input("number of lines : "))
if n > len(s):
    print("limit exceeds")
else:
    for i in range(n):
        print(s[i])
