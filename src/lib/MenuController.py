from .Order import Order
from .Customer import Customer
from .Item import Item

# THIS CLASS IS RESPONSIBLE FOR USER INPUT
class InputMapper:
    def __init__(self, system_instance):
        # Store a reference to the main System to access its lists and trackers
        self.system = system_instance

    def process_input(self, menuInput):
        match menuInput:
            case 1: 
                # Add new Order
                print(f"{'=' * 17}ADD ORDER{'=' * 18}")
                print("ENTER 'exit' or 'cancel' to return to menu.")
                while True: # Outer Loop
                    orderAmt = input("Input amount of order: ")
                    if orderAmt.lower() in self.system.exitCmds: return 1
                    try:
                        orderAmt = int(orderAmt)
                        if orderAmt <= 0:
                            print("Order amount must at least be one")
                            continue
                        break
                    except ValueError:
                        print("Invalid order amount.")
                        continue

                # Map Order To Person
                item = firstName = lastName = orderType = None
                firstName = input("First Name: ")
                if firstName.lower() in self.system.exitCmds: return 1
                lastName = input("Last Name: ")
                if lastName.lower() in self.system.exitCmds: return 1

                # Limit user Response to OTC or ONLINE
                orderType = None
                while True:
                    print("ORDER TYPES ACCEPTED -> [OTC, ONLINE]")
                    orderType = input("Select Order Type: ")
                    if orderType.upper() not in self.system.paymentTypes:
                        print("Invalid Order Type.\n")
                        continue
                    elif orderType.lower() in self.system.exitCmds: return 1
                    else: break    

                # Add a new amount
                for i in range(orderAmt):
                    while True:
                        item = input("Item name: ")
                        if item.lower() in self.system.exitCmds: return 1

                        matched_item = None
                        for inv in self.system.inventory:
                            if inv.name.lower() == item.lower():
                                matched_item = inv
                                break

                        # Validate if the item does not exist or there is no stock.
                        if not matched_item:
                            print(f"Item '{item}' does not exist.")
                            continue

                        if matched_item.stock <= 0:
                            print(f"There is not enough stock of {matched_item.name}")
                            continue

                        while True:
                            amount = input("Enter item amount: ")
                            if amount.lower() in self.system.exitCmds: return 1
                            try:
                                amount = int(amount)
                            except ValueError:
                                print("Invalid input.")
                                continue

                            if amount > matched_item.stock:
                                print("Amount input exceeded amount of current stock.")
                                continue

                            break

                        order = Order(self.system.orderIdTracker, Customer(firstName, lastName), orderType, matched_item, amount, 'PROCESSING')
                        self.system.orders.append(order)
                        self.system.orderIdTracker += 1
                        matched_item.stock -= amount
                        print(f"Successfully added order[{self.system.orderIdTracker - 1}] to the database.")
                        print(f"{'=' * 44}")
                        break
                return 1       
            
            case 2: 
                # Add stock/inv
                print(f"{'=' * 13}ADD INVENTORY{'=' * 18}")
                print("ENTER 'exit' or 'cancel' to return to menu.")
                while True:
                    name = input("Item name: ")
                    if name.lower() in self.system.exitCmds: return 1

                    desc = input("Description: ")
                    if desc.lower() in self.system.exitCmds: return 1

                    while True:
                        price = input("Price: ₱")
                        if price.lower() in self.system.exitCmds: return 1

                        stock = input("Stock: ")
                        if stock.lower() in self.system.exitCmds: return 1
                        try:
                            price = int(price)
                            stock = int(stock)
                            break
                        except ValueError:
                            print("Please enter a valid number.")
                            continue

                    item_exists = any(inv_item.name.lower() == name.lower() for inv_item in self.system.inventory)

                    if item_exists:
                        print("Item already exists, please enter a new one.\n")
                        continue
                    else:
                        item = Item(self.system.itemIdTracker, name, desc, stock, price)
                        self.system.inventory.append(item)
                        self.system.itemIdTracker += 1
                        print(f"Successfully added new item '{item.name}' to inventory")
                    
                    return 1
            case 3: 
                # Update stock
                print(f"{'=' * 16}UPDATE STOCK{'=' * 16}")
                print("ENTER 'exit' or 'cancel' to return to menu.")
                while True:
                    search_term = input("Enter Item Name or ID to update: ")
                    if search_term.lower() in self.system.exitCmds: return 1

                    # Find item in inventory
                    matched_item = None
                    for inv in self.system.inventory:
                        if str(inv.itemID) == search_term or inv.name.lower() == search_term.lower():
                            matched_item = inv
                            break

                    if not matched_item:
                        print("Item not found. Please try again.\n")
                        continue

                    # Sub-menu for specific updates
                    while True:
                        print(f"\n--- Editing: {matched_item.name} (Current Stock: {matched_item.stock} | Price: ₱{matched_item.price}) ---")
                        print("[1] Add to Stock")
                        print("[2] Reduce Stock")
                        print("[3] Set Exact Stock")
                        print("[4] Update Price")
                        print("[5] Back to Search")
                        
                        sub_menu = input("Select update type: ")
                        if sub_menu == '1':
                            try:
                                amt = int(input("Amount to add: "))
                                if amt > 0:
                                    matched_item.stock += amt
                                    print(f"Success! New stock: {matched_item.stock}")
                                else:
                                    print("Amount must be greater than 0.")
                            except ValueError:
                                print("Invalid number.")
                        elif sub_menu == '2':
                            try:
                                amt = int(input("Amount to reduce: "))
                                if 0 < amt <= matched_item.stock:
                                    matched_item.stock -= amt
                                    print(f"Success! New stock: {matched_item.stock}")
                                else:
                                    print("Invalid amount or exceeds current stock.")
                            except ValueError:
                                print("Invalid number.")
                        elif sub_menu == '3':
                            try:
                                amt = int(input("Set exact stock to: "))
                                if amt >= 0:
                                    matched_item.stock = amt
                                    print(f"Success! New stock: {matched_item.stock}")
                                else:
                                    print("Stock cannot be negative.")
                            except ValueError:
                                print("Invalid number.")
                        elif sub_menu == '4':
                            try:
                                new_price = int(input(f"New price: ₱"))
                                if new_price >= 0:
                                    matched_item.price = new_price
                                    print(f"Success! Price updated to ₱{matched_item.price}")
                                else:
                                    print("Price cannot be negative.")
                            except ValueError:
                                print("Invalid number.")
                        elif sub_menu == '5' or sub_menu.lower() in self.system.exitCmds:
                            break # Break inner loop to search again
                        else:
                            print("Invalid option. Please try again.")
            case 4: 
                # Update order status
                print(f"{'=' * 12}UPDATE ORDER STATUS{'=' * 13}")
                print("ENTER 'exit' or 'cancel' to return to menu.")
                while True:
                    search_term = input("Enter Order ID to update: ")
                    if search_term.lower() in self.system.exitCmds: return 1

                    matched_order = None
                    for order in self.system.orders:
                        if str(order.orderID) == search_term:
                            matched_order = order
                            break

                    if not matched_order:
                        print("Order ID not found. Please try again.\n")
                        continue

                    while True:
                        print(f"\n--- Editing Order ID: {matched_order.orderID} | Current Status: {matched_order.status} ---")
                        print("[1] Set status to PROCESSING")
                        print("[2] Set status to COMPLETED")
                        print("[3] Set status to CANCELLED")
                        print("[4] Update Item Amount")
                        print("[5] Back to Search")

                        sub_menu = input("Select update type: ")
                        if sub_menu == '1':
                            matched_order.status = "PROCESSING"
                            print("Order status updated to PROCESSING.")
                        elif sub_menu == '2':
                            matched_order.status = "COMPLETED"
                            print("Order status updated to COMPLETED.")
                        elif sub_menu == '3':
                            if matched_order.status != "CANCELLED":
                                # Refund the stock back to the inventory item
                                matched_order.menuItem.stock += matched_order.itemAmount
                                matched_order.status = "CANCELLED"
                                print("Order CANCELLED. Stock has been refunded to inventory.")
                            else:
                                print("Order is already CANCELLED.")
                        elif sub_menu == '4':
                            if matched_order.status in ["COMPLETED", "CANCELLED"]:
                                print(f"Cannot modify amount because order is {matched_order.status}.")
                                continue
                            try:
                                new_amt = int(input(f"Enter new amount (Current: {matched_order.itemAmount}): "))
                                if new_amt <= 0:
                                    print("Amount must be greater than 0.")
                                    continue
                                
                                diff = new_amt - matched_order.itemAmount
                                if diff > 0: # Adding more items to the order
                                    if diff > matched_order.menuItem.stock:
                                        print("Not enough inventory stock to increase order amount.")
                                    else:
                                        matched_order.menuItem.stock -= diff
                                        matched_order.itemAmount = new_amt
                                        print("Order amount increased successfully.")
                                elif diff < 0: # Reducing items from the order
                                    matched_order.menuItem.stock += abs(diff)
                                    matched_order.itemAmount = new_amt
                                    print("Order amount decreased. Stock refunded to inventory.")
                                else:
                                    print("Amount is unchanged.")
                            except ValueError:
                                print("Invalid number.")
                        elif sub_menu == '5' or sub_menu.lower() in self.system.exitCmds:
                            break
                        else:
                            print("Invalid option. Please try again.")
            case 5: # View Order
                print(f"{'=' * 30}ORDERS{'=' * 30}")
                if len(self.system.orders) > 0:
                    print(f"{'ID':<5}|{'NAME':<20}|{'TYPE':<10}|{'ITEM':<15}|{'AMOUNT':<8}|{'STATUS'}")
                    print(f"{'-' * 80}")
                    for i in range(len(self.system.orders)):
                        order = self.system.orders[i]
                        print(f"{order.orderID:<5}" \
                        f"|{order.customer.getFullName():<20}" \
                        f"|{order.orderType:<10}" \
                        f"|{order.menuItem.name:<15}" \
                        f"|{order.itemAmount:<8}" \
                        f"|{order.status}")
                else:
                    print("No orders in database.\n")
                print(f"{'=' * 66}\n")
                return 1
            case 6: 
                # View Menu and Prices
                print(f"{'=' * 15}MENU&PRICES{'=' * 18}")
                if len(self.system.inventory) == 0:
                    print("You have no Inventory.\n")
                else:
                    print(f"{'NAME':<15}|{'PRICE':<15}")
                    print(f"{'-' * 44}")
                    for i in range(len(self.system.inventory)):
                        item = self.system.inventory[i].getItem()
                        print(f"{item['item']['name']:<15}|{item['item']['price']}")
                print(f"{'=' * 42}\n")
                return 1
            case 7: 
                # View Inventory
                print(f"{'=' * 15}INVENTORY{'=' * 20}")
                if len(self.system.inventory) == 0:
                    print("You have no Inventory.\n")
                else:
                    print(f"{'ID':<15}|{'NAME':<15}|{'DESCRIPTION':<15}|{'PRICE':<15}|{'QUANTITY':<15}")
                    print(f"{'-' * 80}")
                    for i in range(len(self.system.inventory)):
                        item = self.system.inventory[i].getItem()
                        print(f"{item['id']:<15}" \
                            f"|{item['item']['name']:<15}" \
                            f"|{item['item']['description']:<15}" \
                            f"|{item['item']['price']:<15}" \
                            f"|{item['item']['quantity']:<15}")
                print(f"{'=' * 44}\n")
                return 1
            case 8: # View Sales
                print(f"{'=' * 15}SALES SUMMARY{'=' * 16}")
                completed_sales = 0
                processing_sales = 0

                for order in self.system.orders:
                    # Calculate total value of the current order
                    order_value = order.menuItem.price * order.itemAmount
                    
                    if order.status == 'COMPLETED':
                        completed_sales += order_value
                    elif order.status == 'PROCESSING':
                        processing_sales += order_value
                
                print(f"Total Completed Sales:   ₱{completed_sales}")
                print(f"Total Projected Sales:   ₱{processing_sales} (Processing)")
                print(f"{'-' * 44}")
                print(f"Total Expected Revenue:  ₱{completed_sales + processing_sales}")
                print(f"{'=' * 44}\n")
                return 1
            case 9: 
                # Exit
                return 0 # Changed this to 0 so 'not continueProgram' evaluates to True and breaks the main loop
            case _: 
                # Default Case -> Fallback for invalid input
                print("Invalid input.\n")
                return 1