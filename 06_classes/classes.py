# Try it yourself

#9.1 Restaurant

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

restaurant = Restaurant('Double Pizza', 'Italian')
second_restaurant = Restaurant('Freddies', 'Asian')
third_restaurant = Restaurant('Apples', 'Organic')

# restaurant.describe_restaurant()
# second_restaurant.describe_restaurant()
# third_restaurant.describe_restaurant()

restaurant.describe_restaurant() #default value
restaurant.set_number_served(50)
restaurant.describe_restaurant() #used method to add value
restaurant.increment_number_served(1)
restaurant.describe_restaurant() #used method to increment a value

#9.3 Users

class User:
    """Simple class representing user in WebApp"""

    def __init__(self, first_name, last_name, age, email, status) -> None:
        """Initialize attributes to describe a user."""
        self.first = first_name
        self.last = last_name
        self.age = age
        self.email = email
        self.status = status
        self.login_attempts = 0
    
    def describe_user(self):
        """User the attibutes of the user and describe it."""
        print(f"Hello {self.first} {self.last}, we're glad that you're {self.status}. You have logged in {self.login_attempts} in last 24 hours.")

    def increment_login(self, increment):
        """Add number of logins to default value."""
        self.login_attempts += increment

    def restart_login_counter(self):
        """Restart to counter back to default value."""
        self.login_attempts = 0

new_user = User('Steve', 'Peter', 10, 'peter@gmail.com', 'Online')

new_user.increment_login(40)
new_user.describe_user()
new_user.restart_login_counter()
new_user.describe_user()