# Menu
# 1. product listi
# 2. productni rasmiylashtiradi
# 3. rasmiylashtirilgan narsalarni koradi
# 4. Exit

class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty


class Catalog:
    def __init__(self, name):
        self.name = name
        self.products = []


class Order:
    def __init__(self, product, qty):
        self.product = product
        self.qty = qty

class OrderCatalog:
    def __init__(self, name):
        self.name = name
        self.orders = []


product1 = Product('olma', 10000, 2000)
product2 = Product('nok', 15000, 3000)
product3 = Product('guruch', 15000, 5000)

c1 = Catalog('1-catolog')
c1.products = [product1, product2, product3]

# 1
for i in c1.products:
    print(f'{i.name}-{i.price}-{i.qty}')
print()
# 2 productni rasmiylashtirish
or1 = Order(product1, 20)
or2 = Order(product2, 10)

# # 3
# for i in Order.orders:
#     print(f'{i.product.name}-{i.qty}')

print('salom')