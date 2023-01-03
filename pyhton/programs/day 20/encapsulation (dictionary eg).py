#Write a Python class called Dictionary and create a dictionary containing names
#of competition winner students as keys and number of their wins as values.
#implement using encapsulation

class Dictionary:

    __dic={} #private class variable(dictoinary)
    def __init__(self,name):
        self.__name = name

    def res(self):
        if self.__name in Dictionary.__dic:
            Dictionary.__dic[self.__name] += 1
        else:
            Dictionary.__dic[self.__name] = 1

    def display(self):
        print(Dictionary.__dic)

    def wins(name):
        print(name, " has " ,Dictionary.__dic[name]," wins")


#adding students and their wins
st1=Dictionary("ans") #win1
st1.res()

st1=Dictionary("ans") #win2
st1.res()

st1=Dictionary("ans") #win3
st1.res()

##cannot access private attribute(name)
#print(st1.name)

st2=Dictionary("ansi") #win1
st2.res()

st2.display() #displaying result

##cannot access private class variable
#print(st2.dic)

Dictionary.wins("ans") #getting wins of a students
