def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())

'''
Closure is a technique which allows the storing of values in spite of the fact that the context 
in which they have been created does not exist anymore. Intricate? A bit.

Look carefully:

    * the inner() function returns the value of the variable accessible inside its scope, 
    as inner() can use any of the entities at the disposal of outer()
    * the outer() function returns the inner() function itself; more precisely, it returns a 
    copy of the inner() function, the one which was frozen at the moment of outer()'s invocation;
    the frozen function contains its full environment, including the state of all local variables,
    which also means that the value of loc is successfully retained, although outer() ceased to 
    exist a long time ago.

In effect, the code is fully valid, and outputs: 1


The function returned during the outer() invocation is a closure.
'''