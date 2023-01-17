"""
Question 5
give bonus marks of 2 for the candidates whose age is greater than 34

scores = [[1,32,80,],[2,30,62],[3,35,67],[4,37,89]] --> [number,age,mark]
""""

scores = [[1,32,80,],[2,30,62],[3,35,67],[4,37,89]]

new_scores = list(map(lambda x:[x[0],x[1],x[2]+2] if x[1]>34 else [x[0],x[1],x[2]],scores))
print(new_scores)
