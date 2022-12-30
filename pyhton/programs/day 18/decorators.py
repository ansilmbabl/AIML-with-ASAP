#decorators


def decorator_fun(orig_fun):
    def wrapper_fun(*args):
        print("inside wrapper")
        return orig_fun(*args)
    return wrapper_fun

@decorator_fun
def display(a,b):
    print("inside 1st display",a,b)

@decorator_fun
def display2(p,q):
    print("inside 2nd dsiplay",p,q)

display(2,3)
display2(4,5)

##f1=decorator_fun(display)
##f1()
##
##f2=decorator_fun(display2)
##f2()
