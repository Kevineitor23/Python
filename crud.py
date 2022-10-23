""" Decorators """

def nuevo_decorador(a_func):

    def envueleLaFuncion():
        print(" HACIENDO algo antes de llamar a a_func()")

        a_func()

        print("Haciendo algo despues de LLamar A  a_func()")

    return  envueleLaFuncion    


def funcion_a_decorar():
    print("Primera Prueba Decorators")

decorado = nuevo_decorador(funcion_a_decorar)
decorado()


""" Usando el @ """ 

@nuevo_decorador
def funciona():
    print('segund aprueba decoratos')

print(funciona.__name__)

#Imprime 'envueleLaFuncion'  Debido al Decorator, Cambia el Nombre y sobrescribe el docstring.

""" SOLUCION functools.wraps."""

from functools import wraps

def decoratorDefinitive(a_func):
    @wraps(a_func)

    def envuelveLaFuncion05():
        print('Hacemos algo antes de llamar a a_func')

        a_func()

        print('Hacemos algo despues de llamar a  a_func()')

    return envuelveLaFuncion05 


    
""" TEST """
@decoratorDefinitive

def pruebaFinal():
    print('More Better ¡')

print(pruebaFinal.__name__)    





