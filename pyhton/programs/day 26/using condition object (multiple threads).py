## inter thread communication
## using condition object (multiple threads)

from threading import*
from time import sleep

data={}
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    
con = Condition()

def temp():
    con.acquire()
    
    for day in days:
        tmp = float(input(f"enter temperature for {day} : "))
        data[day] = tmp
    print(data)
    
    con.notify_all()
    con.release()

def max_temp():
    con.acquire()
    #con.wait()
    values = list(data.values())
    keys = list(data.keys())
    max_tmp = max(values)
    print("The max temp is in ",keys[values.index(max_tmp)])
    con.release()
    

def avg_temp():
    con.acquire()
    values = list(data.values())

    sum = 0
    for i in values:
        sum += i
    print("The average temperature =",round(sum/7))
    
    con.release()
    

t1 = Thread(target = temp)
t2 = Thread(target = max_temp)
t3 = Thread(target = avg_temp)

t1.start()
t2.start()
t3.start()
