# Funciones de orden superior 
# recibe otra funcion como parametro
# filter, map, y reduce

from functools import reduce

my_list=range(1,11)

odd = list(filter(lambda x: x%2 !=0,my_list))
print(odd)

squares = list(map(lambda x: x**2, my_list))
print(squares)

multiplos = reduce(lambda a, b: a * b, my_list)
print(multiplos) 


