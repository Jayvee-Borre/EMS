import time
from .Customer import Customer
from .Order import Order

class OrderFlow:
    def __init__(self, system_instance):
        self.system = system_instance

    def _display_menu_category(self, categories):
        print(f"\n{'-'*45}")
        print(f"{'ID':<4} | {'Item Name':<20} | {'Price':<6} | {'Stock'}")
        print(f"{'-'*45}")
        for item in self.system.inventory:
            if item.description in categories: # Matches the category assigned in CafeSystem
                print(f"[{item.itemID:02d}] | {item.name:<20} | ₱{item.price:<5} | {item.stock}")
        print(f"{'-'*45}")

    def _get_item_by_input(self, val):
        for item in self.system.inventory:
            if str(item.itemID) == val or item.name.lower() == val.lower():
                return item
        return None

    def _order_loop(self, categories, section_name, current_order_items):
        while True:
            self._display_menu_category(categories)
            choice = input(f"Choose {section_name} by ID or Name (or type 'skip'): ").strip()
            
            if choice.lower() == 'skip' or choice == '':
                break
                
            item = self._get_item_by_input(choice)
            if not item:
                print("Invalid selection. Please try again.")
                continue
                
            if item.stock <= 0:
                print("Out of stock! Please select another.")
                continue
                
            try:
                qty_input = input(f"Enter quantity for {item.name} (Max {item.stock}): ").strip()
                if qty_input.lower() == 'skip':
                    break
                    
                qty = int(qty_input)
                if qty <= 0:
                    print("Quantity must be at least 1.")
                    continue
                if qty > item.stock:
                    print(f"Not enough stock! Only {item.stock} left.")
                    continue
                
                current_order_items.append((item, qty))
                print(f"Added {qty}x {item.name}.")
            except ValueError:
                print("Invalid quantity.")
                continue
                
            again = input(f"Add Another {section_name}? (Y/N): ").strip().upper()
            if again != 'Y':
                break

    def start_sequence(self):
        # 1. START / WELCOME PAGE
        print("\n" + "="*45)
        print("           Welcome to Studio Blend           ")
        print("="*45)
        start = input("Press Enter to Start Order (or type 'exit' to quit): ")
        if start.lower() == 'exit':
            return False
            
        current_order_items = []

        while True:
            current_order_items.clear()
            
            # 2. DRINKS MENU
            print("\n" + "*"*15 + " DRINKS MENU " + "*"*15)
            self._order_loop(["Coffee", "Non-coffee", "Frappe"], "Drink", current_order_items)

            # 3. PASTRIES MENU
            print("\n" + "*"*15 + " PASTRIES MENU " + "*"*13)
            self._order_loop(["Pastries"], "Pastry", current_order_items)

            if not current_order_items:
                print("No items ordered. Returning to Start Menu...")
                return True 

            # 4. CUSTOMER INFORMATION
            print("\n--- CUSTOMER INFORMATION ---")
            customer_name = input("Enter Customer Name (First Name only): ").strip()
            if not customer_name: 
                customer_name = "Guest"

            # 5. ORDER TYPE
            print("\n--- ORDER TYPE ---")
            order_type = ""
            while True:
                order_type = input("Select Order Type (DineIn/Takeout): ").strip()
                if order_type in ["DineIn", "Takeout"]:
                    break
                print("Invalid option. Please input exactly 'DineIn' or 'Takeout'.")

            # 6. ORDER SUMMARY
            print("\n" + "="*45)
            print(f"ORDER SUMMARY FOR: {customer_name.upper()}")
            print("="*45)
            total_price = 0
            for item, qty in current_order_items:
                subtotal = item.price * qty
                total_price += subtotal
                print(f"{qty}x {item.name:<22} ₱{subtotal}")
            print(f"-"*45)
            print(f"TOTAL AMOUNT: ₱{total_price}")
            
            confirm = input("\nConfirm Order or Edit Order? (Confirm/Edit/Cancel): ").strip().lower()
            if confirm == 'edit':
                print("Restarting order process...")
                continue 
            elif confirm == 'cancel':
                print("Order cancelled. Returning to main screen...")
                return True
            else:
                break 

        # 7. PAYMENT
        print("\n--- PAYMENT ---")
        print(f"Total Amount to Pay: ₱{total_price}")
        print("Available Online Payment Methods:")
        print("(1) E-Wallet")
        print("(2) Card")
        print("(3) Other online payments")
        
        while True:
            pay_method = input("Select payment method (1/2/3): ").strip()
            if pay_method in ['1', '2', '3']:
                break
            print("Invalid payment method.")
            
        methods_map = {'1': 'E-Wallet', '2': 'Card', '3': 'Other online payments'}
        print(f"\nProcessing {methods_map[pay_method]} payment...")
        time.sleep(1) # Simulates external payment processing delay
        print("Payment Successful!")

        # Process and deduct stock internally 
        customer = Customer(customer_name)
        for item, qty in current_order_items:
            item.stock -= qty 
            new_order = Order(self.system.orderIdTracker, customer, order_type, item, qty, "COMPLETED")
            self.system.orders.append(new_order)
            
        # 8. ORDER CONFIRMATION
        print("\n" + "*"*45)
        print("              ORDER CONFIRMATION             ")
        print("*"*45)
        print(f"Order Number   : #{self.system.orderIdTracker}")
        print(f"Customer Name  : {customer.getName()}")
        print(f"Order Type     : {order_type}")
        print(f"Payment Method : {methods_map[pay_method]}")
        print(f"Total Amount   : ₱{total_price}")
        print("Status         : Payment Successful")
        print("\n         Your order is being prepared.       ")
        print("*"*45 + "\n")
        
        self.system.orderIdTracker += 1
        return True