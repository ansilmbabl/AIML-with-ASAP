#apple
##1 a vowel
##2 p consonent

a= input("enter something : ")

for i in range(len(a)):
    if a[i] in "aeiouAEIOU":
        print (i+1, ",", a[i],",", " vowel")
    else:
        print (i+1, ",", a[i],",", " consonent")

##for i in a:
##    
##for b in range(len(a)):
