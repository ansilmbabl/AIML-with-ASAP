##1.Accept a string and return a new string formed using the middle three characters. IF the input string is of even length, make a string of odd length as below
##• Add a period . at the end if it is not there
##• Otherwise remove the period . from the end

s=input("enter the string: ")

m=len(s)//2

if len(s)%2!=0:
    print(f"{s[m-1]}{s[m]}{s[m+1]}")
else:
    s+="."
    print(f"{s[m-1]}{s[m]}{s[m+1]}")
