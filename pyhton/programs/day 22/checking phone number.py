#WAP tp take phone number and if the number is not have 10 digits it should raise an exception
#if the phon enumber conatain alphabets raise another exception


class digtsException(Exception):
    def __init__(self,number):
        super().__init__(number)

class alphabetException(Exception):
    def __init__(self,number):
        super().__init__(number)

def validate(number):
    if len(str(number))!=10:
        raise digtsException("number of digits is not 10")
    elif str(number).isdigit()== False:
        raise alphabetException("number cannot have alphabets")
    else:
        return True

try:
    number=int(input("enter phone number: "))
    if validate(number) == True:
        print("valid number.")
except digtsException as e:
    print(e)
except alphabetException as e:
    print(e)
except ValueError as e:
    print(e)
