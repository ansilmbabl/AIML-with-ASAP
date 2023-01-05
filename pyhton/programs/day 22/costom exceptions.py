
#costom exceptions (user defined exception class)

class underAgeException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

try:
    age = int(input("Enter you age: "))
    if age<18:
        raise underAgeException("The candidate is underage")
        
    else:
        print("Liscence can be issued.")
        
# except Exception as e:
# or
except underAgeException as e:    
    print(e)
