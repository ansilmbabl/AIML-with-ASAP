#multilevel inheritence

class grand_parent:
    gf="grand father"
    gm="grand mother"

    def details(self):
        print("grand father: ",self.gf)
        print("grand mother: ",self.gm)
    
class parent(grand_parent):
    f="father"
    m="mother"

    def details(self):
        print("father: ",self.f)
        print("mother: ",self.m)

class child(parent):
    c="child"

    def print_details(self):
        print("child: ", self.c)
        parent.details(self)
        grand_parent.details(self)


child1=child()
child1.print_details()
