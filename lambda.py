# def area_triangulo(base, altura):
#     return (base*altura)/2

# t1 = area_triangulo(5,2)
# print(t1)    

#usamos lambda para funnciones sencillas solo calculos sin condicionales

area_triangulo = lambda base, altura : (base*altura)/2
print(area_triangulo(5, 3))