#String methods assignment : 25/11/2022

a = "string methods assignment"
b = "STRING methods assignment"
c = "My name is Ståle"
d = "I have {dollar:.3f} dollars with me"
e = "alpha123"
f = "125465"
g = "  "
h = "String Methods Assignment"
i = ("String","Methods","Assignment")
j = "   abcd   "
k = "string \nmethods \nassignment"


capitalize()	Converts the first character to upper case
    print(a.capitalize())
    >>> String methods assignment
    
casefold()	Converts string into lower case
    print(b.casefold())
    >>> string methods assignment

center()	Returns a centered string
    print(a.center(20))
    >>>         string methods assignment

count()	Returns the number of times a specified value occurs in a string
    print(a.count("s"))
    >>> 4

encode()	Returns an encoded version of the string
    print(c.encode())
    >>> b'My name is St\xc3\xa5le'

endswith()	Returns true if the string ends with the specified value
    print(a.endswith("!"))
    >>> False
    print(a.endswith("t"))
    >>> True

find()	Searches the string for a specified value and returns the position of where it was found
    print(a.find("t"))
    >>> 1
    
format()	Formats specified values in a string
    print(d.format(dollar = 45.10))
    >>> I have 45.100 dollars with me

index()	        Searches the string for a specified value and returns the position of where it was found
    print(a.index("t"))
    >>> 1

isalnum()	Returns True if all characters in the string are alphanumeric
    print(a.isalnum())
    >>> False
    print(e.isalnum())
    >>> True

isalpha()	Returns True if all characters in the string are in the alphabet
    print(a.isalpha())
    >>> False
    print(e.isalpha())
    >>> False
    
isdecimal()	Returns True if all characters in the string are decimals (0-9)
    print(f.isdecimal())
    >>> True

isdigit()	Returns True if all characters in the string are digits
    print(f.isdigit())
    >>> True

isidentifier()	Returns True if the string is a valid identifier (A valid identifier cannot start with a number, or contain any spaces.)
    print(a.isidentifier())
    >>> False
    print(e.isidentifier())
    >>> True

islower()	Returns True if all characters in the string are lower case
    print(a.islower())
    >>> True

isnumeric()	Returns True if all characters in the string are numeric
    print(f.isnumeric())
    >>> True
    
isprintable()	Returns True if all characters in the string are printable
    print(e.isprintable())
    >>> True

isspace()	Returns True if all characters in the string are whitespaces
    print(g.isspcae())
    >>> True

istitle()	Returns True if the string follows the rules of a title
    print(h.istitle())
    >>> True
    
isupper()	Returns True if all characters in the string are upper case
    print(h.isupper())
    >>> False
    
join()	Converts the elements of an iterable into a string
    print(",".join(i))
    >>> String,Methods,Assignment

lower()	        Converts a string into lower case
    print(b.lower())
    >>> string methods assignment
    
lstrip()	Returns a left trim version of the string
    print("string" ,j.lstrip(),"string")
    >>> string abcd    string
    
replace()	Returns a string where a specified value is replaced with a specified value
    print(a.replace("string" , "text"))
    >>> text methods assignment
    
rfind()	        Searches the string for a specified value and returns the last position of where it was found
    print(c.rfind("is"))
    >>> 8

rsplit()	Splits the string at the specified separator, and returns a list
    print(a.rsplit(" "))
    >>> ['string', 'methods', 'assignment']

rstrip()	Returns a right trim version of the string
    print("string" ,j.rstrip(),"string")
    >>> string    abcd string
    
split()	        Splits the string at the specified separator, and returns a list
    print(a.split())
    >>> ['string', 'methods', 'assignment']
        
splitlines()	Splits the string at line breaks and returns a list
    print(k.splitlines())
    >>> ['string ', 'methods ', 'assignment']
    
startswith()	Returns True if the string starts with the specified value
    print(a.startswith("string"))
    >>> True

strip()	        Returns a trimmed version of the string
    print("string" ,j.strip(),"string")
    >>> string abcd string
    
title()	        Converts the first character of each word to upper case
    print(a.title())
    >>> String Methods Assignment
    
upper()	        Converts a string into upper case
    print(a.upper())
    >>> STRING METHODS ASSIGNMENT
