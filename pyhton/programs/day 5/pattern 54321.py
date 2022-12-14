'''
1
21
321
4321
54321
'''

for i in range(1,6):
    for j in range(1,i+1):
        print(i-j+1,end=" ")
    print("\n")

"""
OR
"""

for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\n")
