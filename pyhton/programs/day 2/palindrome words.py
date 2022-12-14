#WAP palindrome words

a=input("enter the word : ")

if a == a[::-1]:
    print("it is a palindrome")
else:
    print("not a palindrome")

