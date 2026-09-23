from .Item import Item
from .MenuController import OrderFlow

class System:
    def __init__(self):
        self.orderIdTracker = 1001
        self.orders = []
        self.inventory = []
        self._load_fixed_menu()
        self.flow = OrderFlow(self)

    def _load_fixed_menu(self):
        # Format: (Category, Name, Price). We map Category to Item's 'description' field.
        menu_data = [
            ("Coffee", "Espresso", 135),
            ("Coffee", "Americano", 145),
            ("Coffee", "Cappuccino", 180),
            ("Coffee", "Spanish latte", 195),
            ("Coffee", "Mocha", 210),
            ("Coffee", "Vanilla latte", 205),
            ("Coffee", "Caramel macchiato", 220),
            ("Non-coffee", "Chocolate milk", 130),
            ("Non-coffee", "Matcha latte", 185),
            ("Non-coffee", "Strawberry milk", 140),
            ("Non-coffee", "Iced chocolate", 175),
            ("Frappe", "Caramel", 200),
            ("Frappe", "Java chip", 215),
            ("Frappe", "Matcha", 190),
            ("Frappe", "Strawberry cream", 185),
            ("Frappe", "Cookies & Cream", 210),
            ("Frappe", "Mango Yakult", 165),
            ("Pastries", "Butter Croissant", 120),
            ("Pastries", "Chocolate Croissant", 145),
            ("Pastries", "Cinnamon roll", 135),
            ("Pastries", "Banana bread", 125),
            ("Pastries", "Chocolate muffin", 140),
            ("Pastries", "Cheese Danish", 155),
            ("Pastries", "Carrot cake slice", 195)
        ]
        
        # Instantiate Items with a default stock to fulfill the stock count requirement
        for idx, (cat, name, price) in enumerate(menu_data, start=1):
            self.inventory.append(Item(idx, name, cat, 50, price))

    def initializeSystem(self):
        """
        Runs the guided Cashier Order Flow.
        """
        while True:
            continue_program = self.flow.start_sequence()
            if not continue_program:
                break