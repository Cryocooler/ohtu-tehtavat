from email.policy import default
from functools import reduce

class Product:
    def __init__(self,name: str, saldo: int):
        self._name = name
        self._saldo = saldo

    def balance(self):
        return self._saldo
    def name(self):
        return self._name
    def increase_balance(self):
        self._saldo +=1

products = []
p1 = Product('cola', 5)
p2 = Product('pepsi',2)

products.append(p1)
products.append(p2)

for pr in products:
    print(pr.balance())

balances = map(lambda x: x.balance(), products)
print('total balance of products',sum(balances))

b2 = reduce(lambda x, y: x.balance() + y.balance(), products)
print(b2)

names = [*map(lambda x: x.name(), products)]
cont = filter(lambda x: x == 'cola', names)
print('number of matches', len(list(cont)))

ftest2 = list(filter(lambda x: x.name() == 'buro', products ))
print('ftest2', len(ftest2))

print('product names', names)

##try increasing the balance of a product in products
#access the right object first

for pr in products:
    if pr.name() == 'cola':
        pr.increase_balance()
        print('cola balance', pr.balance())


tlist = ["abcd", "bam", "could", "milk"]

# check = 0
# for l in tlist:
#     if l == 'milk':
#         check +=1

# if check == 0:
#     print('cool this works')
# elif check != 0:
#     print('there was a match')

for pr in products:
    if pr.name() == 'cola':
        products.remove(pr)
print('removed product', products)

# class Location:
#     def __init__(self, name :str, code :int):

#         if not isinstance(name, str):
#             raise Exception('name must be a string.')
#         self.name = name
#         self.code = code




# l1 = Location(123,'lol')

# print('####Constructor with def arg and instance')
# print(l1.name)
# print(l1.code)


### dynamic list

# n_list = [0] * 5
# list0 = []
# print('listan kapasiteetti', len(list0))

# n_list[len(n_list)-1] = 3

# print(n_list)

a = [1,2,3,4,5]

print(str(a[:len(a)]).join("{}"))

rts = ', '.join(str(alkio) for alkio in a)
print(rts)

pricel = {1 :'Love-All', 2: 'Fifteen-All'}

score = ""

p1_pt = 1

p1_score = pricel[p1_pt]
print((p1_score))

print(list(pricel.keys()))