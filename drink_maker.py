class DrinkMaker:
    def __init__(self, resources):
        self.resources = resources

    def report(self):
        """Prints a report of all resources."""
        for resource in self.resources:
            if resource == 'Ice':
                unit = 'cubes'
            else:
                unit = 'ml'
            print(f"{resource}: {self.resources[resource]}{unit}")

    def is_resource_sufficient(self, item):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for resource in self.resources:
            if self.resources[resource] < item[resource]:
                print(f"Sorry there is not enough {resource}.")
                return False
        return True

    def make_drink(self, order):
        """Deducts the required ingredients from the resources."""
        for resource in self.resources:
            self.resources[resource] -= order[resource]
        print(f"Here is your {order['Name']}. Enjoy!\n\n")
