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