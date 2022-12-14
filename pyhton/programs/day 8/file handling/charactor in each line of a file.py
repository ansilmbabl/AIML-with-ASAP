"""
file handling
"""

#WAP to count number of charactor in each line of a file

import os
f=open("D:\\AIML\\pyhton\\programs\\day 8\\file handling\\new file","r")
s=f.readlines()

for i in range (len(s)):
    print(f"number of charators in line{i+1} = {len(s[i])}")
