from .Customer import Customer
from .Item import Item

class Order:
    def __init__(self, id, customer: Customer, orderType, item, status):
        self.orderID: int = id
        self.customer: Customer = customer
        self.orderType: str = orderType
        self.menuItem: Item = item
        self.status: str = status

    def getOrder(self):
        return {
            'orderID': self.orderID,
            'customer': self.customer,
            'orderType': self.orderType,
            'item': self.item,
            'status': self.status
        }

    def updateOrder(self):
        pass