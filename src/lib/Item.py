class Item:
    def __init__(self, id, name, description, quantity, price):
        self.itemID = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = quantity

    def getItem(self):
        return {
            'id': self.itemID,
            'item': {
                'name': self.name,
                'description': self.description,
                'quantity': self.quantity,
                'price': self.price
            }
        }

    def updateItem(self):
        pass