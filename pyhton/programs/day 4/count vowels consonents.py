#WAP to get a string from the user and count the vowel and consonents

n=input("enter the sentence: ")

v=0
c=0

for i in n:
    if i in "AEIOUaeiou":
        v+=1
    else:
        c+=1

print(f"vowels = {v} and consonents = {c}")
