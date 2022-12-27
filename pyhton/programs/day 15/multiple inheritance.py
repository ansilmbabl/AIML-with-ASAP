##multiple inheritance

class father:
    f="father"

class mother:
    m="mother"

class child(father,mother):
    c="child"

    def details(self):
        print("father: ",self.f)
        print("mother: ",self.m)
        print("child: ",self.c)


child=child()
child.details()
