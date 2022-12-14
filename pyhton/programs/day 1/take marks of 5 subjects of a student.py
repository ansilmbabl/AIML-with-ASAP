#WAP to take marks of 5 subjects of a student
#calculate total marks and percentage ( Max mark is 100)

a = float(input("Mark of mathematics =" ))
b = float(input("Mark of science =" ))
c = float(input("Mark of chemistry =" ))
d = float(input("Mark of english =" ))
e = float(input("Mark of physics =" ))

t_mark = a+b+c+d+e
p_mark = t_mark/500*100

print (f"You have scored {t_mark} with a percentile of {p_mark}")
