#WAP that calculates number of uppercase letters, lower case letters,
#total number of charators,total number of words in sentence

def low(x):
    y=0
    for i in x:
        if i.islower() == True:
            y+=1
    print("lowercase :",y)

def upper(x):
    y=0
    for i in x:
        if i.isupper() == True:
            y+=1
    print("uppercase :",y)

def total(x):
    print("total :",len(x))

def words(x):
    y=0
    for i in x:
        if i in ",. :;":
            y+=1
    print("words :",y)


x = input("enter the string : ")

low(x)
upper(x)
total(x)
words(x)
