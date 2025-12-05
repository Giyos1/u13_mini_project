class OrderCatalog:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def get_info(self):
        text = f'{self.name}\n'
        for o in self.orders:
            text += f"{o.product.name} - {o.qty}\n"
        return text

