from .Order import Order
from .Customer import Customer
from .Item import Item
from .MenuController import InputMapper

class System:
    def __init__(self):
        self.paymentTypes = ["OTC", "ONLINE"]
        self.exitCmds = ['exit', 'cancel']
        self.orderIdTracker = 0
        self.itemIdTracker = 0
        self.orders = []
        self.inventory = []
        self.mapper = InputMapper(self)

    def __showMenu(self):
        print(f"{'=' * 20}MENU{'=' * 20}\n" \
        "[1] Add New Order\n" \
        "[2] Add Inventory/Stock\n" \
        "[3] Update Stock\n" \
        "[4] Update Order Status\n" \
        "[5] View Orders\n" \
        "[6] View Menu And Prices\n" \
        "[7] View Inventory/Stock\n" \
        "[8] View Sales Summary\n" \
        "[9] Exit\n" \
        f"{'=' * 44}\n")

    def initializeSystem(self):
        """
        Runs the system
        """
        while True:
            self.__showMenu()
            try:
                menu = int(input("INPUT: "))
            except ValueError:
                print("Please input a valid number.\n")
                continue
            
            continueProgram = self.mapper.process_input(menu)
            if not continueProgram:
                break