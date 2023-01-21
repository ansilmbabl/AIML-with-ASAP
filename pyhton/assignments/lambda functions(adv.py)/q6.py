#Write a Python program to check whether a given string is number or not using Lambda

c = lambda x:x.isalpha()
print("using isalpha()")
print(not (c("hsdgvfjdsh")))

"""
isdigit() will give false for float and negative values
hence it can't be used to check string is number or not
"""

print("\nusing isdigit()")
c = lambda x:x.isdigit()
print((c("1.23")))
print((c("-123")))
print((c("123")))
