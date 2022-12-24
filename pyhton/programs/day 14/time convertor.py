#Write a class Timeconverter that recieve time in seconds ,at the object creation
#second_to_minutes() --> 130 --> 2 min 10 sec
#second to hours()-->130--> 0 hrs 2 min 10 sec
#second to days()-->130-->0 days 0 hrs 2 min 10 se



class time:
    def __init__(self):
        self.tim = int(input("enter seconds: "))

    def minute(self):
        m = self.tim // 60
        s = self.tim % 60
        return m,s
        

    def hour(self):
        h = self.tim // (60*60)
        m = (self.tim - h*60*60) // 60
        s = (self.tim - m*60 - h*60*60) % 60
        return h,m,s
    
    def day(self):
        d = self.tim // (60*60*24)
        h = (self.tim - d*24*60*60) // (60*60)
        m = (self.tim - h*60*60 - d*24*60*60) // 60
        s = (self.tim - m*60 - h*60*60 - d*24*60*60) % 60
        return d,h,m,s


time1 = time()
m,s = time1.minute()
print(f"{m} minutes {s} seconds")
h,m,s = time1.hour()
print(f"{h} hours {m} minutes {s} seconds")
d,h,m,s = time1.day()
print(f"{d} days {h} hours {m} minutes {s} seconds")
