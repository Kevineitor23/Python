from functools import wraps
from unittest import result

def nombredecorador(f):
    @wraps(f)

    def decorada(*args, **kwargs):
        if not can_run:
            return "La funcion no se ejecutara"
        return f(*args, **kwargs)
    return decorada        


def func():
    return("La funcion se esta ejecutando")

can_run = True
print(func())



def logit(fu):
    @wraps(fu)

    def with_loggins(*args, **kwargs):
        print(fu.__name__ + "was called")

        return fu(*args, **kwargs)

    return with_loggins    

@logit

def addition_func(x):
    return x + x 

result = addition_func(4)


#Salida : addition_func was called