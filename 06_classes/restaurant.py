class Restaurant:
    """Simple attempt to create a restaurant class with basic methods."""

    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        """Initialize attributes to describe a restaurant."""

        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print resturant description."""
        print("This is really good restaurant. Thank you for visiting me.")
        print(f"We're {self.name} and we serve {self.type} food.")
        print(f"We have served {self.number_served} customers. We're really popular in the city!\n")

    def open_restaurant(self):
        """Simple print that resturant is open."""
        print("Restaurant is open!")

    def set_number_served(self, number):
        """Set a number of customers served."""
        self.number_served = number
    
    def increment_number_served(self, increment):
        """Set an increment value of serverd portions."""
        self.number_served += increment

class IceCreamStand(Restaurant):
    """Child class of restaurant to model this special case of restaurants."""

    def __init__(self, name, ctype) -> None:
        """Initialize the subclass."""
        super().__init__(restaurant_name=name, cuisine_type=ctype)
        self.flavors = ['strawberry', 'lemon', 'chocolate']

    def list_available_flavors(self):
        """List all available flavors that can someone order."""

        for flavor in self.flavors:
            print(f"You can choose - {flavor}.")

    print("I hope you will like it.")

steves_ice_cream_stand = IceCreamStand("Steve's Ice", 'Ice Cream')
steves_ice_cream_stand.describe_restaurant()
steves_ice_cream_stand.list_available_flavors()