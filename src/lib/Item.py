class Item:
    def __init__(self, id, name, description, quantity, price):
        self.itemID: int = id
        self.name = name
        self.description = description
        self.price: int = price
        self.stock: int = quantity