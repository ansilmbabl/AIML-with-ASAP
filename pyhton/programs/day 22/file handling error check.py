#wapto open a file and read th e contents from the file and if thefile has no contents
#it has tp raise an esxception and should print "empty filw message

class EmptyFile(Exception):
    def __init__(self,file):
        super().__init__(file)

def empty(file):
    r = file.read()
    if len(r) == 0:
        raise EmptyFile("empty file")
    else:
        print(r)

try:
    f = open("f.txt","r")
    empty(f)


except FileNotFoundError as e:
    print(e)
except EmptyFile as e:
    print(e)
