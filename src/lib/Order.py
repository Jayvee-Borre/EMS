from .Customer import Customer
from .Item import Item

class Order:
    def __init__(self, id, customer: Customer, orderType, item, amt, status):
        self.orderID: int = id
        self.customer: Customer = customer
        self.orderType: str = orderType
        self.menuItem: Item = item
        self.itemAmount: int = amt
        self.status: str = status

    def getOrder(self):
        return {
            'orderID': self.orderID,
            'customer': self.customer.getName(),
            'orderType': self.orderType,
            'item': self.menuItem.name,
            'status': self.status,
            'amount': self.itemAmount
        }

    def updateOrder(self):
        pass
