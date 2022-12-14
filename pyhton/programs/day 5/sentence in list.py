#WAP to get a sentence string from the user. If the last charactor is not dot(.) then add dot to the string
#count the number of words(,space:;-.)
#seperate the words in the sentence and store in a list
#print list(do not use split fn)

s=input("enter the sentence : ")

if s[-1] != ".":
    s += "." 
print ("edited string = ",s)

c = 0
for i in s:
    if i in ":;.- ":
        c+=1
print ("number of words in the sentence = ",c)

temp =""
l=[]

for i in s:
    if i not in ":;.- ":
        temp += i
    else:
        l.append(temp)
        temp = ""
print(l)
