class Item:
    def __init__(self, id, name, description, quantity, price):
        self.itemID: int = id
        self.name = name
        self.description = description
        self.price: int = price
        self.stock: int = quantity

    def getItem(self):
        return {
            'id': self.itemID,
            'item': {
                'name': self.name,
                'description': self.description,
                'quantity': self.stock,
                'price': self.price
            }
        }