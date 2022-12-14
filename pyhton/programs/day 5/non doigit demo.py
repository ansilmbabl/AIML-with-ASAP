l = []
print("Enter values and to stop type a non digit variable")
while True:
    n = input()
    if n.isdigit()!=True:
            break
    else:
        l.append(int(n))
print(l)
