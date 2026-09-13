from .Order import Order
from .Customer import Customer

class System:
    def __init__(self):
        """
        This is assuming we have a primitive database
        """
        self.orderIdTracker = 0
        self.itemIdTracker = 0
        self.orders = []
        self.inventory = []

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
        while True:
            self.__showMenu()
            try:
                menu = int(input("INPUT: "))
            except ValueError:
                print("Please input a valid number.\n")
                continue
            
            continueProgram = self.__mapInput(menu)
            if not continueProgram:
                break
            

    def __mapInput(self, menuInput):
        match menuInput:
            case 1: # Add new Order
                print(f"{'=' * 17}ADD ORDER{'=' * 18}")
                print("ENTER 'exit' or 'cancel' to return to menu.")
                while True: # Outer Loop
                    item = firstName = lastName = orderType = None
                    firstName = input("First Name: ")
                    if (firstName.lower() == "exit" or firstName.lower() == "cancel"):
                        break
                    lastName = input("Last Name: ")
                    if (lastName.lower() == "exit" or lastName.lower() == "cancel"):
                        break

                    # Limit user Response to OTC or ONLINE
                    types = ["OTC", "ONLINE"]
                    while True: # Inner Loop
                        print("ORDER TYPES ACCEPTED -> [OTC, ONLINE]")
                        orderType = input("Order Type: ")
                        if orderType.upper() not in types:
                            print("Invalid Order Type.")
                            continue
                        else:
                            break

                    if orderType.lower() == "exit" or orderType.lower() == "cancel":
                        break           
                    
                    # Check if item exists
                    while True:
                        item = input("Item name: ")
                        if (item.lower() == "exit" or item.lower() == "cancel"):
                            break
                        else:
                            # Try to find item
                            if (len(self.inventory) < 0):
                                print("You have no stock")
                            else:
                                for i in range(len(self.inventory)):
                                    if self.inventory[i]['item']['name'].lower() == item.lower():
                                        break
                                print(f"Item '{item}' does not exist. Re-enter Item Name")
                                continue
                        continue

                    # TODO: Check if the item is available (e.g. the quantity isnt 0)
                    if (item.lower() == "exit" or item.lower() == "cancel"):
                        break

                    order = Order(self.orderIdTracker, Customer(firstName, lastName), orderType, item, 'PROCESSING')
                    self.orders.append(order.getOrder())
                    self.orderIdTracker += 1
                    break
                print()
                return 1
            
            case 2: # Add stock/inv
                print(f"{'=' * 13}ADD INVENTORY{'=' * 18}")
                print("ENTER 'exit' or 'cancel' to return to menu.")
                while True:
                    
                    self.itemIdTracker += 1
                    pass
                return 1
            case 3: # Update stock
                return 1
            case 4: # Update order status
                return 1
            case 5: # View Order
                return 1
            case 6: # View Menu and Prices
                return 1
            case 7: # View Inventory
                return 1
            case 8: # View Sales
                return 1
            case 9: # Exit
                return
            case _: # Default Case -> Fallback for the number 0 input
                print("Invalid input.\n")
                return 1