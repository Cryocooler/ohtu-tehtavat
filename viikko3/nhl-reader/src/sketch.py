from functools import reduce

lista = [1,2,3,4,5]

g = reduce(lambda x,y: x+y,lista)
print(g)

b = filter(lambda x,y: x>y, lista)
print(list(b))