#ploymorphism
##method overriding

class father:
    def mode_of_transport(self):
        print("cycle")


class child(father):
    def mode_of_transport(self):
        super().mode_of_transport()
        print("bike")

c=child()
c.mode_of_transport()
