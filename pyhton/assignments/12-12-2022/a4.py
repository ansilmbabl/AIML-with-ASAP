
count=0

for x in range(1,1001):
    for y in range(x+1,1001):
        for z in range(y+1,1001):
            if x**2 + y**2 == z**2 :
                count += 1
                print(x,y,z)
print(f"totale count {count}")
