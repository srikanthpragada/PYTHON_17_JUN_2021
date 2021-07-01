def fun():
    print("This is fun()")


print("Address of fun() : ", id(fun))
fun2 = fun


def fun(msg):
    print(msg)


print("Address of fun(msg) : ", id(fun))

print(type(fun))
#fun()
fun("Hello")
fun2()
