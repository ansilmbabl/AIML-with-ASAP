#WAP to read every fifth charactor in a file and print it as a string.

f=open("D:\\AIML\\pyhton\\programs\\day 9\\file handling\\new file.txt","rb")
s=f.read(0)
print(s)

s1=""

while(f.read() != eof):
    f.seek(5,1)
    s1 += f.read(1).decode("utf-8")
print(s1)


t=""
    
if f.read() != eof:
    f.seek(5,1)
    t+= f.read(1).decode("utf-8")
else:
print(t)
