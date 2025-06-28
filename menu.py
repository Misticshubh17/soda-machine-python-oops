class Menu:
    def __init__(self, data):
        """Models the Menu with drinks."""
        self.items = data

    def get_items(self):
        """Returns all the names of the available menu items"""
        drink_names = ""
        for drink_name in self.items:
            drink_names += drink_name['Name']+'/'
        return drink_names[:-1]

    def find_drink(self, choice):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.items:
            if item['Name'].lower() == choice:
                return item
