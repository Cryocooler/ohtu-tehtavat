from functools import reduce

class Product:
    def __init__(self,name: str, saldo: int):
        self._name = name
        self._saldo = saldo
    
    def balance(self):
        return self._saldo

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
